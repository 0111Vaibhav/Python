import json
import os

file_Name = "todo.json"

def load_tasks():
    if not os.path.exists(file_Name):
        with open(file_Name, 'w') as f:
            json.dump([], f)
        return []
    else:
        with open(file_Name, 'r') as f:
            return json.load(f)

def save_tasks(tasks):
    with open(file_Name, 'w') as f:
        json.dump(tasks, f)
        
def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    
    print("---Your Tasks---")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task['status'] == 'done' else "❌"
        print(f"{i}. {status} {task['text']}")
    print("---------------")

def add_task(tasks):
    
    task_text = input("Enter Your Task: ")
    
    tasks.append({
        "text" : task_text,
        "status" : "pending"
    })
    
    save_tasks(tasks)
    print(f"Task '{task_text}' added successfully.")

def delete_task(tasks):
    
    show_tasks(tasks)
    
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_tasks = tasks.pop(task_num -1)
            save_tasks(tasks)
            print(f"Task: {removed_tasks['text']} deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid Input. Please enter a valid number.")

def mark_task_done(tasks):
    
    show_tasks(tasks)
    
    if not tasks:
        return
    
    try: 
        task_num = int(input("Enter the task number to mark as done: "))
        if 1<= task_num <= len(tasks):
            tasks[task_num-1]["status"] = 'done'
            save_tasks(tasks)
            print(f"Task: {tasks[task_num-1]['text']} marked as done.")
        else:
            print("Invalid task number.")
    except:
        print("Invalid Input. Please enter a valid number.")

def main():
    tasks=load_tasks()
    while True:
        print("\n---Todo List Menu---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Marks Task as Done")
        print("5. Exit")
        try:
            choice = int(input("Enter Your Choice (1-5): "))
            if choice == 1:
                show_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                delete_task(tasks)
            elif choice == 4:
                mark_task_done(tasks)
            elif choice == 5:
                break
            
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

        
if __name__ == "__main__":
    main()
    
