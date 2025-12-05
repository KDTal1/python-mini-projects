from boat_pile import Rock, AutoBoat
import random, os, time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# we now add in rock
clear_screen()
rock1 = Rock(10) #initialize rock
boat1 = AutoBoat("boris", "fast")
boat2 = AutoBoat("merlin", "fast")

boat1_score = 0
boat2_score = 0

boats = [boat1, boat2]
boat_score = [boat1_score, boat2_score]
sim_win = False
winner_declared = False

boat1.show_info()
print()
boat2.show_info()

input("Press Enter to proceed with simulation.")

start_time = time.time()
while winner_declared == False:
    while sim_win == False:
        clear_screen()
        random_encounter = random.randint(1, 30)

        for i, score in zip(boats, boat_score):
            print(f"{i.name} score: {score}")
        print("=" * 30)

        if random_encounter >= 15:
            dmg = rock1.damage_inflict()

            for i in boats:
                i.score -= dmg
                i.change_speed("stop")

            print(f"Rock encountered. Removing {dmg} points from BOTH boats.")

        for i in boats:
            i.add_score()
            i.update_move()

            if i.score < 0:
                i.score = 0

        print("\n--- STATUS ---")
        boat1.show_info()
        print()
        boat2.show_info()

        print(f"\nRock encounter test: {random_encounter}")

        # Check if any boat reached the per-simulation win threshold and update its counter in boat_score
        for idx, boat in enumerate(boats):
            if boat.score >= 20:
                sim_win = True
                print(f"{boat.name} is the winner!")
                time.sleep(1)
                boat_score[idx] += 1   # update the counter stored in the list
                boat.score = 0
                break

        time.sleep(0.05)

    for i, score in zip(boats, boat_score):
        print(f"{i.name} score: {score}")

        time.sleep(1)
        if score >= 5:
            print(f"{i.name} is the final winner!")
            winner_declared = True
        else:
            sim_win = False

print("Simulation ended.")
end_time = time.time()
time.sleep(1)
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")
input("Press Enter to leave simulation. Thank you for observing.")
