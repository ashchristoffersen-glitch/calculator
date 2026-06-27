from PIL import Image, ImageDraw, ImageFont

S = 512
img = Image.new("RGB", (S, S), "#7873f5")
d = ImageDraw.Draw(img)

# diagonal gradient: pink -> purple -> green (matches the app background)
def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

c1 = (255, 110, 196)   # #ff6ec4
c2 = (120, 115, 245)   # #7873f5
c3 = (74, 222, 128)    # #4ade80
for y in range(S):
    for_x_t = y / (S - 1)
    # vertical gradient through the three stops
    if for_x_t < 0.5:
        col = lerp(c1, c2, for_x_t / 0.5)
    else:
        col = lerp(c2, c3, (for_x_t - 0.5) / 0.5)
    d.line([(0, y), (S, y)], fill=col)

# white display panel
pad = 70
disp_top = 96
disp_h = 130
d.rounded_rectangle([pad, disp_top, S - pad, disp_top + disp_h], radius=34, fill="white")
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 86)
except Exception:
    font = ImageFont.load_default()
txt = "12+7"
bbox = d.textbbox((0, 0), txt, font=font)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
d.text(((S - tw) / 2 - bbox[0], disp_top + (disp_h - th) / 2 - bbox[1]), txt, fill="#5b3aa6", font=font)

# colorful button grid (3 x 3)
colors = ["#ffb703", "#ffb703", "#06d6a0",
          "#ffb703", "#ffb703", "#ff5d8f",
          "#8338ec", "#ffb703", "#06d6a0"]
labels = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]
grid_top = disp_top + disp_h + 40
gap = 26
cols = 3
bw = (S - 2 * pad - (cols - 1) * gap) / cols
bfont = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
for i in range(9):
    r, c = divmod(i, 3)
    x0 = pad + c * (bw + gap)
    y0 = grid_top + r * (bw + gap)
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bw], radius=24, fill=colors[i])
    lb = labels[i]
    bb = d.textbbox((0, 0), lb, font=bfont)
    lw, lh = bb[2] - bb[0], bb[3] - bb[1]
    d.text((x0 + (bw - lw) / 2 - bb[0], y0 + (bw - lh) / 2 - bb[1]), lb, fill="white", font=bfont)

img.save("icon-512.png")
img.resize((192, 192), Image.LANCZOS).save("icon-192.png")
img.resize((180, 180), Image.LANCZOS).save("apple-touch-icon.png")
print("icons written")
