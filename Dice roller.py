logo="""

DDDDDDDDDDDDD          iiii                                                                                    lllllll lllllll                                         
D::::::::::::DDD      i::::i                                                                                   l:::::l l:::::l                                         
D:::::::::::::::DD     iiii                                                                                    l:::::l l:::::l                                         
DDD:::::DDDDD:::::D                                                                                            l:::::l l:::::l                                         
  D:::::D    D:::::D iiiiiii     cccccccccccccccc    eeeeeeeeeeee         rrrrr   rrrrrrrrr      ooooooooooo    l::::l  l::::l     eeeeeeeeeeee    rrrrr   rrrrrrrrr   
  D:::::D     D:::::Di:::::i   cc:::::::::::::::c  ee::::::::::::ee       r::::rrr:::::::::r   oo:::::::::::oo  l::::l  l::::l   ee::::::::::::ee  r::::rrr:::::::::r  
  D:::::D     D:::::D i::::i  c:::::::::::::::::c e::::::eeeee:::::ee     r:::::::::::::::::r o:::::::::::::::o l::::l  l::::l  e::::::eeeee:::::eer:::::::::::::::::r 
  D:::::D     D:::::D i::::i c:::::::cccccc:::::ce::::::e     e:::::e     rr::::::rrrrr::::::ro:::::ooooo:::::o l::::l  l::::l e::::::e     e:::::err::::::rrrrr::::::r
  D:::::D     D:::::D i::::i c::::::c     ccccccce:::::::eeeee::::::e      r:::::r     r:::::ro::::o     o::::o l::::l  l::::l e:::::::eeeee::::::e r:::::r     r:::::r
  D:::::D     D:::::D i::::i c:::::c             e:::::::::::::::::e       r:::::r     rrrrrrro::::o     o::::o l::::l  l::::l e:::::::::::::::::e  r:::::r     rrrrrrr
  D:::::D     D:::::D i::::i c:::::c             e::::::eeeeeeeeeee        r:::::r            o::::o     o::::o l::::l  l::::l e::::::eeeeeeeeeee   r:::::r            
  D:::::D    D:::::D  i::::i c::::::c     ccccccce:::::::e                 r:::::r            o::::o     o::::o l::::l  l::::l e:::::::e            r:::::r            
DDD:::::DDDDD:::::D  i::::::ic:::::::cccccc:::::ce::::::::e                r:::::r            o:::::ooooo:::::ol::::::ll::::::le::::::::e           r:::::r            
D:::::::::::::::DD   i::::::i c:::::::::::::::::c e::::::::eeeeeeee        r:::::r            o:::::::::::::::ol::::::ll::::::l e::::::::eeeeeeee   r:::::r            
D::::::::::::DDD     i::::::i  cc:::::::::::::::c  ee:::::::::::::e        r:::::r             oo:::::::::::oo l::::::ll::::::l  ee:::::::::::::e   r:::::r            
DDDDDDDDDDDDD        iiiiiiii    cccccccccccccccc    eeeeeeeeeeeeee        rrrrrrr               ooooooooooo   llllllllllllllll    eeeeeeeeeeeeee   rrrrrrr            

"""
import random


def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results


def main():
    print(logo)
    print("Welcome to the Dice Rolling App!")

    while True:
        num_dice = int(input("How many dice do you want to roll? (Enter 1 or 2): "))

        if num_dice not in [1, 2]:
            print("Invalid input. Please enter 1 or 2.")
            continue

        dice_results = roll_dice(num_dice)

        print(f"Result{'s' if num_dice > 1 else ''}: {', '.join(map(str, dice_results))}")

        play_again = input("Roll again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for using the Dice Rolling App!")
            break


main()