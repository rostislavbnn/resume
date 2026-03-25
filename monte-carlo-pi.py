import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def monte_carlo_simulation(N):
    R = 0.5
    points = np.random.rand(N, 2)
    inside_circle = points[((points[:,0] - 0.5)**2 + (points[:,1] - 0.5)**2) <= R**2]
    outside_circle = points[((points[:,0] - 0.5)**2 + (points[:,1] - 0.5)**2) > R**2]
    
    # Очистка предыдущих точек
    ax.clear()
    
    # Рисование новых точек
    ax.scatter(inside_circle[:,0], inside_circle[:,1], color='red', s=1)
    ax.scatter(outside_circle[:,0], outside_circle[:,1], color='blue', s=1)
    
    # Добавление окружности
    circle = plt.Circle((0.5, 0.5), R, color='black', fill=False)
    ax.add_patch(circle)
    
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    canvas.draw()
    
    total_inside_points = inside_circle.shape[0]
    S = total_inside_points / N
    pi_approx = 4 * S
    
    # Обновление текста характеристик
    result_text.set(f"Точек внутри круга: {total_inside_points}\n"
                    f"Отношение: {S:.6f}\n"
                    f"Приближение числа Пи: {pi_approx:.6f}")

def plot_100():
    monte_carlo_simulation(100)

def plot_1000():
    monte_carlo_simulation(1000)

def plot_10000():
    monte_carlo_simulation(10000)

def plot_100000():
    monte_carlo_simulation(100000)

def clear_plot():
    ax.clear()
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Добавление окружности
    circle = plt.Circle((0.5, 0.5), 0.5, color='black', fill=False)
    ax.add_patch(circle)
    
    canvas.draw()
    result_text.set("")  # Очистка текста характеристик

# Создание основного окна
root = tk.Tk()
root.title("Метод Монте-Карло для числа Пи")
root.geometry("700x700")  # Фиксированный размер окна

# Создание фигуры для графика
fig, ax = plt.subplots(figsize=(5, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Инициализация графика при запуске приложения
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
circle = plt.Circle((0.5, 0.5), 0.5, color='black', fill=False)
ax.add_patch(circle)
canvas.draw()

# Создание текстового поля для вывода характеристик
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify=tk.LEFT, font=("Arial", 16))
result_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# Создание кнопок
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

button_100 = tk.Button(button_frame, text="100 точек", command=plot_100, font=("Arial", 14))
button_100.pack(side=tk.LEFT, padx=5, pady=5)

button_1000 = tk.Button(button_frame, text="1000 точек", command=plot_1000, font=("Arial", 14))
button_1000.pack(side=tk.LEFT, padx=5, pady=5)

button_10000 = tk.Button(button_frame, text="10000 точек", command=plot_10000, font=("Arial", 14))
button_10000.pack(side=tk.LEFT, padx=5, pady=5)

button_100000 = tk.Button(button_frame, text="100000 точек", command=plot_100000, font=("Arial", 14))
button_100000.pack(side=tk.LEFT, padx=5, pady=5)

button_clear = tk.Button(button_frame, text="Очистить график", command=clear_plot, font=("Arial", 14))
button_clear.pack(side=tk.LEFT, padx=5, pady=5)

# Запуск основного цикла
root.mainloop()