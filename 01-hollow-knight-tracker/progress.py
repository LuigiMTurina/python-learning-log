total_bosses = 17
left_bosses = 17

total_spells = 6
left_spells = 6

total_skills = 7
left_skills = 7

total_charms = 40
left_charms = 40

current_percentage = 0
left_percentage = 100

my_achievements = {}

def add_achievement(item, categ):
    my_achievements[item] = categ
    print(f"\nAchievement added!\n")

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
            conq = input("What type of achievement do you want to add?: ")
            conq = conq.capitalize()

            match conq:
                case "Boss":
                    boss = input("What boss was defeated?: ")
                    add_achievement(boss.capitalize(), conq)
                    left_bosses -= 1
                    current_percentage = calc_current_percentage(conq, current_percentage)
                    left_percentage = 100 - current_percentage
                case "Charm":
                    charm = input("What charm was obtained?: ")
                    add_achievement(charm.capitalize(), conq)
                    left_charms -= 1
                    current_percentage = calc_current_percentage(conq, current_percentage)
                    left_percentage = 100 - current_percentage
                case "Spell":
                    spell = input("What spell was discovered?: ")
                    add_achievement(spell.capitalize(), conq)
                    left_spells -= 1
                    current_percentage = calc_current_percentage(conq, current_percentage)
                    left_percentage = 100 - current_percentage
                case "Skill":
                    skill = input("What skill was found?: ")
                    add_achievement(skill.capitalize(), conq)
                    left_skills -= 1
                    current_percentage = calc_current_percentage(conq, current_percentage)
                    left_percentage = 100 - current_percentage

        case 2:
            print("\nYour current achievements are:")
            for item, conq in my_achievements.items():
                print(f" --> {item}, {conq}")

            print(f"\nConclusion percentage: --> {current_percentage}% <--\n")

        case 3: 
            print(f"\n{left_percentage}% remaining for the game conclusion")
            
            print("\nLeft achievements:")
            print(f" --> {left_bosses} bosses")      
            print(f" --> {left_charms} charms")   
            print(f" --> {left_skills} skills")   
            print(f" --> {left_spells} spells\n")  

        case 4: 
            print("\nGood luck on your journey!")
            