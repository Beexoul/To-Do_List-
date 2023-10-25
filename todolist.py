import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

def clear_list():
    listbox.delete(0, tk.END)

def save_to_file():
    tasks = listbox.get(0, tk.END)
    with open("todo.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_from_file():
    try:
        with open("todo.txt", "r") as file:
            for line in file:
                task = line.strip()
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")

listbox = tk.Listbox(root)
listbox.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
clear_button = tk.Button(root, text="Clear List", command=clear_list)
save_button = tk.Button(root, text="Save to File", command=save_to_file)
load_button = tk.Button(root, text="Load from File", command=load_from_file)

add_button.pack()
remove_button.pack()
clear_button.pack()
save_button.pack()
load_button.pack()

load_from_file()

root.mainloop()
