import sys
from .structure import Task

def main():

    if len(sys.argv) < 2:
        print("Usage: task-cli [command] [arguments]")
        print("Available commands: add, show, delete, help")
        return
    command = sys.argv[1].lower()
    one_task = Task()

    if command == "add":
        
        description = " ".join(sys.argv[2:])
        
        if not description.strip():
            print("Error: Please provide a task description. Example: task-cli add Wash dishes")
            return
            
        one_task = Task(description=description)
        one_task.add()

    elif command in ("help", "/help"):
        one_task.help()

    elif command == "show":
        print("\n---All tasks in tracker---\n")
        one_task.show()
        print("\n---End of tasks---\n")

    elif command == "delete":
        
        if len(sys.argv) < 3:
            print("Error: Please provide a task ID. Example: task-cli delete 1")
            return
            
        try:
            task_id = int(sys.argv[2])
            print(one_task.delete(task_id))
        except ValueError:
            print("Error: Task ID must be a number!")

    else:
        print(f"Unknown command: '{command}'. Type 'task-cli help' to see available commands.")

if __name__ == "__main__":
    main()

        