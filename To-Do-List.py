import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.entry_task = tk.Entry(root, width=50,bg="pink",foreground="black")
        self.entry_task.pack()

        self.btn_add_task = tk.Button(root, text="Add Task", width=48, command=self.add_task,fg="black",background="floral white")
        self.btn_add_task.pack()

        self.listbox_tasks = tk.Listbox(root, width=50, height=10,bg="#F0F8FF",fg="black")
        self.listbox_tasks.pack()

        self.scrollbar_tasks = tk.Scrollbar(root)   
        self.scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox_tasks.config(yscrollcommand=self.scrollbar_tasks.set)
        self.scrollbar_tasks.config(command=self.listbox_tasks.yview)

        self.btn_delete_task = tk.Button(root, text="Delete Task", width=48, command=self.delete_task,bg="#7FFFD4",fg="black")
        self.btn_delete_task.pack()

        self.btn_mark_completed = tk.Button(root, text="Mark as Completed", width=48, command=self.mark_as_completed,fg='black',bg="#8A2BE2")
        self.btn_mark_completed.pack()

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.listbox_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_index = self.listbox_tasks.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks.pop(index)
            self.listbox_tasks.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_as_completed(self):
        selected_index = self.listbox_tasks.curselection()
        if selected_index:
            index = selected_index[0]
            completed_task = self.tasks.pop(index)
            self.listbox_tasks.delete(index)
            self.listbox_tasks.insert(tk.END, "Completed: " + completed_task)
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
