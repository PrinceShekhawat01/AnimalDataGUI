import tkinter as tk
from tkinter import messagebox, ttk
import requests

# Function to fetch and display animal details
def fetch_animal_details():
    animal_name = animal_entry.get().strip().lower()
    if not animal_name:
        messagebox.showerror("Input Error", "Please enter an animal name")
        return
    
    url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    headers = {'X-Api-Key': 'AkaK+a3jYNQ4uRj2cbW3tA==nuzOXJvlMFU5Kgx7'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            animal = data[0]
            details = f"Name: {animal.get('name', 'N/A')}\n" \
                      f"Taxonomy: {animal.get('taxonomy', 'N/A')}\n" \
                      f"Locations: {', '.join(animal.get('locations', []))}\n" \
                      f"Lifespan: {animal.get('lifespan', 'N/A')}\n" \
                      f"Conservation Status: {animal.get('conservation_status', 'N/A')}"
            result_text.set(details)
        else:
            result_text.set("No details found for the given animal.")
    else:
        messagebox.showerror("API Error", f"Failed to fetch data: {response.status_code}")

# Set up the main application window
root = tk.Tk()
root.title("Animal Details Finder")
root.geometry("500x400")
root.resizable(False, False)

# Frame for the main content
frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

# Input field for animal name
ttk.Label(frame, text="Enter animal name:", font=("Helvetica", 12)).pack(pady=10)
animal_entry = ttk.Entry(frame, font=("Helvetica", 12))
animal_entry.pack(pady=5, fill=tk.X)

# Button to fetch animal details
fetch_button = ttk.Button(frame, text="Fetch Details", command=fetch_animal_details)
fetch_button.pack(pady=10)

# Result display
result_text = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result_text, justify=tk.LEFT, font=("Helvetica", 10), relief="sunken", padding="10")
result_label.pack(pady=10, fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
root.mainloop()
