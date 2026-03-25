import tkinter as tk
import math
import random

class BugVisualization:
    def __init__(self, master):
        self.master = master
        self.master.title("Визуализация задачи о жуках")

        self.canvas = tk.Canvas(master, width=600, height=600, bg='white')
        self.canvas.pack()

        self.slider = tk.Scale(master, from_=2, to=12, orient=tk.HORIZONTAL, 
            label='Число жуков', command=self.reset_simulation)
        self.slider.pack(pady=10)

        self.animate_button = tk.Button(master, text="Начать анимацию", command=self.start_animation)
        self.animate_button.pack(pady=10)

        self.bug_count = self.slider.get()
        self.bug_colors = ['red', 'blue', 'green', 'purple', 'orange', 'yellow', 'pink', 
            'brown', 'cyan', 'magenta', 'gray', 'black']
        self.bugs = []
        self.tracks = []  # Хранение треков
        self.reset_simulation(self.bug_count)

        self.animating = False

    def reset_simulation(self, bug_count):
        self.bug_count = int(self.slider.get())
        self.animating = False  # Останавливаем анимацию при изменении количества жуков
        self.canvas.delete("all")
        self.bugs = []
        self.tracks = []
        self.draw_polygon(self.bug_count)

    def draw_polygon(self, n):
        radius = 200
        center_x, center_y = 300, 300
        self.bug_positions = []

        for i in range(n):
            angle = (2 * math.pi / n) * i
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            self.bug_positions.append([x, y])

        fill_color = self.random_muted_color()  # Генерируем случайный приглушённый цвет
        self.canvas.create_polygon(self.bug_positions, outline='black', fill=fill_color, width=2)

        for i, (x, y) in enumerate(self.bug_positions):
            bug = self.draw_bug(x, y, self.bug_colors[i % len(self.bug_colors)])
            self.bugs.append(bug)

    def draw_bug(self, x, y, color):
        size = 10
        return self.canvas.create_oval(x - size, y - size, x + size, y + size, fill=color, tags="bug")

    def random_muted_color(self):
        """Генерирует случайный приглушённый цвет."""
        r = random.randint(50, 200)
        g = random.randint(50, 200)
        b = random.randint(50, 200)
        return f'#{r:02x}{g:02x}{b:02x}'

    def start_animation(self):
        if not self.animating:
            self.animating = True
            self.animate_bugs()

    def animate_bugs(self):
        if not self.animating:
            return

        new_positions = []
        for i in range(len(self.bug_positions)):
            next_i = (i + 1) % len(self.bug_positions)
            x1, y1 = self.bug_positions[i]
            x2, y2 = self.bug_positions[next_i]
            dx, dy = x2 - x1, y2 - y1
            dist = math.sqrt(dx**2 + dy**2)

            if dist > 1:
                step = 5
                new_x = x1 + step * dx / dist
                new_y = y1 + step * dy / dist
                new_positions.append([new_x, new_y])
            else:
                new_positions.append([x1, y1])

        # Рисуем треки
        for i, pos in enumerate(new_positions):
            track_size = 2
            self.canvas.create_oval(pos[0] - track_size, pos[1] - track_size, pos[0] + track_size, 
                pos[1] + track_size, fill=self.bug_colors[i % len(self.bug_colors)], tags="track")

        # Обновляем позиции жуков
        for i, pos in enumerate(new_positions):
            self.bug_positions[i] = pos
            self.canvas.coords(self.bugs[i], pos[0] - 10, pos[1] - 10, pos[0] + 10, pos[1] + 10)

        # Поднимаем жуков на передний план
        self.canvas.tag_raise("bug")

        # Проверяем расстояние между жуками для остановки анимации
        stop_threshold = 6
        all_close = all(
            math.sqrt((new_positions[i][0] - new_positions[(i + 1) % len(new_positions)][0]) ** 2 +
                      (new_positions[i][1] - new_positions[(i + 1) % len(new_positions)][1]) ** 2) < stop_threshold
            for i in range(len(new_positions))
        )

        if not all_close:
            self.master.after(30, self.animate_bugs)
        else:
            self.animating = False  # Останавливаем анимацию, когда жуки сблизились

if __name__ == "__main__":
    root = tk.Tk()
    app = BugVisualization(root)
    root.mainloop()
