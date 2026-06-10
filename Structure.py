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
            new_id = max(tasks["id"]) + 1
            task = { "id": new_id,
                     "description": self.description,
                     "status": self.status,
                     "created at": datetime.now().isoformat(),
                     "updated at": datetime.now().isoformat(),
                    }
            tasks = tasks.append(task)
            tasks = json.dumps(tasks, indent=4)
        except FileNotFoundError:
            task = { "id": 1,
                     "description": self.description,
                     "status": self.status,
                     "created at": datetime.now().isoformat(),
                     "updated at": datetime.now().isoformat(),
                    }
            tasks = json.dumps(task, indent=4)

            