from tkinter import *
from tkinter import messagebox
import pickle  # Add this import for saving and loading data

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
        save_tasks()  # Save tasks when a new one is added
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    try:
        selected_task_index = lb.curselection()[0]
        lb.delete(selected_task_index)
        save_tasks()  # Save tasks after deleting one
    except IndexError:
        messagebox.showwarning("warning", "Please select a task to delete.")

def save_tasks():
    tasks = lb.get(0, END)  # Get all tasks in the listbox
    with open("tasks.dat", "wb") as file:
        pickle.dump(tasks, file)

def load_tasks():
    try:
        with open("tasks.dat", "rb") as file:
            tasks = pickle.load(file)
            for task in tasks:
                lb.insert(END, task)
    except FileNotFoundError:
        pass

ws = Tk()
ws.geometry('500x450+500+200')
ws.title('To-Do List')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)



def on_enter(event):
    newTask()

frame = Frame(ws)
frame.pack(pady=10)
ws.bind("<Return>", on_enter) 
lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
)
my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

# Load saved tasks when the application starts
load_tasks()

ws.mainloop()
