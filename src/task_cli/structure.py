import json
from datetime import datetime
from pathlib import Path
import textwrap

HOME_DIR = Path.home()
DATA_FILE = HOME_DIR / ".task_tracker_data.json"

class Task:
    def __init__(self, description=None, status="todo", id=None):
        self.id = id
        self.description = description
        self.status = status

    def add(self):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                tasks = json.load(file)  
                if not isinstance(tasks, list):  
                    tasks = []
        except (FileNotFoundError, json.JSONDecodeError):
            tasks = []

        new_id = max([t["id"] for t in tasks], default=0) + 1

        date = datetime.now().strftime("%H:%M %d.%m.%Y")

        new_task = {
            "id": new_id,
            "description": self.description,
            "status": self.status,
            "created at": date,
            "updated at": date,
        }

        tasks.append(new_task)

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)

        print(f"\n---Task added successfully, task id: {new_id}---\n")
    
    def delete(self, id):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                tasks = json.load(file)
            tasks_Updated = [i for i in tasks if i["id"] != id]

            if len(tasks) != len(tasks_Updated):
                with open(DATA_FILE, "w", encoding="utf-8") as file:
                    json.dump(tasks_Updated, file, indent=4, ensure_ascii=False)
                return (f"\n---Task removed successfully---\n")
            
            else:
                return (f"\n---Task with this ID was not found---\n")
        except (FileNotFoundError, json.JSONDecodeError):
            return "\n---Error: Data file not found.---\n"

    def show(self, status_Filter=None):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            tasks = []
        
        if status_Filter != None:
            tasks = [s for s in tasks if s['status']==status_Filter]

        if not tasks:
            print("\n--- No tasks found ---\n")
            return
        
        col_id = 4
        col_status = 15
        col_date = 18
        full_width = 90
        col_desc = full_width - col_id - col_status - (col_date * 2) - 3

        print("\n" + "=" * full_width)
        headers = [
            "ID".ljust(col_id),
            "STATUS".ljust(col_status),
            "DESCRIPTION".ljust(col_desc),
            "CREATED AT".ljust(col_date),
            "UPDATED AT".ljust(col_date)
        ]
        print(" | ".join(headers))
        print("-" * full_width)


        for t in tasks:
            t_id = str(t.get("id")).ljust(col_id)
            status = f"[{t.get('status')}]".ljust(col_status)
            created = str(t.get("created at")).ljust(col_date)
            updated = str(t.get("updated at")).ljust(col_date)
            
            raw_desc = t.get("description") or ""
            wrapped_desc_list = textwrap.wrap(raw_desc, width=col_desc)
            
            if not wrapped_desc_list:
                wrapped_desc_list = [""]

            first_desc_line = wrapped_desc_list[0].ljust(col_desc)
            row_elements = [t_id, status, first_desc_line, created, updated]
            print(" | ".join(row_elements))

            if len(wrapped_desc_list) > 1:
                for additional_line in wrapped_desc_list[1:]:
                    extra_row = [
                        " " * col_id,
                        " " * col_status,
                        additional_line.ljust(col_desc),
                        " " * col_date,
                        " " * col_date
                    ]
                    print(" | ".join(extra_row))

        print("=" * full_width + "\n")

    def help(self):
        commands = [
             ("1. Add:", "Create a new task in the tracker"),
             ("2. List:", "Show all tasks in the tracker"),
             ("3. Delete:", "Delete a task from the tracker"),
             ("4. Help:", "Show this help message"),
             ("5. Update:", "Update a task in the tracker"),
             ("6. Mark:", "Change status of a task in the tracker. (mark-in-progress, mark-done, mark-todo)")
            ]
        print("\n--- COMMANDS ---")
        for cmd, desc in commands:
            print(f"{cmd.ljust(12)}{desc}")
        print()

    def update(self, id, new_description=None, new_status=None):   
        try:  
            with open(DATA_FILE, "r", encoding="utf-8") as file:
              tasks = json.load(file) 
            for i in tasks:
                if i["id"] == id:
                    if new_description != None:
                        i['description'] = new_description
                    if new_status !=None:
                        i['status'] = new_status
                    date = datetime.now().strftime("%H:%M %d.%m.%Y")
                    i['updated at'] = date
                    print("\n---Task updated successfully---\n")
                    break

            with open(DATA_FILE, "w", encoding="utf-8") as file:
                json.dump(tasks, file, indent=4, ensure_ascii=False)

        except (FileNotFoundError, json.JSONDecodeError):
            return "\n---Error: Data file not found.---\n"
        

