**-INSTALLATION-**

*1*
```bash
git clone https://github.com/ZKRV02/Task-Tracker.git
```
*2*
```bash
cd Task-Tracker
```
*3*
```bash
pip install .
```
or

*( `pip install -e .` if you want to edit the code)*


**-USAGE-**

*1. Add task*
```bash
task-cli add task
```
**2 Updating task**
```bash
task-cli update 1 "Updated task"
```
**3 Updating task status**
```bash
task-cli mark-done 1
```
**4 Deleting task**
```bash
task-cli delete 1
```
**5 Listing all tasks**
```bash
task-cli list
```
or list by filter
```bash
task-cli list (done, in-progress, todo)
```

https://roadmap.sh/projects/task-tracker