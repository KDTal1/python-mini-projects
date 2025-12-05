from boat_pile import Boat

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

test_boat = Boat("jerma", "slow")

while test_boat.score != 100:
    clear_screen()
    query = input(f"What will you do for {test_boat.name}?\nType 'help' for info\n>>> ")

    match query:
        case "boat_stop":
            test_boat.change_speed("stop")
        case "boat_speed":
            inc_dec = input("increase, or decrease?: ")
            inc_dec = "increment" if inc_dec == "increase" else ("decrement" if inc_dec == "decrease" else None)

            speed = input("Set speed? Y/N: ")

            if speed == "Y":
                speed = int(input("How much? (Write in int): "))
            else:
                speed = None

            test_boat.change_speed(inc_dec, speed)
        case "boat_move":
            test_boat.add_score()
        case "boat_info":
            test_boat.show_info()
        case "help":
            print("boat_info - Shows info of your boat\nboat_move - Moves your boat, adds your score\nboat_speed - Adds/removes your boat speed\n" \
            "boat_stop - Stops your boat entirely.\nhelp - Shows this menu.\nexit - Exits your program.\n")
        case "exit":
            print("Thanks for testing out the boat class. Boat.")
            break
        case _:
            print("Error, invalid input.")

    input("Press Enter to continue.")

    if test_boat.score == 100:
        print("Thank you for testing this interactive boat boat.")