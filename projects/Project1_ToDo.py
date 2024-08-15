import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        update_task_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Not Done"
        task_listbox.insert(tk.END, f"{idx + 1}. {task['task']} - {status}")

def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks[selected_task_index]["completed"] = True
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to complete.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            tasks[selected_task_index]["task"] = new_task
            update_task_listbox()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a new task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Tkinter setup
root = tk.Tk()
root.title("To-Do List")

# Entry for new task
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
