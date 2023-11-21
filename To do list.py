import tkinter as tk
from tkinter import ttk

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def update_task(self, task_id, title=None, completed=None):
        for task in self.tasks:
            if task.title == title:
                if completed is not None:
                    task.completed = completed

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.title == task_id:
                self.tasks.remove(task)
                break

    def display_tasks(self):
        for task in self.tasks:
            print(f"Task: {task.title}, Status: {'Completed' if task.completed else 'Not Completed'}")

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

class TaskApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List")
        self.geometry("300x400")

        self.task_list = ToDoList()

        self.create_widgets()

    def create_widgets(self):
        self.title_label = ttk.Label(self, text="Task Title:")
        self.title_label.grid(column=0, row=0, padx=10, pady=10, sticky='w')

        self.title_entry = ttk.Entry(self, width=30)
        self.title_entry.grid(column=1, row=0, padx=10, pady=10)

        self.add_button = ttk.Button(self, text="Add Task", command=self.add_task)
        self.add_button.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

        self.tasks_label = ttk.Label(self, text="Tasks:")
        self.tasks_label.grid(column=0, row=2, padx=10, pady=10, sticky='w')

        self.tasks_listbox = tk.Listbox(self, width=30)
        self.tasks_listbox.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        self.delete_button = ttk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

    def add_task(self):
        title = self.title_entry.get()
        self.task_list.add_task(title)
        self.tasks_listbox.insert(tk.END, title)
        self.title_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task = self.tasks_listbox.get(tk.ACTIVE)
        self.task_list.delete_task(selected_task)
        self.tasks_listbox.delete(tk.ACTIVE)

if __name__ == "__main__":
    app = TaskApp()
    app.mainloop()