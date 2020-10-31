from microbit import *
while True:
    if button_a.is_pressed():
        display.scroll("A")
    elif button_b.is_pressed():
        display.scroll("B")
    else:
        display.show(Image.GHOST)