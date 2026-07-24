total_locals = 17
left_locals = 17

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

def calc_current_percentage(categ):
    global current_percentage
    global left_percentage

    if categ == "Skill":
        current_percentage += 2
        left_percentage -= 2
    else:
        current_percentage += 1
        left_percentage -= 1


print("-" * 70)
print("-" * 70)
print("PROGRESS-OMETER\n".center(60))
print("""
     Welcome to the progressometer, your favorite tool 
            of progress analysis in games

    \n""".center(60))
print("-" * 70)
print("-" * 70)
print("\n")

print("GAME SELECTED ----> HOLLOW KNIGHT <----\n\n")

option = 0

while option != 4:
    print("-" * 70)
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
            print(" --> Local")
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
                    calc_current_percentage(conq)
                case "Local":
                    local = input("What local was explored?: ")
                    add_achievement(local.capitalize(), conq)
                    left_locals -= 1
                    calc_current_percentage(conq)
                case "Charm":
                    charm = input("What charm was obtained?: ")
                    add_achievement(charm.capitalize(), conq)
                    left_charms -= 1
                    calc_current_percentage(conq)
                case "Spell":
                    spell = input("What spell was discovered?: ")
                    add_achievement(spell.capitalize(), conq)
                    left_spells -= 1
                    calc_current_percentage(conq)
                case "Skill":
                    skill = input("What skill was found?: ")
                    add_achievement(skill.capitalize(), conq)
                    left_skills -= 1
                    calc_current_percentage(conq)

        case 2:
            print("\nYour current achievements are:")
            for item, conq in my_achievements.items():
                print(f" --> {item}, {conq}")

            print(f"\nConclusion percentage: --> {current_percentage}% <--\n")

        case 3: 
            print(f"\n{left_percentage}% remaining for the game conclusion")
            
            print("\nLeft achievements:")
            print(f" --> {left_bosses} bosses")   
            print(f" --> {left_locals} locals")   
            print(f" --> {left_charms} charms")   
            print(f" --> {left_skills} skills")   
            print(f" --> {left_spells} spells\n")  

        case 4: 
            print("\nGood luck on your journey!")
            