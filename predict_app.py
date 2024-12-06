import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import pandas as pd
import re

# Load the trained model and vectorizer
try:
    rf_model = joblib.load('random_forest_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
except FileNotFoundError:
    raise Exception("Model or Vectorizer file not found. Ensure 'random_forest_model.pkl' and 'tfidf_vectorizer.pkl' exist.")

# Function to preprocess input text
def preprocess_text(title, tags, description):
 
    combined_text = f"{title} {tags} {description}"
    
    def clean_text(text):
        if pd.isnull(text):
            return ""
        
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        
        # Remove HTML tags
        text = re.sub(r'<.*?>', '', text)
        
        # Remove special characters and numbers (keep only letters and spaces)
        text = re.sub(r'[^A-Za-z\s]', '', text)
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    cleaned_text = clean_text(combined_text)
    return cleaned_text


def predict_category():
    # Get user input
    title = title_entry.get()
    tags = tags_entry.get()
    description = description_text.get("1.0", tk.END).strip()
    
    if not title and not tags and not description:
        messagebox.showwarning("Input Error", "Please enter at least one of Title, Tags, or Description.")
        return
    
    # Preprocess the input text
    cleaned_input = preprocess_text(title, tags, description)
    
    # Vectorize the input text
    input_tfidf = vectorizer.transform([cleaned_input])
    
    # Make prediction
    prediction = rf_model.predict(input_tfidf)
    
    # Display the prediction
    predicted_category = prediction[0]
    result_label.config(text=f"Predicted Category: {predicted_category}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Category Predictor")

# Styling
style = ttk.Style()
style.configure('TLabel', font=('Arial', 16))
style.configure('TButton', font=('Arial', 16, 'bold'))
style.configure('TEntry', font=('Arial', 16))
style.configure('TText', font=('Arial', 16))

# Title Label and Entry
title_label = ttk.Label(root, text="Video Title:")
title_label.pack(pady=(20, 5))
title_entry = ttk.Entry(root, width=70)
title_entry.pack()

# Tags Label and Entry
tags_label = ttk.Label(root, text="Video Tags (separated by commas or spaces):")
tags_label.pack(pady=(20, 5))
tags_entry = ttk.Entry(root, width=70)
tags_entry.pack()

# Description Label and Text Box
description_label = ttk.Label(root, text="Video Description:")
description_label.pack(pady=(20, 5))
description_text = tk.Text(root, width=60, height=10, wrap='word')
description_text.pack()

# Predict Button
predict_button = ttk.Button(root, text="Predict Category", command=predict_category)
predict_button.pack(pady=20)

# Result Label
result_label = ttk.Label(root, text="Predicted Category: ", foreground="blue", font=('Arial', 14, 'bold'))
result_label.pack(pady=10)

# Run the application
root.mainloop()
