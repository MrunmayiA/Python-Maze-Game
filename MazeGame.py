from tkinter import *
import tkinter as tk
import math
from tkinter import messagebox
import turtle
from MazeFunctions import *

def create_main_window():
    global root, btnStart, btnExit, l1, btnBack
    
    root = Tk()
    root.title("Maze Game")
    root.geometry("600x600")
    root.configure(bg="black")
    l1 = tk.Label(root, text="Welcome to the Maze Game", fg="white", bg="black", font=("arial", 20, "bold"))
    l1.place(x=135, y=180)
    
    btnStart = tk.Button(root, text="Start Game", font=("Arial", 15, "bold"), width=10, command=start_game,
                         relief='raised', bg="#A580CA", fg="white")
    btnStart.place(x=240, y=250)
    btnExit = tk.Button(root, text="Exit Game", font=("Arial", 15, "bold"), width=10, command=exit_game,
                        relief='raised', bg="#A580CA", fg="white")
    btnExit.place(x=240, y=300)

def start_game():
    btnStart.destroy()
    btnExit.destroy()
    l1.destroy()
    
    btnLevel1 = tk.Button(root, text="Level-1", command=lambda: setup_and_start(level_1), font=("Arial", 15, "bold"), width=10, relief='raised', bg="#A580CA", fg="white")
    btnLevel1.place(x=240, y=240) 
    
    btnLevel2 = tk.Button(root, text="Level-2", command=lambda: setup_and_start(level_2), font=("Arial", 15, "bold"), width=10, relief='raised', bg="#A580CA", fg="white")
    btnLevel2.place(x=240, y=300) 

    
    lblSelectLevel = tk.Label(root, text="Select Level", fg="white", bg="black", font=("Arial", 20, "bold"))
    lblSelectLevel.place(x=220, y=200)

def setup_and_start(level):
    global collected_points, win
    collected_points = 0
    
    if 'win' in globals():
        win.bye()

    root.destroy()
    
    win = turtle.Screen()
    win.bgcolor("black")
    win.title("Maze game by Mrunmayi & Shravani")
    setup_maze(level)

    #points label
    points_label = turtle.Turtle()
    points_label.hideturtle()
    points_label.color("white")
    points_label.penup()
    points_label.goto(-300, 320)
    points_label.write("Points: {}".format(collected_points), align="center", font=("Courier", 16, "bold"))

    turtle.listen()
    turtle.onkey(player.go_left, "Left")
    turtle.onkey(player.go_right, "Right")
    turtle.onkey(player.go_up, "Up")
    turtle.onkey(player.go_down, "Down")
    win.tracer(0)

    while True:
        for treasure in treasures:
            if player.is_collision(treasure):
                player.gold += treasure.gold
                collected_points += treasure.gold
                print("Player Gold: {}".format(player.gold))
                update_points_label(points_label)
                treasure.destroy()
                treasures.remove(treasure)

        if not treasures:
            messagebox.showinfo("Level Completed", "Congratulations! You've collected all the gold coins.")
            win.clear()
            turtle.bye()
            create_main_window()
            break

        win.update()

def update_points_label(points_label):
    points_label.clear()
    points_label.write("Points: {}".format(collected_points), align="center", font=("Courier", 16, "normal"))

def exit_game():
    response = messagebox.askquestion("Exit", "Are you sure you want to exit?", icon='warning')

    if response == 'yes':
        root.destroy()
        turtle.bye()

create_main_window()
root.mainloop()
