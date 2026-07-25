left_achievements = {
    "Boss": 17,
    "Spell": 6,
    "Skill": 7,
    "Charm": 40
}

modify_input = {
    "Boss": "What boss was defeated?",
    "Spell": "What spell was discovered?",
    "Skil": "What skill was found?",
    "Charm": "What charm was obtained?"
}

total_bosses = 17
total_spells = 6
total_skills = 7
total_charms = 40

current_percentage = 0
left_percentage = 100

my_achievements = {}

def add_achievement(item, categ):
    my_achievements[item] = categ
    print(f"\nAchievement added!\n")


def decrement_remaining(achv):
    left_achievements[achv] -= 1

def calc_current_percentage(categ, current_per):
    if categ == "Skill":
        current_per += 2
        return current_per
    else:
        current_per += 1
        return current_per    

print("-" * 80)
print("-" * 80)
print("HOLLOW KNIGHT TRACKER\n".center(60))
print(
     """
    Are you lost on Hollow Knight? Don't know how good you're going?
    This tool is your answer! Here you can measure your progress quickly!
    You just need to inform your achievements, and we'll make the math
   \n""".center(60))
print("-" * 80)
print("-" * 80)
print("\n")

print("PRESS START ----> HOLLOW KNIGHT <----\n\n".center(60))

option = 0

while option != 4:
    print("-" * 80)
    print("OPERATIONS\n")
    print("1 - Insert new achievement")
    print("2 - Show actual progress")
    print("3 - Left progress")
    print("4 - Leave\n")

    option = int(input("What operation you want to perform?: "))

    match option:
        case 1:
            print("\nACHIEVEMENT CATEGORIES\n")
            print(" --> Boss")
            print(" --> Charm")
            print(" --> Spell")
            print(" --> Skill\n")

            achv = input("What type of achievement do you want to add?: ")
            achv = achv.capitalize()

            name = input(f"{modify_input[achv]}: ")

            add_achievement(name.capitalize(), achv)
            decrement_remaining(achv)

            current_percentage = calc_current_percentage(achv, current_percentage)
            left_percentage = 100 - current_percentage

        case 2:
            print("\nYour current achievements are:")
            for item, achv in my_achievements.items():
                print(f" --> {item}, {achv}")

            print(f"\nConclusion percentage: --> {current_percentage}% <--\n")

        case 3: 
            print(f"\n{left_percentage}% remaining for the game conclusion")
            
            print("\nLeft achievements:")
            for key, value in left_achievements.items():
                print(f" --> {key}: {value} left")  

        case 4: 
            print("\nGood luck on your journey!")
            