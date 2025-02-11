import numpy as np
import matplotlib.pyplot as plt

# Настройка осей
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 5.5)
ax.axis('off')

# 1. Голова (Pea)
x = np.linspace(-1, 1, 400)
y_upper = 4 + np.sqrt(1 - x**2)  # Верхняя полукруглая часть
y_lower = 4 - np.sqrt(1 - x**2)  # Нижняя полукруглая часть
ax.plot(x, y_upper, color="orange", lw=4)
ax.plot(x, y_lower, color="orange", lw=4)

# 2. Уши (Kõrvad)
x_ears_left = np.linspace(-1.9, -1.1, 100)
y_ears_left = 5.5 + 0.4 * np.cos(x_ears_left + 1.5)
ax.plot(x_ears_left, y_ears_left, color="orange", lw=4)

x_ears_right = np.linspace(1.1, 1.9, 100)
y_ears_right = 5.5 + 0.4 * np.cos(x_ears_right - 1.5)
ax.plot(x_ears_right, y_ears_right, color="orange", lw=4)

# 3. Глаза (Silmad)
x_eyes_left = np.linspace(-0.8, -0.2, 100)
y_eyes_left = 4.5 + 0.1 * np.sin(x_eyes_left + 0.5)
ax.plot(x_eyes_left, y_eyes_left, color="white", lw=4)

x_eyes_right = np.linspace(0.2, 0.8, 100)
y_eyes_right = 4.5 + 0.1 * np.sin(x_eyes_right - 0.5)
ax.plot(x_eyes_right, y_eyes_right, color="white", lw=4)

# 4. Нос (Nina)
x_nose = np.linspace(-0.2, 0.2, 100)
y_nose_left = -5 * x_nose + 4.1
y_nose_right = 5 * x_nose + 3.7
ax.plot(x_nose, y_nose_left, color="black", lw=3)
ax.plot(x_nose, y_nose_right, color="black", lw=3)

# 5. Вусы (Vuntsid)
x_whiskers_left = np.linspace(-1, -0.3, 100)
y_whiskers_left_1 = -0.2 * x_whiskers_left + 4.1
y_whiskers_left_2 = 0.2 * x_whiskers_left + 3.9
ax.plot(x_whiskers_left, y_whiskers_left_1, color="black", lw=2)
ax.plot(x_whiskers_left, y_whiskers_left_2, color="black", lw=2)

x_whiskers_right = np.linspace(0.3, 1, 100)
y_whiskers_right_1 = 0.2 * x_whiskers_right + 4.1
y_whiskers_right_2 = -0.2 * x_whiskers_right + 3.9
ax.plot(x_whiskers_right, y_whiskers_right_1, color="black", lw=2)
ax.plot(x_whiskers_right, y_whiskers_right_2, color="black", lw=2)

# 6. Тело (Keha) - эллипс, более плоская форма
x_body = np.linspace(-2, 2, 400)
y_body_upper = 3 * np.sqrt(1 - (x_body / 2) ** 2) + 1
y_body_lower = -3 * np.sqrt(1 - (x_body / 2) ** 2) - 1
ax.plot(x_body, y_body_upper, color="orange", lw=6)
ax.plot(x_body, y_body_lower, color="orange", lw=6)

# 7. Лапы (Käpad)
x_paws_left = np.linspace(-1.4, -0.6, 100)
y_paws_left = 2 + 0.3 * np.sin(x_paws_left + 1)
ax.plot(x_paws_left, y_paws_left, color="orange", lw=4)

x_paws_right = np.linspace(0.6, 1.4, 100)
y_paws_right = 2 + 0.3 * np.sin(x_paws_right - 1)
ax.plot(x_paws_right, y_paws_right, color="orange", lw=4)

# 8. Хвост (Saba)
x_tail = np.linspace(2, 5, 400)
y_tail = 0.3 * np.sin(2 * x_tail) - 1.5
ax.plot(x_tail, y_tail, color="orange", lw=4)

# 9. Полосы (Triibud)
x_stripes_left = np.linspace(-1.5, -1, 100)
y_stripes_left = -0.5 * x_stripes_left + 3
ax.plot(x_stripes_left, y_stripes_left, color="black", lw=3)

x_stripes_middle = np.linspace(-0.5, 0.5, 100)
y_stripes_middle = 3 * np.ones_like(x_stripes_middle)
ax.plot(x_stripes_middle, y_stripes_middle, color="black", lw=3)

x_stripes_right = np.linspace(1, 1.5, 100)
y_stripes_right = 0.5 * x_stripes_right + 3
ax.plot(x_stripes_right, y_stripes_right, color="black", lw=3)

# Показать результат
plt.show()