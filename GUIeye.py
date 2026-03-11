import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.font as tkFont

# Import new architecture modules
from inference_engine import InferenceEngine
import database

# Initialize Database on app start
database.init_db()

# Dictionary to hold all the Tkinter IntVars dynamically
symptom_vars = {}

def detectDisease():
    # Collect data cleanly from Tkinter IntVars
    user_symptoms = {key: str(var.get()) for key, var in symptom_vars.items()}

    # Run inference engine
    engine = InferenceEngine()
    disease, desc, photo, match_pct = engine.forward_chaining(user_symptoms)
    
    # Save to database
    database.save_diagnosis(user_symptoms, disease if disease else "Unknown")
    
    # Print the explanation log to the terminal
    print("================ CHAIN OF THOUGHT ================")
    print(engine.explanation.get_explanation())
    print("==================================================")

    return disease, desc, photo, match_pct

def openNewWindow():
    newWindow = tk.Toplevel()
    newWindow.title("Diagnosis Results")
    newWindow.geometry("800x650")
    newWindow.config(bg="#F0F4F8") # Soft modern background

    # Clean Header
    header_frame = tk.Frame(newWindow, bg="#2B6CB0", height=80)
    header_frame.pack(fill="x")
    tk.Label(header_frame, text="Diagnostic Results", font=('Helvetica', 20, 'bold'), fg="white", bg="#2B6CB0").pack(pady=20)
    
    name, description, photo, match_pct = detectDisease()
    
    if name == '':
        display_name = 'No Confident Match Found'
        photo = r'.\photo\no.jpg'
        color = "#A0AEC0" # Gray for unknown
    else:
        display_name = f"{name} ({match_pct:.1f}% Match)"
        color = "#E53E3E" # Medical Red for diagnosis

    # Image Canvas
    try:
        img = ImageTk.PhotoImage(Image.open(photo).resize((400, 250)))
        canvas = tk.Canvas(newWindow, width=400, height=250, bg="#FFFFFF", highlightthickness=0)
        canvas.pack(pady=30)
        canvas.create_image(200, 125, anchor=tk.CENTER, image=img)
        canvas.img = img # Keep reference
    except Exception as e:
        print(f"Error loading image: {e}")
    
    # Results Text
    tk.Label(newWindow, text=display_name, font=('Helvetica', 18, 'bold'), fg=color, bg="#F0F4F8").pack(pady=10)
    
    # Description with word wrap so it looks like a clean paragraph
    desc_label = tk.Label(newWindow, text=description, font=('Helvetica', 12), bg="#F0F4F8", fg="#2D3748", wraplength=600, justify="center")
    desc_label.pack(pady=10)

    # Close button
    ttk.Button(newWindow, text="Close", command=newWindow.destroy).pack(pady=20)


# --- Tkinter UI Setup ---
source = tk.Tk()
source.title("Eye Disease Expert System")
source.geometry("1100x800")
source.config(bg="#F0F4F8") # Modern soft background

# Configure TTK Styles for a modern look
style = ttk.Style()
style.theme_use('clam') # 'clam' is generally the cleanest cross-platform base theme
style.configure("TCheckbutton", background="#FFFFFF", font=('Helvetica', 11), foreground="#2D3748", padding=5)
style.configure("TFrame", background="#FFFFFF")
style.configure("Primary.TButton", font=('Helvetica', 14, 'bold'), background="#2B6CB0", foreground="white", padding=10)
style.map("Primary.TButton", background=[('active', '#3182CE')])

# Main Header
header_frame = tk.Frame(source, bg="#2B6CB0", height=100)
header_frame.pack(fill="x")
tk.Label(header_frame, text="Eye Disease Diagnostic System", font=('Helvetica', 24, 'bold'), fg="white", bg="#2B6CB0").pack(pady=15)
tk.Label(header_frame, text="Please check all the symptoms you are currently experiencing.", font=('Helvetica', 12), fg="#E2E8F0", bg="#2B6CB0").pack(pady=0)

# Content Container (White Card)
content_frame = ttk.Frame(source, style="TFrame", padding=30)
content_frame.pack(pady=40, padx=40, fill="both", expand=True)

QUESTIONS = {
    "itching": "Itching and burning in the eyes",
    "blurring": "Blurry or fuzzy vision",
    "redness": "Redness in the eye",
    "night": "Difficulty seeing while driving at night",
    "mucus": "Discharge of sticky mucus",
    "tear": "Excessive tearing in both eyes",
    "yellowing": "Yellowing of colors",
    "headache": "Severe headaches",
    "cough": "Cough, runny nose, or scratchy throat",
    "pain": "Eye pain and swollen eyelids",
    "overstrain": "Eyes constantly feel overstrained",
    "sensitivity": "Increased sensitivity to light",
    "rainbow": "Seeing halos or rainbow circles around lights",
    "double": "Double vision in a single eye",
    "sightedness": "Nearsightedness (can't see far away)",
    "sight": "Sudden loss of sight",
    "nausea": "Constant nausea and vomiting",
    "dilated": "Dilated pupils",
    "eyelid": "Need to partially close eyelids to see clearly",
    "vision": "Sudden decrease in vision"
}

# Dynamically generate checkboxes in a clean 2-column grid
col_frame1 = ttk.Frame(content_frame, style="TFrame")
col_frame1.pack(side="left", fill="both", expand=True, padx=20)

col_frame2 = ttk.Frame(content_frame, style="TFrame")
col_frame2.pack(side="right", fill="both", expand=True, padx=20)

for i, (key, text) in enumerate(QUESTIONS.items()):
    symptom_vars[key] = tk.IntVar() # Defaults to 0 (No)
    
    # Route the first 10 questions to the left column, the rest to the right
    parent = col_frame1 if i < 10 else col_frame2
    
    chk = ttk.Checkbutton(parent, text=text, variable=symptom_vars[key], onvalue=1, offvalue=0, style="TCheckbutton")
    chk.pack(anchor="w", pady=8)

# Submit Button
btn_frame = tk.Frame(source, bg="#F0F4F8")
btn_frame.pack(fill="x", pady=10)
submit_btn = ttk.Button(btn_frame, text="Analyze Symptoms", command=openNewWindow, style="Primary.TButton", cursor="hand2")
submit_btn.pack()

source.mainloop()