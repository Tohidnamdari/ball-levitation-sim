import pygame
import time

# -------------------------------
# ⚙️ تنظیمات اولیه شبیه‌سازی
# -------------------------------
WIDTH, HEIGHT = 400, 600
FPS = 60

# ثابت‌های فیزیکی
g = 9.81          # گرانش
m = 0.05          # جرم توپ (kg)
k = 0.002         # ضریب نیروی موتور (قدرت باد)
dt = 0.05         # گام زمانی

# PID ضرایب
Kp = 2.0
Ki = 0.05
Kd = 1.0

target_height = 300  # ارتفاع هدف اولیه (پیکسل)
integral = 0
prev_error = 0

# مقدارهای اولیه توپ
y = 500        # موقعیت توپ (پیکسل)
v = 0          # سرعت توپ

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🔥 Ball Levitation Simulation (PID Control)")
clock = pygame.time.Clock()
font = pygame.font.SysFont("tahoma", 18)

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)
RED = (255, 0, 0)
GREY = (220, 220, 220)

running = True
paused = False

# -------------------------------
# 🎮 حلقه‌ی اصلی شبیه‌سازی
# -------------------------------
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # --- رویدادهای کیبورد ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # تغییر ارتفاع هدف با کلیدها
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        target_height -= 2
    if keys[pygame.K_DOWN]:
        target_height += 2

    target_height = max(100, min(500, target_height))

    # --- PID کنترل ---
    error = (target_height - y)
    integral += error * dt
    derivative = (error - prev_error) / dt
    prev_error = error

    motor_speed = Kp * error + Ki * integral + Kd * derivative
    motor_speed = max(0, min(255, motor_speed))  # محدودسازی توان موتور

    # --- شبیه‌سازی فیزیک ---
    force_up = k * motor_speed
    force_down = m * g
    a = (force_up - force_down) / m

    v += a * dt
    y += v * 100 * dt  # ضریب برای بزرگنمایی در پیکسل

    # محدودسازی مرزها
    if y > 550:
        y = 550
        v = 0
    if y < 50:
        y = 50
        v = 0

    # --- رسم محفظه و توپ ---
    pygame.draw.rect(screen, GREY, (150, 50, 100, 500), 4)
    pygame.draw.circle(screen, BLUE, (200, int(y)), 20)
    pygame.draw.rect(screen, RED, (150, 550, 100, 10))  # موتور

    # --- نمایش اطلاعات ---
    info = [
        f"Target Height: {target_height:.1f} px",
        f"Current Height: {y:.1f} px",
        f"Motor Speed: {motor_speed:.1f}",
        f"Error: {error:.1f}",
        f"Use ↑ / ↓ to change target height"
    ]
    for i, text in enumerate(info):
        txt = font.render(text, True, BLACK)
        screen.blit(txt, (10, 10 + i * 25))

    pygame.display.flip()
    time.sleep(dt)

pygame.quit()
