import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.refresh_button = tk.Button(root, text="Refresh", command=self.refresh_tasks)
        self.refresh_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack(pady=5)

    def add_task(self):
        task_title = self.task_entry.get()
        if task_title:
            new_task = {'title': task_title, 'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'completed': False}
            self.tasks.append(new_task)
            self.task_listbox.insert(tk.END, f"{new_task['title']} - {new_task['date']}")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.tasks[selected_index[0]]
            if not selected_task['completed']:
                selected_task['completed'] = True
                messagebox.showinfo("Task Completed", f"{selected_task['title']} marked as completed.")
                self.refresh_tasks()
            else:
                messagebox.showwarning("Warning", "Task is already completed.")
        else:
            messagebox.showwarning("Warning", "Please select a task.")

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task['completed'] else " "
            self.task_listbox.insert(tk.END, f"{status} {task['title']} - {task['date']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
