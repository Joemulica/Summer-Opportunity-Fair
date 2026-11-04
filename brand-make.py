import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage
src = Image.open('logo-src.png').convert('RGB')
a = np.array(src).astype(int)
mn = a.min(axis=2)
# teal sample from OPPORTUNITY row
band = a[450:510, 70:890]; dark = band[band.min(axis=2) < 200]
print('teal-ish median', np.median(dark, axis=0))

def cutout(rgb_arr, pad=0):
    mnl = rgb_arr.min(axis=2)
    white = mnl > 224
    lab, n = ndimage.label(white)
    edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    bg = np.isin(lab, list(edge))
    near = ndimage.binary_dilation(bg, iterations=2) & ~bg
    alpha = np.where(bg, 0, 255).astype(float)
    soft = np.clip((255 - mnl) * 255.0 / 90.0, 0, 255)
    alpha = np.where(near, np.minimum(255, soft), alpha)
    out = np.dstack([rgb_arr, alpha]).astype(np.uint8)
    return Image.fromarray(out, 'RGBA')

# full logo cropped
x0, y0, x1, y1 = 70, 96, 887, 590
logo = cutout(a[y0-6:y1+6, x0-6:x1+6])
logo.save('logo.png')
# tiles row
tiles = cutout(a[94:292, 68:889]); tiles.save('logo-tiles.png')
# favicon: 2x2 of tiles
segs = [(70, 262), (275, 467), (480, 672), (684, 886)]
ims = []
for sx, ex in segs:
    t = cutout(a[94:292, sx-2:ex+3]); ims.append(t.resize((240, 240), Image.LANCZOS))
S = 512; g = 16
fav = Image.new('RGBA', (S, S), (0, 0, 0, 0))
pos = [(g, g), (S//2 + g//2, g), (g, S//2 + g//2), (S//2 + g//2, S//2 + g//2)]
for im, p in zip(ims, pos): fav.alpha_composite(im, p)
fav.save('icon-512.png')
fav.resize((180, 180), Image.LANCZOS).save('apple-touch-icon.png')
fav.resize((32, 32), Image.LANCZOS).save('favicon-32.png')
fav.save('favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
print(logo.size, tiles.size)
names = ["camp", "sports", "nature", "arts"]
for (sx, ex), n in zip(segs, names):
    cutout(a[94:292, sx-2:ex+3]).resize((160, 160), Image.LANCZOS).save(f'tile-{n}.png')
