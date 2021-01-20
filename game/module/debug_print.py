from icecream import ic

def debug_print(text_to_print_in_terminal, text_color_str="white", bg_color_str="black"):
    text_color_nbr = 37
    if text_color_str == "red":
        text_color_nbr = 31
    if text_color_str == "green":
        text_color_nbr = 32
    if text_color_str == "yellow":
        text_color_nbr = 33
    if text_color_str == "blue":
        text_color_nbr = 34
    if text_color_str == "black":
        text_color_nbr = 30
    if text_color_str == "white":
        text_color_nbr = 37

    bg_color_nbr = 40
    if bg_color_str == "red":
        bg_color_nbr = 41
    if bg_color_str == "green":
        bg_color_nbr = 42
    if bg_color_str == "yellow":
        bg_color_nbr = 43
    if bg_color_str == "blue":
        bg_color_nbr = 44
    if bg_color_str == "black":
        bg_color_nbr = 40
    if bg_color_str == "white":
        bg_color_nbr = 47

    print(f"\033[0;{text_color_nbr};{bg_color_nbr}m")
    print(text_to_print_in_terminal)
    print(f"\033[0;37;40m")
