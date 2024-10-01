import tkinter as tk
from PIL import Image, ImageTk

def create_graphs_window():
    graph_window = tk.Tk()
    graph_window.title("Training and Validation Graphs")
    graph_window.geometry("800x600")
    graph_window.resizable(0,0)
    graph_window.configure(bg='#2c3e50')

    title = tk.Label(graph_window, text="Training and Validation Graphs", font=("Helvetica", 16, "bold"), bg='#2c3e50', fg='white')
    title.pack(pady=10)

    # Create a canvas and a scrollbar
    canvas = tk.Canvas(graph_window, bg='#2c3e50')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(graph_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = tk.Frame(canvas, bg='#2c3e50')
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Display the confusion matrix
    confusion_matrix_img = Image.open(r'C:\Users\DELL\Desktop\Brain Tumor Project\confusionmatrix.png')
    confusion_matrix_img = confusion_matrix_img.resize((350, 250), Image.LANCZOS)
    confusion_matrix_photo = ImageTk.PhotoImage(confusion_matrix_img)
    confusion_matrix_label = tk.Label(scrollable_frame, image=confusion_matrix_photo, bg='#2c3e50')
    confusion_matrix_label.image = confusion_matrix_photo
    confusion_matrix_label.grid(row=0, column=0, padx=10, pady=10)

    confusion_matrix_title = tk.Label(scrollable_frame, text="Confusion Matrix", font=("Helvetica", 14, "bold"), bg='#2c3e50', fg='white')
    confusion_matrix_title.grid(row=1, column=0, padx=10, pady=5)

    # Display the recall precision result
    recall_precision_img = Image.open(r'C:\Users\DELL\Desktop\Brain Tumor Project\recallprecision.png')
    recall_precision_img = recall_precision_img.resize((350, 250), Image.LANCZOS)
    recall_precision_photo = ImageTk.PhotoImage(recall_precision_img)
    recall_precision_label = tk.Label(scrollable_frame, image=recall_precision_photo, bg='#2c3e50')
    recall_precision_label.image = recall_precision_photo
    recall_precision_label.grid(row=0, column=1, padx=10, pady=10)

    recall_precision_title = tk.Label(scrollable_frame, text="Classification Report", font=("Helvetica", 14, "bold"), bg='#2c3e50', fg='white')
    recall_precision_title.grid(row=1, column=1, padx=10, pady=5)

    # Display the accuracy and loss graph
    accuracy_loss_img = Image.open(r'C:\Users\DELL\Desktop\Brain Tumor Project\trainingandvalidationaccuracy.png')
    accuracy_loss_img = accuracy_loss_img.resize((700, 400), Image.LANCZOS)
    accuracy_loss_photo = ImageTk.PhotoImage(accuracy_loss_img)
    accuracy_loss_label = tk.Label(scrollable_frame, image=accuracy_loss_photo, bg='#2c3e50')
    accuracy_loss_label.image = accuracy_loss_photo
    accuracy_loss_label.grid(row=2, column=0, columnspan=2, pady=20)

    accuracy_loss_title = tk.Label(scrollable_frame, text="Training and Validation Accuracy and Loss Analysis", font=("Helvetica", 14, "bold"), bg='#2c3e50', fg='white')
    accuracy_loss_title.grid(row=3, column=0, columnspan=2, pady=5)

    graph_window.mainloop()

if __name__ == "__main__":
    create_graphs_window()
