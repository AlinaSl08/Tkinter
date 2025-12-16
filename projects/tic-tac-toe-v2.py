import tkinter  as tk
from tkinter import messagebox
import random


root = tk.Tk()
root.title("Крестики-нолики")
#root.geometry("400x400")
root.iconbitmap("icon1.ico")

buttons = []

score_x = 0
score_o = 0

def handle_click(index):
    if game_mode == "pvp":
        on_click(index)
    else:
        on_click_computer(index)


for i in range(9): #создает игровое поле
    button = tk.Button(
        root,
        text="",
        font="Arial 30",
        width=5,
        height=2,
        command=lambda idx=i: handle_click(idx)
        )
    button.grid(row=i//3, column=i%3) # размещает кнопку в таблице 3×3. row=i//3 – вычисляет номер строки. column=i%3 – вычисляет номер столбца.
    buttons.append(button)

game_mode = "pvp"
current_player = "X" #чей ход, по-умолчанию у Х
HIGHLIGHT_COLOR = "#ffd966"
current_theme = "light"
game_over = False
themes = {
    "light": {"bg": "#f0f0f0", "button_bg": "#ffffff", "button_fg": "#000000"},
    "dark":  {"bg": "#2b2b2b", "button_bg": "#444444", "button_fg": "#f0f0f0"}
}

def hex_to_rgb(color):
    color = color.lstrip("#")
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

def interpolate(c1, c2, step, total):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * step / total) for i in range(3))

def animate_theme(from_theme, to_theme, step=0, steps=15):
    if step > steps:
        return

    bg = rgb_to_hex(interpolate(hex_to_rgb(themes[from_theme]["bg"]),
                                hex_to_rgb(themes[to_theme]["bg"]),
                                step, steps))
    btn_bg = rgb_to_hex(interpolate(hex_to_rgb(themes[from_theme]["button_bg"]),
                                   hex_to_rgb(themes[to_theme]["button_bg"]),
                                   step, steps))
    btn_fg = rgb_to_hex(interpolate(hex_to_rgb(themes[from_theme]["button_fg"]),
                                   hex_to_rgb(themes[to_theme]["button_fg"]),
                                   step, steps))

    root.config(bg=bg)

    for button in buttons:
        if button["bg"] != "lightgreen":  # победная линия не меняется
            button.config(bg=btn_bg, fg=btn_fg)

    reset_button.config(bg=btn_bg, fg=btn_fg)
    score_label.config(bg=bg, fg=btn_fg)

    root.after(20, lambda: animate_theme(from_theme, to_theme, step+1, steps))
def toggle_theme():
    global current_theme
    new_theme = "dark" if current_theme == "light" else "light"
    animate_theme(current_theme, new_theme)
    current_theme = new_theme


def set_pvp():
    global game_mode
    game_mode = "pvp"
    reset_game()
    messagebox.showinfo("Режим игры", "Режим: Игрок против игрока")

def set_pve():
    global game_mode
    game_mode = "pve"
    reset_game()
    messagebox.showinfo("Режим игры", "Режим: Игрок против компьютера")

def computer_move():
    global current_player, HIGHLIGHT_COLOR
    empty_cells = [i for i, b in enumerate(buttons) if b["text"] == ""]
    if empty_cells:
        index = random.choice(empty_cells)
        buttons[index]["text"] = current_player
        theme = themes[current_theme]
        buttons[index].config(bg=HIGHLIGHT_COLOR, fg=theme["button_fg"])
        root.after(300, lambda idx=index: restore_button_color(idx))

def restore_button_color(index):
    if buttons[index]["bg"] == "lightgreen":
        return
    theme = themes[current_theme]
    buttons[index].config(bg=theme["button_bg"], fg=theme["button_fg"])

def computer_turn():
    global current_player, score_o, game_over
    if game_over:
        return
    computer_move()
    if check_winner():
        score_o += 1
        update_score()
        messagebox.showinfo("Поражение", "Компьютер победил!", parent=root)
        return
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Ничья!", "Игра окончена. Ничья!", parent=root)
        return
    current_player = "X"


def on_click(index):
    global current_player, score_x, score_o, game_over
    if game_over:
        reset_game()
        return
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player
        if check_winner():
            if current_player == "X":
                score_x += 1
            else:
                score_o += 1

            update_score()
            messagebox.showinfo("Победа!", f"Победил {current_player}!", parent=root)
        elif all(button["text"] != "" for button in buttons):
            messagebox.showinfo("Ничья!", "Игра окончена. Ничья!", parent=root)
        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"


def on_click_computer(index):
    global current_player, score_x, game_over
    if game_over:
        reset_game()
        return

    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player
        theme = themes[current_theme]
        buttons[index].config(fg=theme["button_fg"])  # текст видим
        if check_winner():
            score_x += 1
            update_score()
            messagebox.showinfo("Победа!", f"Победил {current_player}!", parent=root)
            return
        if all(button["text"] != "" for button in buttons):
            messagebox.showinfo("Ничья!", "Игра окончена. Ничья!", parent=root)
        current_player = "O"
        root.after(400, computer_turn)

def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        a, b, c = combo
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            buttons[a].config(bg="lightgreen")
            buttons[b].config(bg="lightgreen")
            buttons[c].config(bg="lightgreen")
            return True
    return False

def reset_game():
    global current_player, game_over
    current_player = "X"
    game_over = False
    theme = themes[current_theme]
    for button in buttons:
        button.config(text="", bg=theme["button_bg"], fg=theme["button_fg"])
    score_label.config(bg=theme["bg"], fg=theme["button_fg"])
    reset_button.config(bg=theme["button_bg"], fg=theme["button_fg"])

reset_button = tk.Button(root, text="Новая игра", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="we") # Размещает кнопку под игровым полем. columnspan=3 — кнопка растягивается на всю ширину (3 колонки). sticky="we" — заполняет всю доступную ширину.

def update_score():
    score_label.config(text=f"X: {score_x} | O: {score_o}")

score_label = tk.Label(root, text="X: 0 | O: 0", font=("Arial", 14))
score_label.grid(row=4, column=0, columnspan=3)

menu = tk.Menu(root)
root.config(menu=menu)

settings_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Настройки", menu=settings_menu)
settings_menu.add_command(label="Новая игра", command=reset_game)
settings_menu.add_separator()
settings_menu.add_command(label="Выход", command=root.quit)
mode_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Режим игры", menu=mode_menu)

mode_menu.add_command(label="Игрок vs Игрок", command=set_pvp)
mode_menu.add_command(label="Игрок vs Компьютер", command=set_pve)


settings_menu.add_command(label="Сменить тему", command=toggle_theme)
theme_button = tk.Button(root, text="🌙/☀", command=toggle_theme)
theme_button.grid(row=5, column=0, columnspan=3, sticky="we")


root.mainloop()
