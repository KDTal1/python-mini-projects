import time, os, random
import math

class Plant:
    def __init__(self, name: str = None, 
                 sunlight: int = 0, 
                 water: int = 0, 
                 soil: str = None, 
                 soil_efficiency: float = 0, 
                 soil_maintenance: float = 0):
        
        # for naming purposes
        if not name:
            self.name = "plant"
        else:
            self.name = name

        self.GROWTH_SCHEMA = { # initialize growth schematic
            'height': 1.0,
            'new_branch_prob': 0
        }

        # initialize the plant's indistributable parts
        self.age = 0 # adds in increment
        self.branches = 0 # checks how many branches

        # incrementing variable
        self.energy_used = 10

        # user inputs the factors for plant to grow.
        self.sunlight = sunlight
        self.water = water
        
        self.SOIL_SCHEMA = {
            "dry": {
                "efficiency": 0.6,
                "maintenance": 2.5
            },
            "normal": {
                "efficiency": 1.0,
                "maintenance": 1.0
            },
            "damp": {
                "efficiency": 1.1,
                "maintenance": 1.2
            },
            "drenched": {
                "efficiency": 0.7,
                "maintenance": 3.5
            },
            "custom_parameters": {
                "efficiency": soil_efficiency,
                "maintenance": soil_maintenance
            }
        }

        if not soil:
            self.soil = self.SOIL_SCHEMA["normal"]
        else:
            self.soil= self.SOIL_SCHEMA[soil]
        

    def show_info(self):
        print(f"plant_name: {self.name}\nplant_age: {self.age}\nplant_height: {self.GROWTH_SCHEMA['height']} inches\nplant_branches: {self.branches} branches\nplant_branchProb: {self.GROWTH_SCHEMA['new_branch_prob']}")
        print(f"\nSunlight: {self.sunlight}\nWater: {self.water} ounces\nSoil: {self.soil['efficiency']}")

    def calculate_nutrient(self): #for nutrients
        return (self.sunlight + self.water + self.soil["efficiency"]) / 3
    
    def calculate_decay_rate(self): # initial decay calculation, gradual decay as time passes. 
        if self.energy_used <= 0:
            return 0
        
        decay = (self.energy_used * ((((self.age * math.pi) / (self.soil["maintenance"] * self.calculate_nutrient() / 10)) * 0.5) / 200))  # considers the outside input for the decay rate to increase.
        # checking if inclusion of soil quality may increase or decrease decay rate.
        return decay 

    def calculate_distribution(self):
        if self.energy_used <= 0:
            return 0
        
        decay = self.calculate_decay_rate()
        
        energy = self.energy_used - self.soil["maintenance"] - decay
        return (self.calculate_nutrient() / len(self.GROWTH_SCHEMA)) * (energy / 100)
    
    def grow(self):
        distribution = self.calculate_distribution()
        self.GROWTH_SCHEMA['height'] += distribution * 0.5
        self.GROWTH_SCHEMA['new_branch_prob'] += distribution * 0.1
        if self.GROWTH_SCHEMA['new_branch_prob'] >= 1:
            self.branches += 1
            self.GROWTH_SCHEMA['new_branch_prob'] = 0
        self.age += 1



if __name__ == "__main__":
    allocation = [] #stores plant info
    soil_choices = ["dry", "normal", "damp", "drenched"]
    status = None
    setting = input("How many plants do you want to simulate? ")
    instance = 0 # instance starts at zero
    plant_instance = 1 # but plant_instance start at one

    if setting == "exit":
        exit()

    while instance < int(setting):
        tick = 0
        #plant = Plant(name=f"plant {plant_instance}", sunlight=random.randint(1, 10), water=random.randint(10, 30), soil=random.choice(soil_choices)) - for randomized testing
        #plant = Plant(name=f"plant {plant_instance}", sunlight=9, water=20, soil=random.choice(soil_choices)) - for static testing, but soil choices
        plant = Plant(name=f"plant {plant_instance}", sunlight=9, water=20, soil="custom_parameters", soil_efficiency=(random.uniform(0.0, 1.0)), soil_maintenance=(random.uniform(1.0, 5.0)))

        

        while True: # now set to True until decay rate breaks it.
            os.system('cls' if os.name == "nt" else 'clear')
            plant_decay = plant.calculate_decay_rate()
            plant.show_info()
            print(f"Nutrient count: {plant.calculate_nutrient()}")
            print(f"Distribution per cycle: {plant.calculate_distribution()}")
            print(f"Decay rate: {plant_decay}") # now accounts decay rate.

            time.sleep(0.05)

            if plant_decay > 1.0:
                break
            else:
                plant.grow()

            tick += 1

        time.sleep(1)
        if plant.GROWTH_SCHEMA['height'] >= 6.3:
            print("Plant is at successful rate")
            status = "Success"
        else:
            print("Plant is at failed rate")
            status = "Failed"
        
        allocation.append(f"Plant {plant_instance}, age {plant.age}: {status}")
        time.sleep(1)

        instance += 1
        plant_instance += 1

    time.sleep(0.5)
    os.system('cls' if os.name == "nt" else 'clear')

    for i in allocation:
        print(i)
    
    # Calculate batch growth probability
    successful_plants = sum(1 for result in allocation if "Success" in result)
    total_plants = len(allocation)
    success_probability = (successful_plants / total_plants) * 100 if total_plants > 0 else 0
    
    print(f"\n--- Batch Analysis ---")
    print(f"Successful Plants: {successful_plants}/{total_plants}")
    print(f"Growth Probability: {success_probability:.2f}%")
