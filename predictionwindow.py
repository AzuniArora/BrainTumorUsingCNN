import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2
import webbrowser
from tensorflow.keras.models import load_model

# Load the pre-trained model
model = load_model(r'C:\Users\DELL\Desktop\Brain Tumor Project\brain_tumor_detection_model.h5')

# Labels
labels = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']

# Professional suggestions for healthy individuals and those with tumors
suggestions = {
    'no_tumor': """You don't have a tumor. Here are some tips to maintain a healthy brain:
1. Eat a balanced diet rich in fruits, vegetables, and omega-3 fatty acids.
2. Exercise regularly to improve blood flow to the brain.
3. Stay mentally active with puzzles, reading, and learning new skills.
4. Get regular medical check-ups.
For more information, visit: [Healthy Brain Tips]""",
   
    'glioma_tumor': """A glioma tumor has been detected. Please consult a healthcare professional for a detailed diagnosis and treatment plan. Here are some general steps:
1. Schedule an appointment with a neurologist or oncologist.
2. Follow the prescribed treatment plan, which may include surgery, radiation, or chemotherapy.
3. Maintain a healthy diet and stay hydrated.
4. Seek support from a mental health professional if needed.
For more information, visit: [Glioma Tumors]""",

    'meningioma_tumor': """A meningioma tumor has been detected. Please consult a healthcare professional for a detailed diagnosis and treatment plan. Here are some general steps:
1. Schedule an appointment with a neurologist or oncologist.
2. Follow the prescribed treatment plan, which may include surgery, radiation, or observation.
3. Maintain a healthy diet and stay hydrated.
4. Seek support from a mental health professional if needed.
For more information, visit: [Meningioma Tumors]""",

    'pituitary_tumor': """A pituitary tumor has been detected. Please consult a healthcare professional for a detailed diagnosis and treatment plan. Here are some general steps:
1. Schedule an appointment with an endocrinologist or neurosurgeon.
2. Follow the prescribed treatment plan, which may include medication, surgery, or radiation.
3. Maintain a healthy diet and stay hydrated.
4. Seek support from a mental health professional if needed.
For more information, visit: [Pituitary Tumors]"""
}

# Function to preprocess the input image
def preprocess_image(image_path, target_size=(150, 150)):
    image = cv2.imread(image_path)
    image = cv2.resize(image, target_size)
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Function to make predictions
def predict_image(image_path, model):
    image = preprocess_image(image_path, (150, 150))
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction, axis=1)[0]
    predicted_label = labels[predicted_class]
    return predicted_label, prediction

# Function to load an image file and show prediction
def load_image():
    img_path = filedialog.askopenfilename()
    if img_path:
        predicted_label, prediction = predict_image(img_path, model)
        confidence = np.max(prediction)
        result_text.set(f"Prediction: {predicted_label}\nConfidence: {confidence:.2f}")
        display_image(img_path)
        show_suggestions(predicted_label)

# Function to display the selected image
def display_image(img_path):
    img = Image.open(img_path)
    img = img.resize((150, 150), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img

def show_suggestions(predicted_label):
    suggestion_text = suggestions[predicted_label]
    suggestion_textbox.config(state=tk.NORMAL)
    suggestion_textbox.delete(1.0, tk.END)
    suggestion_textbox.insert(tk.END, suggestion_text)

    # Adding clickable links
    add_clickable_links(suggestion_textbox)

    suggestion_textbox.config(state=tk.DISABLED)

def add_clickable_links(text_widget):
    link_data = {
        "Healthy Brain Tips": "https://www.mayoclinic.org/healthy-lifestyle/healthy-aging/in-depth/brain-health-tips/art-20555198",
        "Glioma Tumors": "https://www.medicalnewstoday.com/articles/glioma#types",
        "Meningioma Tumors": "https://www.mayoclinic.org/diseases-conditions/meningioma/symptoms-causes/syc-20355643",
        "Pituitary Tumors": "https://www.cancer.org/cancer/pituitary-tumors.html"
    }
   
    for label, url in link_data.items():
        start_idx = text_widget.search(label, "1.0", tk.END)
        if start_idx:
            end_idx = f"{start_idx}+{len(label)}c"
            text_widget.tag_add(label, start_idx, end_idx)
            text_widget.tag_config(label, foreground="blue", underline=True)
            text_widget.tag_bind(label, "<Button-1>", lambda e, url=url: open_url(url))

def open_url(url):
    webbrowser.open_new(url)

def create_prediction_window():
    global image_label
    global result_text
    global suggestion_textbox

    pred_window = tk.Tk()
    pred_window.title("Brain Tumor Prediction")
    pred_window.geometry("800x600")
    pred_window.configure(bg='#2c3e50')

    title = tk.Label(pred_window, text="Brain Tumor Prediction", font=("Helvetica", 16, "bold"), bg='#2c3e50', fg='white')
    title.pack(pady=10)

    image_label = tk.Label(pred_window, text="No image selected", bg='#2c3e50', fg='white')
    image_label.pack(pady=20)

    load_button = tk.Button(pred_window, text="Choose Photo", command=load_image, bg="blue", fg="white", font=("Helvetica", 12, "bold"))
    load_button.pack(pady=10)

    result_text = tk.StringVar()
    result_label = tk.Label(pred_window, textvariable=result_text, font=('Helvetica', 14), bg='#2c3e50', fg='white')
    result_label.pack(pady=20)

    suggestion_textbox = tk.Text(pred_window, font=('Helvetica', 12), bg='#2c3e50', fg='white', wrap=tk.WORD, height=10, width=90, borderwidth=0, highlightthickness=0)
    suggestion_textbox.pack(pady=20)
    suggestion_textbox.config(state=tk.DISABLED)

    pred_window.mainloop()

if __name__ == "__main__":
    create_prediction_window()
