import turtle

screen = turtle.Screen()
screen.setup(height=750, width=650)
screen.bgpic("Map Of India.png")


def get_mouse_click(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click)
turtle.mainloop()
