import json
from datetime import datetime
class Task:
    def __init__(self, id, description, status="todo"):
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

        now = datetime.now().isoformat()

        new_task = {
            "id": new_id,
            "description": self.description,
            "status": self.status,
            "created at": now,
            "updated at": now,
        }

        tasks.append(new_task)

        with open("data.json", "w") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)

        print(f"Task added succesfully, task id:{new_id}")
