import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from datetime import datetime
import json

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("TO DO List")
        self.master.geometry("600x400")
        
        self.tasks = []
        
        self.task_label = tk.Label(master, text="Task:")
        self.task_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.task_entry = tk.Entry(master)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.date_label = tk.Label(master, text="Date:")
        self.date_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.date_entry = tk.Entry(master)
        self.date_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.time_label = tk.Label(master, text="Time:")
        self.time_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.time_entry = tk.Entry(master)
        self.time_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.priority_label = tk.Label(master, text="Priority:")
        self.priority_label.grid(row=3, column=0, padx=10, pady=10)
        
        self.priority_combobox = ttk.Combobox(master, values=["Low", "Medium", "High"])
        self.priority_combobox.grid(row=3, column=1, padx=10, pady=10)
        self.priority_combobox.current(0)
        
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=4, columnspan=2, padx=10, pady=10)
        
        self.task_list = tk.Listbox(master, width=50, height=15)
        self.task_list.grid(row=5, columnspan=2, padx=10, pady=10)
        
        self.done_checkbox = tk.Checkbutton(master, text="✔", command=self.mark_task_done)
        self.done_checkbox.grid(row=6, column=0, padx=10, pady=10)
        
        self.cancel_button = tk.Button(master, text="✘", command=self.delete_task)
        self.cancel_button.grid(row=6, column=1, padx=10, pady=10)
        
        self.load_tasks_from_file()  # Load tasks from file when app starts
        

    def add_task(self):
        task = self.task_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        priority = self.priority_combobox.get()
        self.tasks.append({"task": task, "date": date, "time": time, "priority": priority, "done": False})
        self.update_listbox()
        self.clear_entries()
        self.save_tasks_to_file()  # Save tasks to file after adding a new task
        
    def update_listbox(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            status = "✔" if task["done"] else "✘"
            self.task_list.insert(tk.END, f"{task['task']} - {task['date']} {task['time']} - Priority: {task['priority']} - {status}")
        
    def mark_task_done(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["done"] = True
            self.update_listbox()
            self.save_tasks_to_file()  # Save tasks to file after marking a task as done
        
    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_listbox()
            self.save_tasks_to_file()  # Save tasks to file after deleting a task
        
    def clear_entries(self):
        self.task_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        
    def save_tasks_to_file(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
        
    def load_tasks_from_file(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
                self.update_listbox()
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
