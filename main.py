from structure import *
print("\n---Task-cli has started.---\n")

while True:
    user_input = input("Write command (type /help to show commands): ")
    one_task = Task()
    splited = user_input.split()
    if splited[0].capitalize() == "Add":
        splited.remove(splited[0])
        one_task = Task(description=" ".join(splited))
        one_task.add()

    if splited[0].lower() == "help":
        one_task = Task()
        one_task.help()
    
    if splited[0].lower() == "show":
        print("\n---All tasks in tracker---\n")
        one_task.show()
        print("\n---End of tasks---\n")
    
    if splited[0].lower() == "delete":
        print(one_task.delete(int(splited[1])))  
        



        