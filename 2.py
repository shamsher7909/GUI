import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Retrieve the input values from the entry fields
        L = float(entry_L.get())
        DD = float(entry_DD.get())
        i = float(entry_i.get())
        sigma_v = float(entry_sigma_v.get())
        c = float(entry_c.get())
        phi = float(entry_phi.get())

        # Constants
        G1C2 = -3.48844627213141
        G1C5 = -6.20175817133091
        G2C6 = 5.49893271745485
        G2C5 = -4.29113855828654
        G2C9 = -3.95507070751173
        G2C2 = 3.49594053665271
        G3C0 = -7.14015242255928
        G3C7 = -9.77987402445779
        G4C2 = 7.15933713797418
        G4C8 = -6.18209711691404
        G4C9 = 4.90646790649796
        G4C7 = 3.12698433622949
        G4C0 = -5.74391414499274

        # Calculate the result
        y = ((L + (((phi * i) + (sigma_v + phi)) / 2.0)) + (G1C2 / (((phi / L) + G1C5) / 2.0)))
        y = y + ((G2C6 * ((G2C9 - G2C6) + (G2C2 / DD))) + (((phi + phi) - i) - (G2C5 * c)))
        y = y + ((((L / DD) - (G3C0 * L)) - phi) / (((((G3C7 + G3C7) + phi) / 2.0) + (i - phi)) / 2.0))
        y = y + (((((G4C7 * G4C7) / ((c + G4C0) / 2.0)) + ((L - DD) * i)) / 2.0) - (((G4C2 + G4C8) + (G4C9 * i)) / 2.0))

        # Display the result
        messagebox.showinfo("Result", f"The result is: {y}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Create the GUI window
window = tk.Tk()
window.title("GEP Model GUI")

# Create labels and entry fields for each variable
labels = ["L", "DD", "i", "sigma_v", "c", "phi"]
entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(window, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

    entry = tk.Entry(window)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Create the "Calculate" button
button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.grid(row=len(labels), column=0, columnspan=2, padx=10, pady=10)

# Assign entry fields to variable names
entry_L = entries[0]
entry_DD = entries[1]
entry_i = entries[2]
entry_sigma_v = entries[3]
entry_c = entries[4]
entry_phi = entries[5]

# Start the GUI main loop
window.mainloop()
