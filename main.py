def on_button_pressed_a():
    global lepra
    lepra += 1
    if lepra == 1:
        basic.show_leds("""
            # . . . .
                        # # # . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 2:
        basic.show_leds("""
            # # # . .
                        # . . . .
                        # . . . .
                        # . . . .
                        . . . . .
        """)
    if lepra == 3:
        basic.show_leds("""
            # # # . .
                        # . . . .
                        # # # . .
                        # . . . .
                        . . . . .
        """)
    if lepra == 4:
        basic.show_leds("""
            # # # . .
                        # . . . .
                        # . . . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 5:
        basic.show_leds("""
            # . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 6:
        basic.show_leds("""
            # . . . .
                        # . . . .
                        # # # . .
                        # . . . .
                        . . . . .
        """)
    if lepra == 7:
        basic.show_leds("""
            # # # . .
                        # # # . .
                        # . . . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 7:
        basic.show_leds("""
            # # # . .
                        # # # . .
                        # . . . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 8:
        basic.show_leds("""
            # . . . .
                        # . . . .
                        # . . . .
                        # . . . .
                        . . . . .
        """)
    if lepra == 9:
        basic.show_leds("""
            # . . . .
                        # . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 10:
        basic.show_leds("""
            # . . . .
                        # # # . .
                        # # # . .
                        # # # . .
                        . . . . .
        """)
    if lepra == 11:
        basic.show_leds("""
            # # # . .
                        # . . . .
                        # # # . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 12:
        basic.show_leds("""
            # . . . .
                        # # # . .
                        # . . . .
                        # . . . .
                        . . . . .
        """)
    if lepra == 13:
        basic.show_leds("""
            # # # . .
                        # # # . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 14:
        basic.show_leds("""
            # # # . .
                        # # # . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 15:
        basic.show_leds("""
            # # # . .
                        # . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 1:
        basic.show_leds("""
            # # # . .
                        # # # . .
                        # # # . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 16:
        basic.show_leds("""
            # . . . .
                        # # # . .
                        # # # . .
                        # . . . .
                        . . . . .
        """)
    if lepra == 17:
        basic.show_leds("""
            # # # . .
                        # # # . .
                        # . . . .
                        # # # . .
                        . . . . .
        """)
    if lepra == 18:
        basic.show_leds("""
            # . . . .
                        # # # . .
                        # . . . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 19:
        basic.show_leds("""
            # . . . .
                        # . . . .
                        # . . . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 20:
        basic.show_leds("""
            # # # . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 21:
        basic.show_leds("""
            # . . . .
                        # . . . .
                        # # # . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 22:
        basic.show_leds("""
            # . . . .
                        # . . . .
                        # . . . .
                        # # # . .
                        . . . . .
        """)
    if lepra == 23:
        basic.show_leds("""
            # . . . .
                        # # # . .
                        # # # . .
                        . . . . .
                        . . . . .
        """)
    if lepra == 24:
        basic.show_leds("""
            # # # . .
                        # . . . .
                        # . . . .
                        # # # . .
                        . . . . .
        """)
    if lepra == 25:
        basic.show_leds("""
            # # # . .
                        # . . . .
                        # # # . .
                        # # # . .
                        . . . . .
        """)
    if lepra == 26:
        basic.show_leds("""
            # # # . .
                        # # # . .
                        # . . . .
                        # . . . .
                        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if lepra == 1:
        basic.show_string("A")
    elif lepra == 2:
        basic.show_string("B")

    else:
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

lepra = 0
lepra = 0