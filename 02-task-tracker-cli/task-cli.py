import json
import sys
from pathlib import Path
from datetime import datetime

now = datetime.now()
target_dir = Path(".")
file_path = target_dir / "tasks.json"

if file_path.exists():
    with file_path.open("r", encoding="UTF-8") as file:
        try:
            my_tasks = json.load(file)
        except json.JSONDecodeError:
            my_tasks = []

else:
    my_tasks = []

todo_list = []
progress_list = []
done_list = []

def update_lists(my_tasks, todo_list, progress_list, done_list):
    for task in my_tasks:
        if task["status"] == "todo":
            todo_list.append(task)
        elif task["status"] == "in-progress":
            progress_list.append(task)
        elif task["status"] == "done":
            done_list.append(task)

    return my_tasks, todo_list, progress_list, done_list

def indexes(my_tasks):
    indexes = []
    for task in my_tasks:
        indexes.append(task["id"])
    return indexes

def get_index(id, indexes):
    for idx in indexes:
        if idx == id:
            return indexes.index(idx)
        else:
           continue

def add(task, now, my_tasks):
    if my_tasks == []:
        id = 1
    else: 
        id = my_tasks[-1]["id"] + 1

    new_task = {
        "id": id,
        "description": task,
        "status": "todo",
        "createdAt": str(now),
        "updatedAt": str(now)
    }

    my_tasks.append(new_task)
    indexes(my_tasks)

    print(f"Task added successfully (ID: {id})")


def update(id, description, my_tasks):
    try:

        index = get_index(id, indexes(my_tasks))
        my_tasks[index]["description"] = description
        print(f"Task updated sucessfully (ID: {id})")
    except IndexError:
        if not my_tasks == []:
            print("Non-existent ID")
        else:
            create = input("Empty tasks list. Create a task? (y/n): ")
            if create == 'y':
                add(description, now, my_tasks)
            else:
                print("Failed to update")

def delete(id, my_tasks):
    try:
        index = get_index(id, indexes(my_tasks))
        del my_tasks[index]
        print(f"Task deleted sucessfully (ID: {id})")
        indexes(my_tasks)
    except IndexError:
        if not my_tasks == []:
            print("Non-existent ID")
        else:
            print("Empty tasks list")

def change_status(id, status, my_tasks):
    try:
        status = status[1:]
        new_status = "-".join(status)
        index = id - 1
        my_tasks[index]["status"] = new_status
        print(f"{new_status.title()}: {my_tasks[index]["description"]} (ID: {id})")
    except IndexError:
        if not my_tasks == []:
            print("Non-existent ID")
        else:
            print("Empty tasks list")

def _list(status, my_tasks, todo_list, progress_list, done_list):
    update_lists(my_tasks, todo_list, progress_list, done_list)

    match status:
        case "":
            print("\nAll Tasks:")
            for task in my_tasks:
                print(f" --> {task["description"]}, {task["status"]}")
        case "todo":
            print("\nTODO Tasks:")
            for task in todo_list:
                print(f" --> {task["description"]}")
        case "in-progress":
            print("\nIn-progress Tasks:")
            for task in progress_list:
                print(f" --> {task["description"]}")
        case "done":
            print("\nDone Tasks:")
            for task in done_list:
                print(f" --> {task["description"]}")


if len(sys.argv) > 1:
    command = sys.argv[1]

    match command:
        case "add":
            task = sys.argv[2]
            add(task, now, my_tasks)
        case "update":
            task_id = int(sys.argv[2])
            description = sys.argv[3]
            update(task_id, description, my_tasks)
        case "delete":
            task_id = int(sys.argv[2])
            delete(task_id, my_tasks)
        case "mark-in-progress":
            task_id = int(sys.argv[2])
            status = sys.argv[1].split("-")
            change_status(task_id, status, my_tasks)
        case "mark-done":
            task_id = int(sys.argv[2])
            status = sys.argv[1].split("-")
            change_status(task_id, status, my_tasks)
        case "list":    
            try:
                if sys.argv[2] == "done":
                    status = sys.argv[2]
                    _list(status, my_tasks, todo_list, progress_list, done_list)
                elif sys.argv[2] == "todo":
                    status = sys.argv[2]
                    _list(status, my_tasks, todo_list, progress_list, done_list)
                elif sys.argv[2] == "in-progress":
                    status = sys.argv[2]
                    _list(status, my_tasks, todo_list, progress_list, done_list)
            except IndexError:
                status = ""
                _list(status, my_tasks, todo_list, progress_list, done_list)

        case _:
            print("Invalid operation")

else: 
    print("Please, enter a valid action")



with file_path.open("w", encoding="utf-8") as file:
    json.dump(my_tasks, file, indent=4)