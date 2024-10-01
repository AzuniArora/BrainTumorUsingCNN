import tkinter as tk
from tkinter import messagebox
import subprocess

def open_prediction_window():
    subprocess.Popen(['python', 'predictionwindow.py'], creationflags=subprocess.CREATE_NO_WINDOW)

def open_graphs_window():
    subprocess.Popen(['python', 'graphwindow.py'], creationflags=subprocess.CREATE_NO_WINDOW)

def create_main_window():
    global root
    root = tk.Tk()
    root.title("Brain Tumor Detection")
    root.geometry("600x500")
    root.configure(bg='#34495e')

    # Widgets
    frame = tk.Frame(root, bg='#34495e')
    frame.pack(pady=20)

    title = tk.Label(frame, text="Brain Tumor Detection", font=("Helvetica", 18, "bold"), bg='#34495e', fg='white')
    title.pack(pady=10)

    graph_button = tk.Button(frame, text="Show Result Graphs", command=open_graphs_window, bg="green", fg="white", font=("Helvetica", 12, "bold"))
    graph_button.pack(pady=10)

    predict_button = tk.Button(frame, text="Check Tumor", command=open_prediction_window, bg="red", fg="white", font=("Helvetica", 12, "bold"))
    predict_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()
