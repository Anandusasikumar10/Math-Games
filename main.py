import random
import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import numpy as np


# -------- 1. Scatter Plot Game -------- #
def scatter_plot_game(num_points=5, grid_size=10):
    points = [(random.randint(0, grid_size), random.randint(0, grid_size)) for _ in range(num_points)]

    x_vals, y_vals = zip(*points)
    plt.figure()
    plt.scatter(x_vals, y_vals, color='red')
    plt.xlim(0, grid_size + 1)
    plt.ylim(0, grid_size + 1)
    plt.title("Guess the Coordinates of the Points")
    plt.grid(True)
    plt.show()

    score = 0
    for i, point in enumerate(points):
        user_input = input(f"Guess coordinates of point {i+1} (format x,y): ")
        try:
            x, y = map(int, user_input.strip().split(','))
            if (x, y) == point:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer was {point}")
        except:
            print("Invalid input format. Skipping.")

    print(f"\nYour Score: {score}/{num_points}")


# -------- 2. Algebra Practice Game -------- #
def algebra_game(num_questions=5, difficulty='easy'):
    ops = ['+', '-', '*', '//']
    score = 0

    for _ in range(num_questions):
        if difficulty == 'easy':
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            x = random.randint(-10, 10)
            expr = f"{a}*x + {b}" if random.choice([True, False]) else f"{a}*x - {b}"
            solution = eval(expr.replace('x', str(x)))
            question = f"{expr} = {solution}"
        else:  # two-step
            a = random.randint(-20, 20)
            b = random.randint(-20, 20)
            c = random.randint(-20, 20)
            x = random.randint(-10, 10)
            expr = f"{a}*x + {b} = {c}"
            left = eval(f"{a}*{x} + {b}")
            question = f"{a}x + {b} = {c}"
            solution = (c - b) // a if a != 0 else 'undefined'

        print("Solve for x:")
        print(question)
        try:
            user_answer = int(input("x = "))
            if user_answer == x:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer was x = {x}\n")
        except:
            print("Invalid input. Skipping.\n")

    print(f"Your Score: {score}/{num_questions}")


# -------- 3. Projectile Game -------- #
def projectile_game():
    def draw_projectile(a, b, c, wall_x, wall_height):
        x_vals = np.linspace(0, 20, 400)
        y_vals = a * x_vals**2 + b * x_vals + c

        plt.figure()
        plt.plot(x_vals, y_vals, label="Projectile")
        plt.axvline(x=wall_x, color='r', linestyle='--', label="Wall")
        plt.axhline(y=wall_height, xmin=wall_x/20, xmax=wall_x/20, color='r')
        plt.xlim(0, 20)
        plt.ylim(0, max(y_vals)+5)
        plt.legend()
        plt.title("Projectile Game")
        plt.grid(True)
        plt.show()

        wall_y = a * wall_x**2 + b * wall_x + c
        return wall_y > wall_height

    def slider_mode():
        wall_x = random.randint(5, 15)
        wall_height = random.randint(5, 15)

        def check():
            a = float(a_slider.get())
            b = float(b_slider.get())
            c = float(c_slider.get())
            cleared = draw_projectile(a, b, c, wall_x, wall_height)
            result = "✅ You cleared the wall!" if cleared else "❌ You hit the wall!"
            messagebox.showinfo("Result", result)

        win = tk.Tk()
        win.title("Projectile Slider Game")
        tk.Label(win, text=f"Wall is at x={wall_x}, height={wall_height}").pack()

        a_slider = tk.Scale(win, from_=-2, to=0, resolution=0.1, orient=tk.HORIZONTAL, label='a')
        b_slider = tk.Scale(win, from_=0, to=20, resolution=1, orient=tk.HORIZONTAL, label='b')
        c_slider = tk.Scale(win, from_=0, to=10, resolution=1, orient=tk.HORIZONTAL, label='c')
        a_slider.pack()
        b_slider.pack()
        c_slider.pack()

        tk.Button(win, text="Shoot", command=check).pack()
        win.mainloop()

    def input_mode():
        wall_x = random.randint(5, 15)
        wall_height = random.randint(5, 15)
        print(f"\nWall is at x = {wall_x} and has height = {wall_height}")
        try:
            a = float(input("Enter value of a: "))
            b = float(input("Enter value of b: "))
            c = float(input("Enter value of c: "))
            cleared = draw_projectile(a, b, c, wall_x, wall_height)
            result = "✅ You cleared the wall!" if cleared else "❌ You hit the wall!"
            print(result)
        except:
            print("Invalid input.")

    choice = input("Choose mode: (1) Slider mode, (2) Enter a, b, c manually: ")
    if choice == '1':
        slider_mode()
    else:
        input_mode()


# --------- Main Menu --------- #
def main():
    while True:
        print("\n📘 Math Games Menu:")
        print("1. Scatter Plot Game")
        print("2. Algebra Practice Game")
        print("3. Projectile Game")
        print("4. Exit")

        choice = input("Choose a game (1-4): ")
        if choice == '1':
            scatter_plot_game()
        elif choice == '2':
            diff = input("Choose difficulty (easy/hard): ").strip().lower()
            algebra_game(difficulty=diff)
        elif choice == '3':
            projectile_game()
        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
