"""Render an 8 s, 1920x1080, 24 fps vintage-film animation: children playing on a 1945 street."""
import math, random, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W, H, FPS, SECS = 1920, 1080, 24, 8
N = FPS * SECS
OUT = sys.argv[1] if len(sys.argv) > 1 else "street_1945.mp4"
rng = random.Random(1945)
GROUND = 1010          # foreground street baseline
CURB = 700             # top of street / curb line

# ---------------------------------------------------------------- background
def background():
    img = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(img)
    # sky
    for y in range(0, 260):
        d.line([(0, y), (W, y)], fill=int(205 - y * 0.12))
    # far rooftops / chimneys
    for x in range(0, W, 140):
        d.rectangle([x, 150, x + 140, 260], fill=120 + rng.randint(-8, 8))
        cx = x + rng.randint(20, 100)
        d.rectangle([cx, 110, cx + 24, 150], fill=95)
        d.rectangle([cx - 3, 104, cx + 27, 112], fill=85)
    # row houses
    house_w = 320
    for i, x in enumerate(range(-40, W + house_w, house_w)):
        base = 108 + (i % 3) * 10
        d.rectangle([x, 230, x + house_w, 640], fill=base)
        # bricks
        for by in range(232, 640, 14):
            off = 0 if (by // 14) % 2 else 20
            for bx in range(x - off, x + house_w, 40):
                t = base + rng.randint(-14, 10)
                d.rectangle([bx + 1, by + 1, bx + 38, by + 12], fill=t)
        # cornice
        d.rectangle([x, 222, x + house_w, 240], fill=175)
        # upstairs windows
        for wx in (x + 40, x + 190):
            d.rectangle([wx - 8, 290, wx + 98, 300], fill=170)
            d.rectangle([wx, 300, wx + 90, 430], fill=40)
            d.rectangle([wx + 42, 300, wx + 48, 430], fill=165)
            d.rectangle([wx, 362, wx + 90, 368], fill=165)
            d.rectangle([wx - 6, 430, wx + 96, 440], fill=170)
            # net curtains
            for cy in range(304, 360, 6):
                d.line([(wx + 4, cy), (wx + 38, cy)], fill=70)
        # door + bay window downstairs
        dx = x + 40
        d.rectangle([dx - 10, 470, dx + 80, 480], fill=170)
        d.rectangle([dx, 480, dx + 70, 640], fill=55 + (i % 2) * 25)
        d.ellipse([dx + 50, 555, dx + 58, 563], fill=200)
        d.rectangle([dx + 25, 495, dx + 45, 500], fill=180)
        d.rectangle([x + 150, 490, x + 290, 600], fill=45)
        for k in range(1, 3):
            d.rectangle([x + 150 + k * 46, 490, x + 153 + k * 46, 600], fill=165)
        d.rectangle([x + 145, 600, x + 295, 610], fill=170)
        # front step
        d.rectangle([dx - 15, 640, dx + 85, 652], fill=165)
    # sidewalk
    d.rectangle([0, 640, W, CURB], fill=150)
    for x in range(0, W, 110):
        d.line([(x, 640), (x - 20, CURB)], fill=125, width=2)
    d.rectangle([0, CURB, W, CURB + 14], fill=175)       # curb stone
    d.rectangle([0, CURB + 14, W, H], fill=118)
    # cobbles
    for row, y in enumerate(range(CURB + 18, H, 22)):
        h = 18 + (y - CURB) // 40
        off = (row % 2) * 20
        for x in range(-40 + off, W, 42 + (y - CURB) // 30):
            t = 110 + rng.randint(-18, 14)
            d.rounded_rectangle([x, y, x + 38 + (y - CURB) // 30, y + h], radius=6, fill=t)
    # chalk hopscotch
    hx, hy = 1250, 770
    boxes = [(0, 0), (0, 1), (-0.5, 2), (0.5, 2), (0, 3), (-0.5, 4), (0.5, 4), (0, 5)]
    for bx, by in boxes:
        x0 = hx + bx * 90
        y0 = hy + (5 - by) * 40
        d.rectangle([x0, y0, x0 + 90, y0 + 40], outline=215, width=3)
    # lamp post
    lx = 1640
    d.rectangle([lx, 300, lx + 14, 700], fill=35)
    d.rectangle([lx - 12, 680, lx + 26, 702], fill=30)
    d.polygon([(lx - 22, 300), (lx + 36, 300), (lx + 26, 250), (lx - 12, 250)], fill=60)
    d.rectangle([lx - 26, 296, lx + 40, 304], fill=30)
    d.polygon([(lx - 8, 250), (lx + 22, 250), (lx + 7, 232)], fill=30)
    d.rectangle([lx - 30, 330, lx + 44, 336], fill=30)  # ladder bar
    # parked 1940s car
    cx, cy = 140, 830
    d.rounded_rectangle([cx, cy - 70, cx + 430, cy + 20], radius=30, fill=32)
    d.chord([cx + 90, cy - 170, cx + 330, cy - 20], 180, 360, fill=32)
    d.polygon([(cx + 120, cy - 95), (cx + 200, cy - 150), (cx + 200, cy - 95)], fill=150)
    d.polygon([(cx + 215, cy - 95), (cx + 215, cy - 152), (cx + 290, cy - 128), (cx + 310, cy - 95)], fill=150)
    d.ellipse([cx - 30, cy - 80, cx + 120, cy + 30], fill=28)            # front wing
    d.ellipse([cx + 320, cy - 80, cx + 460, cy + 30], fill=28)           # rear wing
    for wx in (cx + 45, cx + 390):
        d.ellipse([wx - 50, cy - 30, wx + 50, cy + 70], fill=12)
        d.ellipse([wx - 22, cy - 2, wx + 22, cy + 42], fill=150)
    d.ellipse([cx - 22, cy - 60, cx + 8, cy - 30], fill=210)            # headlamp
    d.rectangle([cx - 40, cy + 5, cx + 470, cy + 14], fill=170)          # bumper line
    # VE-day bunting across the street
    for row, (y0, sag) in enumerate([(260, 70), (330, 55)]):
        pts = [(x, y0 + sag * math.sin(math.pi * ((x % 640) / 640))) for x in range(0, W + 1, 8)]
        d.line(pts, fill=60, width=2)
        for x in range(10 + row * 20, W, 46):
            y = y0 + sag * math.sin(math.pi * ((x % 640) / 640))
            shade = [220, 70, 150][(x // 46 + row) % 3]
            d.polygon([(x, y), (x + 32, y + 1), (x + 16, y + 36)], fill=shade)
    return img

# ---------------------------------------------------------------- figures
def seg(d, p, ang, length, w, fill):
    q = (p[0] + length * math.sin(ang), p[1] + length * math.cos(ang))
    d.line([p, q], fill=fill, width=w)
    d.ellipse([q[0] - w / 2, q[1] - w / 2, q[0] + w / 2, q[1] + w / 2], fill=fill)
    return q

def kid(d, x, ground, s, legs, arms, outfit="shorts", tone=40, skin=185, cap=True, lift=0.0, face=1):
    """legs/arms: ((thigh, knee), (thigh, knee)) angles from vertical (rad). face: +1 right, -1 left."""
    gy = ground - lift
    hip = (x, gy - 52 * s)
    sh = (x, gy - 98 * s)
    lw, aw = int(11 * s), int(8 * s)
    sock = 225
    for th, kn in legs:                       # legs
        k = seg(d, hip, th * face, 26 * s, lw, skin)
        f = seg(d, k, (th + kn) * face, 26 * s, lw, sock)
        d.ellipse([f[0] - 8 * s + 4 * s * face, f[1] - 4 * s, f[0] + 8 * s + 4 * s * face, f[1] + 5 * s], fill=20)
    if outfit == "dress":
        d.polygon([(x - 13 * s, sh[1]), (x + 13 * s, sh[1]), (x + 24 * s, hip[1] + 6 * s), (x - 24 * s, hip[1] + 6 * s)], fill=tone)
        for i in range(-2, 3):
            d.ellipse([x + i * 8 * s - 2 * s, sh[1] + 20 * s, x + i * 8 * s + 2 * s, sh[1] + 24 * s], fill=min(255, tone + 120))
    else:
        d.rounded_rectangle([x - 15 * s, sh[1], x + 15 * s, hip[1] + 4 * s], radius=int(6 * s), fill=tone)
        d.rectangle([x - 16 * s, hip[1] - 6 * s, x + 16 * s, hip[1] + 14 * s], fill=max(0, tone - 25))
        d.line([(x - 8 * s, sh[1]), (x - 8 * s, hip[1] - 6 * s)], fill=max(0, tone - 25), width=max(1, int(3 * s)))  # braces
        d.line([(x + 8 * s, sh[1]), (x + 8 * s, hip[1] - 6 * s)], fill=max(0, tone - 25), width=max(1, int(3 * s)))
    hands = []
    for th, kn in arms:                        # arms
        e = seg(d, (sh[0], sh[1] + 5 * s), th * face, 22 * s, aw, tone + 15)
        hands.append(seg(d, e, (th + kn) * face, 20 * s, aw, skin))
    d.rectangle([x - 5 * s, sh[1] - 10 * s, x + 5 * s, sh[1] + 2 * s], fill=skin)
    hc = (x + 2 * s * face, sh[1] - 24 * s)
    r = 16 * s
    d.ellipse([hc[0] - r, hc[1] - r, hc[0] + r, hc[1] + r], fill=skin)
    if cap:
        d.chord([hc[0] - r - 1, hc[1] - r - 3, hc[0] + r + 1, hc[1] + r - 6], 180, 360, fill=55)
        d.polygon([(hc[0], hc[1] - 6 * s), (hc[0] + 26 * s * face, hc[1] - 4 * s), (hc[0] + 2 * s * face, hc[1] - 1 * s)], fill=45)
    else:
        d.chord([hc[0] - r - 2, hc[1] - r - 3, hc[0] + r + 2, hc[1] + r * 0.4], 180, 360, fill=70)
        d.pieslice([hc[0] - r - 2, hc[1] - r - 3, hc[0] + r + 2, hc[1] + r], 90 if face > 0 else 270, 270 if face > 0 else 450, fill=70)
        bx_ = hc[0] - face * r * 0.7
        d.ellipse([bx_ - 7 * s, hc[1] - r - 6 * s, bx_ + 7 * s, hc[1] - r + 6 * s], fill=230)  # hair bow
        d.line([(hc[0] - r * 0.8 * face, hc[1]), (hc[0] - (r + 4 * s) * face, hc[1] + 22 * s)], fill=70, width=int(6 * s))  # plait
    d.ellipse([hc[0] + 7 * s * face - 2 * s, hc[1] - 3 * s, hc[0] + 7 * s * face + 2 * s, hc[1] + 1 * s], fill=30)
    return hands

def run_pose(p, amp=0.75):
    a = math.sin(p) * amp
    return ((a, max(0, -math.cos(p)) * 1.1 + 0.15), (-a, max(0, math.cos(p)) * 1.1 + 0.15)), \
           ((-a * 0.9, -0.9), (a * 0.9, -0.9))

STAND = ((0.12, 0.0), (-0.12, 0.0))

# ---------------------------------------------------------------- frame
def frame(bg, t):
    img = bg.copy()
    d = ImageDraw.Draw(img)
    # skipping rope group (left-centre)
    rope_w = 2 * math.pi * 1.6 * t
    ax, bx, gy = 650, 1010, 900
    s = 1.55
    hl = kid(d, ax, gy, s, STAND, ((-0.3 + 0.5 * math.sin(rope_w), -1.4), (0.1, 0.1)), "dress", 150, cap=False, face=1)
    hr = kid(d, bx, gy, s, STAND, ((-0.3 - 0.5 * math.sin(rope_w), -1.4), (0.1, 0.1)), "dress", 90, cap=False, face=-1)
    jump = max(0.0, math.sin(rope_w + math.pi / 2)) * 55
    tuck = jump / 55 * 0.8
    pa, pb = hl[0], hr[0]
    depth = math.cos(rope_w)
    rope_behind = depth > 0
    def draw_rope():
        sag = 150 * math.sin(rope_w + math.pi / 2)
        pts = []
        for i in range(31):
            u = i / 30
            px = pa[0] + (pb[0] - pa[0]) * u
            py = pa[1] + (pb[1] - pa[1]) * u + sag * math.sin(math.pi * u)
            pts.append((px, py))
        d.line(pts, fill=225, width=5)
    if rope_behind:
        draw_rope()
    kid(d, (ax + bx) / 2, gy, s, ((0.15, tuck), (-0.05, tuck * 1.2)), ((0.5, -0.2), (-0.5, 0.2)),
        "dress", 200, cap=False, lift=jump, face=1)
    if not rope_behind:
        draw_rope()

    # hoop roller crossing left -> right in the foreground
    hx = -150 + (W + 300) * (t / SECS)
    p = 2 * math.pi * 2.2 * t
    legs, arms = run_pose(p)
    s2 = 1.9
    hands = kid(d, hx, GROUND, s2, legs, ((0.9, -0.3), arms[1]), "shorts", 60, face=1)
    hr_ = 60
    hcx = hx + 95
    d.ellipse([hcx - hr_, GROUND - 2 * hr_, hcx + hr_, GROUND], outline=30, width=7)
    sp = 4 * t * (W / SECS) / hr_ * 0.25
    for k in range(4):
        a = sp + k * math.pi / 2
        d.line([(hcx, GROUND - hr_), (hcx + hr_ * 0.9 * math.cos(a), GROUND - hr_ + hr_ * 0.9 * math.sin(a))], fill=60, width=2)
    d.line([hands[0], (hcx - hr_ * 0.7, GROUND - hr_ * 1.3)], fill=25, width=5)

    # ball tossers on the right (by hopscotch)
    pa_ = (1430, 880)
    pb_ = (1830, 860)
    period = 1.6
    ph = (t % period) / period
    going = int(t / period) % 2 == 0
    u = ph if going else 1 - ph
    catchA = (not going and ph > 0.85) or (going and ph < 0.15)
    catchB = (going and ph > 0.85) or (not going and ph < 0.15)
    hA = kid(d, pa_[0], pa_[1], 1.5, STAND, ((2.6 if catchA else 1.4, -0.3), (2.4 if catchA else 0.4, -0.4)), "shorts", 110, face=1)
    hB = kid(d, pb_[0], pb_[1], 1.45, STAND, ((2.6 if catchB else 1.4, -0.3), (2.4 if catchB else 0.4, -0.4)), "shorts", 70, face=-1)
    sx, sy = pa_[0] + 40, pa_[1] - 170
    ex, ey = pb_[0] - 40, pb_[1] - 165
    bxp = sx + (ex - sx) * u
    byp = sy + (ey - sy) * u - 230 * math.sin(math.pi * u)
    d.ellipse([bxp - 17, byp - 17, bxp + 17, byp + 17], fill=235, outline=30, width=3)
    d.arc([bxp - 15, byp - 15, bxp + 15, byp + 15], 200, 340, fill=120, width=3)

    # small kid hopping on hopscotch
    hp = 2 * math.pi * 1.0 * t
    hop = abs(math.sin(hp)) * 40
    kid(d, 1340 + 30 * math.sin(hp / 2), 990 - 160 * ((math.sin(hp / 2) + 1) / 2), 1.25,
        ((0.05, 0.1), (-0.6, 1.6)), ((-1.2, 0.2), (1.2, -0.2)), "dress", 175, cap=False, lift=hop, face=-1)

    # dog trotting behind the hoop roller
    dx = hx - 260
    dp = 2 * math.pi * 3 * t
    dy = GROUND - 8
    d.ellipse([dx - 55, dy - 95, dx + 45, dy - 50], fill=200)
    d.ellipse([dx + 30, dy - 125, dx + 80, dy - 82], fill=200)
    d.ellipse([dx + 34, dy - 120, dx + 50, dy - 90], fill=60)          # ear
    d.ellipse([dx + 68, dy - 110, dx + 88, dy - 96], fill=40)          # nose
    d.line([(dx - 52, dy - 85), (dx - 85, dy - 115 + 10 * math.sin(dp * 2))], fill=200, width=8)
    for k, base in enumerate((dx - 40, dx - 25, dx + 15, dx + 30)):
        a = math.sin(dp + k * math.pi) * 0.5
        d.line([(base, dy - 58), (base + 45 * math.sin(a), dy - 58 + 45 * math.cos(a))], fill=190, width=9)
    return img

# ---------------------------------------------------------------- film look
yy, xx = np.mgrid[0:H, 0:W]
vign = 1 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) ** 1.2
vign = np.clip(vign, 0.25, 1).astype(np.float32)
sepia = np.array([1.07, 0.94, 0.74], dtype=np.float32)
nrng = np.random.default_rng(7)

def film(img, f):
    a = np.asarray(img.filter(ImageFilter.GaussianBlur(1.3)), dtype=np.float32) / 255
    a = a * vign * (0.94 + 0.06 * nrng.random())                        # vignette + flicker
    grain = nrng.normal(0, 0.055, (H // 2, W // 2)).astype(np.float32)
    a = a + np.kron(grain, np.ones((2, 2), np.float32))
    for _ in range(nrng.integers(0, 3)):                                 # vertical scratches
        x = int(nrng.integers(0, W))
        a[:, x:x + 2] += 0.25
    for _ in range(nrng.integers(0, 4)):                                 # dust specks
        x, y, r = int(nrng.integers(0, W)), int(nrng.integers(0, H)), int(nrng.integers(2, 6))
        a[max(0, y - r):y + r, max(0, x - r):x + r] *= 0.2
    a = np.clip(a * 1.18, 0, 1) ** 0.92
    rgb = np.clip(a[..., None] * sepia * 255, 0, 255).astype(np.uint8)
    # gate weave
    dy = int(round(nrng.normal(0, 1.2)))
    return np.roll(rgb, dy, axis=0).tobytes()

bg = background()
ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                       "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "slow",
                       "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", OUT], stdin=subprocess.PIPE)
for f in range(N):
    ff.stdin.write(film(frame(bg, f / FPS), f))
ff.stdin.close()
ff.wait()
print("wrote", OUT)
