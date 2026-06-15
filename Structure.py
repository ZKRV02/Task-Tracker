import json
from datetime import datetime

class Task:
    def __init__(self, description=None, status="todo", id=None,):
        self.id = id
        self.description = description
        self.status = status

    def add(self):
        try:
            with open("data.json", "r") as file:
                tasks = json.load(file)  
                if not isinstance(tasks, list):  
                    tasks = []
        except (FileNotFoundError, json.JSONDecodeError):
            tasks = []

        new_id = max([t["id"] for t in tasks], default=0) + 1

        date = datetime.now().strftime("%H:%M, %d.%m.%Y")

        new_task = {
            "id": new_id,
            "description": self.description,
            "status": self.status,
            "created at": date,
            "updated at": date,
        }

        tasks.append(new_task)

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)

        print(f"\n---Task added successfully, task id: {new_id}---\n")
    
    def delete(self, id):
        try:
            with open("data.json", "r", encoding="utf-8") as file:
                tasks = json.load(file)
            tasks_Updated = [i for i in tasks if i["id"] != id]

            if len(tasks) != len(tasks_Updated):
                with open("data.json", "w", encoding="utf-8") as file:
                    json.dump(tasks_Updated, file, indent=4, ensure_ascii=False)
                return (f"\n---Task removed successfully---\n")
            
            else:
                return (f"\n---Task with this ID was not found---\n")
        except (FileNotFoundError, json.JSONDecodeError):
            return "\n---You are trying to delete a task, but you don't have a file with tasks---\n"


    def show(self):
        try:
            with open("data.json", "r", encoding="utf-8") as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            tasks = []

        for task in tasks:
            print(f"{task.get('id')}. {task.get('description')}. created at: {task.get('created at')}, updated at: {task.get('updated at')}")

    def help(self):
        commands = [
             ("1. Add:", "Create a new task in the tracker"),
             ("2. Show:", "Show all tasks in the tracker"),
             ("3. Delete:", "Delete a task from the tracker"),
             ("4. Help:", "Show this help message")
            ]
        print("\n--- COMMANDS ---")
        for cmd, desc in commands:
            print(f"{cmd.ljust(12)}{desc}")
        print()