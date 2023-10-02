logo="""

TTTTTTTTTTTTTTTTTTTTTTT                               d::::::d                      lllllll   iiii                            tttt          
T:::::::::::::::::::::T                               d::::::d                      l:::::l  i::::i                        ttt:::t          
T:::::::::::::::::::::T                               d::::::d                      l:::::l   iiii                         t:::::t          
T:::::TT:::::::TT:::::T                               d:::::d                       l:::::l                                t:::::t          
TTTTTT  T:::::T  TTTTTTooooooooooo            ddddddddd:::::d    ooooooooooo         l::::l iiiiiii     ssssssssss   ttttttt:::::ttttttt    
        T:::::T      oo:::::::::::oo        dd::::::::::::::d  oo:::::::::::oo       l::::l i:::::i   ss::::::::::s  t:::::::::::::::::t    
        T:::::T     o:::::::::::::::o      d::::::::::::::::d o:::::::::::::::o      l::::l  i::::i ss:::::::::::::s t:::::::::::::::::t    
        T:::::T     o:::::ooooo:::::o     d:::::::ddddd:::::d o:::::ooooo:::::o      l::::l  i::::i s::::::ssss:::::stttttt:::::::tttttt    
        T:::::T     o::::o     o::::o     d::::::d    d:::::d o::::o     o::::o      l::::l  i::::i  s:::::s  ssssss       t:::::t          
        T:::::T     o::::o     o::::o     d:::::d     d:::::d o::::o     o::::o      l::::l  i::::i    s::::::s            t:::::t          
        T:::::T     o::::o     o::::o     d:::::d     d:::::d o::::o     o::::o      l::::l  i::::i       s::::::s         t:::::t          
        T:::::T     o::::o     o::::o     d:::::d     d:::::d o::::o     o::::o      l::::l  i::::i ssssss   s:::::s       t:::::t    tttttt
      TT:::::::TT   o:::::ooooo:::::o     d::::::ddddd::::::ddo:::::ooooo:::::o     l::::::li::::::is:::::ssss::::::s      t::::::tttt:::::t
      T:::::::::T   o:::::::::::::::o      d:::::::::::::::::do:::::::::::::::o     l::::::li::::::is::::::::::::::s       tt::::::::::::::t
      T:::::::::T    oo:::::::::::oo        d:::::::::ddd::::d oo:::::::::::oo      l::::::li::::::i s:::::::::::ss          tt:::::::::::tt
      TTTTTTTTTTT      ooooooooooo           ddddddddd   ddddd   ooooooooooo        lllllllliiiiiiii  sssssssssss              ttttttttttt  
"""

tasks = []
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")
def list_tasks():
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")
def remove_task(index):
    if 1 <= index <= len(tasks):
        task = tasks.pop(index - 1)
        print(f"Task '{task}' removed.")
    else:
        print("Invalid task index.")

while True:
    print(logo)
    print("Welcome to the To Do List app")
    print("\nMenu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")



