

left_achievements = {
    "Boss": 14,
    "Charm": 36,
    "Spell": 6,
    "Skill": 7,
    "Dreamer": 3,
    "Dream Nail": 3,
    "Mask Shard": 4,
    "Nail Art": 3,
    "Nail Upgrade": 4,
    "Colosseum": 3,
    "Vessel Fragment": 3,
    "Warrior Dream": 7
}

modify_input = {
    "Boss": "What main boss was defeated?",
    "Charm": "What charm was obtained?",
    "Spell": "What spell was discovered?",
    "Skill": "What skill was found?",
    "Dreamer": "How many Dreamers have you found?",
    "Dream Nail": "In wich phase is your Dream Nail?",
    "Mask Shard": "How many Mask upgrades have you got?",
    "Nail Art": "How many Nail Arts have you unlocked?",
    "Nail Upgrade": "On what stage is your Nail?",
    "Colosseum": "How many levels of Colosseum of Fools you passed through?",
    "Vessel Fragment": "How many Vessel upgrades have you got?",
    "Warrior Dream": "How many Warrior Dreams have you defeated?"
}

current_percentage = 0
left_percentage = 100

my_achievements = {}

def add_achievement(item, categ):
    try:
        int(item)
        my_achievements[categ] = item
    except ValueError:
        my_achievements[item] = categ

    print(f"\nAchievement added!\n")


def decrement_remaining(achv, cat_value):
    if achv in my_achievements.values(): 
        left_achievements[achv] -= 1
    elif achv in my_achievements.keys():
        left_achievements[achv] -= int(cat_value) 

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

    try:
        option = int(input("What operation you want to perform?: "))

        if option < 1 or option > 4:
            raise ValueError("Invalid option! Enter a number between 1 and 4")
    except ValueError as error:
        print(f"\nError: {error}")
        option = 0


    match option:
        case 1:
            print("-" * 80)
            print("\nMAIN ACHIEVEMENT CATEGORIES\n")
            print(" --> Boss")
            print(" --> Charm")
            print(" --> Spell")
            print(" --> Skill")
            print(" --> Dreamer")
            print(" --> Dream Nail")
            print(" --> Mask Shard")
            print(" --> Nail Art")
            print(" --> Nail Upgrade")
            print(" --> Colosseum")
            print(" --> Vessel Fragment")
            print(" --> Warrior Dream\n")

            try:
                achv = input("What type of achievement do you want to add?: ")
                achv = achv.title()

                if achv not in modify_input.keys():
                    raise KeyError("Please, insert a valid category name")
            except KeyError as error:
                print(f"\nError: {error}\n")
                achv = input("What type of achievement do you want to add?: ")

            finally:
                if achv not in modify_input.keys():
                    print("\nOperation cancelled due wrong inputs\n")
                    continue


            category_value = input(f"{modify_input[achv]}: ")

            add_achievement(category_value.title(), achv)
            decrement_remaining(achv, category_value)

            current_percentage = calc_current_percentage(achv, current_percentage)
            left_percentage = 100 - current_percentage

        case 2:
            print("-" * 80)
            print("\nYour current achievements are:")
            for item, achv in my_achievements.items():
                print(f" --> {item}, {achv}")

            print(f"\nConclusion percentage: --> {current_percentage}% <--\n")

        case 3: 
            print("-" * 80)
            print(f"\nRemaining for the game completion --> {left_percentage}% <-- ")
            
            print("\nLeft achievements:")
            for key, value in left_achievements.items():
                print(f" --> {key}: {value} left")  

        case 4: 
            print("\nGood luck on your journey!")
            