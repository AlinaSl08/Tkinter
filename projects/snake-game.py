from tkinter import *
import random

#themes = {"dark": {"bg" : "grey"},"light": {"bg": "white"}}

WIDTH = 400
HEIGHT = 400
DIRECTIONS = ["Up", "Down", "Left", "Right"]
CELL_SIZE = 10  # Размер одной клетки змейки и еды
DELAY = 100     # Скорость игры (задержка между движениями змейки в мс)


root = Tk()
root.title("Змейка | Счет: 0")
root.resizable(False, False)


canvas = Canvas(root,
                width=WIDTH,
                height=HEIGHT,
                bg = "black",
                highlightthickness=0  # Убираем границу вокруг холста
                )
canvas.pack()

def create_snake():
    max_x = (WIDTH // CELL_SIZE) - 3
    max_y = (HEIGHT // CELL_SIZE) - 1
    x = random.randint(0, max_x) * CELL_SIZE
    y = random.randint(0, max_y) * CELL_SIZE
    return [(x, y), (x - CELL_SIZE, y), (x - 2 * CELL_SIZE, y)]

snake = create_snake() #голова, туловище змейки
direction = "Right" #направление движения змейки
score = 0
game_over = False




def create_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake: # Проверяем, не находится ли еда внутри змейки
            return (x, y)

food = create_food()

def draw_food():
    canvas.create_rectangle(
        food[0], food[1], food[0] + CELL_SIZE,
        food[1] + CELL_SIZE, fill="red"
    )

def draw_snake():
    for segment in snake:
        canvas.create_rectangle(
            segment[0], segment[1],
            segment[0] + CELL_SIZE,
            segment[1] + CELL_SIZE,
            fill="green",
            outline="darkgreen" # Цвет обводки
        )



def check_food_collision():
    global food, score
    if snake[0] == food:
        score += 1
        food = create_food()  # Генерируем новую еду
        return True
    return False


def move_snake():
    head_x, head_y = snake[0]

    if direction == "Up":
        new_head = (head_x, head_y - CELL_SIZE)
    elif direction == "Down":
        new_head = (head_x, head_y + CELL_SIZE)
    elif direction == "Left":
        new_head = (head_x - CELL_SIZE, head_y)
    elif direction == "Right":
        new_head = (head_x + CELL_SIZE, head_y)

    snake.insert(0, new_head)

    if not check_food_collision():
        snake.pop()

def restart_game():
    global snake, direction, food, score, game_over
    snake = create_snake()
    direction = "Right"
    food = create_food()
    score = 0
    game_over = False
    canvas.delete("all")
    draw_food()
    draw_snake()
    update_title()
    root.after(DELAY, game_loop)


def on_key_press(event):
    global direction
    key = event.keysym
    if key in DIRECTIONS:
        if (key == "Up" and direction != "Down" or
            key == "Down" and direction != "Up" or
            key == "Left" and direction != "Right" or
            key == "Right" and direction != "Left"):
            direction = key
    elif key == "space" and game_over:
        restart_game()

root.bind("<KeyPress>", on_key_press)


def update_title():
    root.title(f"Змейка | Счёт: {score}")

def game_loop():
    global snake, food, score
    if game_over:
        return

    move_snake()
    if check_wall_collision() or check_self_collision():
        end_game()
        return

    canvas.delete("all")
    draw_food()
    draw_snake()
    update_title()
    root.after(DELAY, game_loop)

def check_wall_collision():
    head_x, head_y = snake[0]
    return (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT)

def end_game():
    global game_over
    game_over = True
    canvas.create_text(
        WIDTH // 2, HEIGHT // 2,
        text=f"Игра окончена! Счёт: {score}",
        fill="white",
        font=("Arial", 24))

def check_self_collision():
    return snake[0] in snake[1:]





draw_food()
draw_snake()
root.after(DELAY, game_loop)
root.mainloop()
