import sys
from .structure import Task

def main():

    if len(sys.argv) < 2:
        print("Usage: task-cli [command] [arguments]")
        print("Available commands: add, list, delete, update, mark-todo, mark-in-progress, mark-done, help")
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

    elif command == "list":
        if len(sys.argv)==3:
            one_task.show(status_Filter=sys.argv[2])
        else:one_task.show()

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Please provide a task ID. Example: task-cli delete 1")
            return
        try:
            task_id = int(sys.argv[2])
            print(one_task.delete(task_id))
        except ValueError:
            print("Error: Task ID must be a number!")
    
    elif command == "update":

        if len(sys.argv) < 4:
            print("Error: Please provide a task ID or new description. Example: task-cli update 1 [new description]")
            return
        try:
            task_id = int(sys.argv[2])
            new_description = " ".join(sys.argv[3:])
            one_task.update(id=task_id, new_description=new_description)
        except ValueError:
            print("Error: Task ID must be a number!")
    
    elif command.startswith("mark-"):
        ALLOWED_STATUSES = ["todo", "in-progress", "done", "abandoned"]
    
        new_status = command.replace("mark-", "")
    
        if new_status in ALLOWED_STATUSES:
          if len(sys.argv) < 3:
            print(f"Error: Please provide a task ID. Example: task-cli {command} 1")
            return
          try:
            task_id = int(sys.argv[2])
            one_task.update(id=task_id, new_status=new_status)
          except ValueError:
            print("Error: Task ID must be a number!")
        else:
            print(f"\n--- Error: Unknown status '{new_status}'! Use todo, in-progress, or done. ---\n")

    else:
        print(f"Unknown command: '{command}'. Type 'task-cli help' to see available commands.")

if __name__ == "__main__":
    main()

        