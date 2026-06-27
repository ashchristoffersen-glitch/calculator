// Simple offline cache for the Kids Calculator app.
const CACHE = 'kidscalc-v2';
// The app shell must be cached for offline to work at all.
const CORE = ['./', './index.html'];
// Nice-to-have extras (icons/manifest) cached best-effort, so a single
// missing/failed asset never breaks offline support.
const EXTRA = [
  './manifest.webmanifest',
  './icon-192.png',
  './icon-512.png',
  './apple-touch-icon.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE)
      .then((cache) => cache.addAll(CORE)
        .then(() => Promise.allSettled(EXTRA.map((u) => cache.add(u)))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

function cachePut(req, res) {
  // Only cache successful responses so a transient error page can't get
  // stored and served forever.
  if (res && res.ok) {
    const copy = res.clone();
    caches.open(CACHE).then((cache) => cache.put(req, copy)).catch(() => {});
  }
  return res;
}

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  // Navigations: network-first so a freshly deployed app is picked up while
  // online, falling back to the cached shell when offline.
  if (req.mode === 'navigate') {
    event.respondWith(
      fetch(req)
        .then((res) => cachePut(req, res))
        .catch(() => caches.match(req).then((c) => c || caches.match('./index.html')))
    );
    return;
  }

  // Other assets (icons, manifest): stale-while-revalidate — serve the cached
  // copy immediately (if any) while refreshing it from the network in the
  // background; otherwise fetch. Always resolve with a valid Response offline.
  event.respondWith(
    caches.match(req).then((cached) => {
      const network = fetch(req)
        .then((res) => cachePut(req, res))
        .catch(() => new Response('', { status: 408, statusText: 'Offline' }));
      return cached || network;
    })
  );
});
