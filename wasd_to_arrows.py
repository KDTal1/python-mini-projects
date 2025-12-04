import keyboard, os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    clear_screen()
    keyboard.remap_key('w', 'up')
    keyboard.remap_key('s', 'down')
    keyboard.remap_key('a', 'left')
    keyboard.remap_key('d', 'right')

    print("This is a simple script that you can make at home\nBut can be turned into an exe file for convenience\n\nJust press ESC to exit.\nOr don't, and see your messages look wonky. :)")
    keyboard.wait('esc')
    