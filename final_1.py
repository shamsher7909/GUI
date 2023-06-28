from math import *
import tkinter as tk

from math import *

def gepModelqu(d):

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

    L = 0
    DD = 1
    i = 2
    sigma_v = 3
    c = 4
    phi = 5

    y = 0.0

    y = ((d[L]+(((d[phi]-d[i])+(d[sigma_v]+d[phi]))/2.0))+(G1C2/(((d[phi]/d[L])+G1C5)/2.0)))
    y = y + ((G2C6*((G2C9-G2C6)+(G2C2/d[DD])))+(((d[phi]+d[phi])-d[i])-(G2C5*d[c])))
    y = y + ((((d[L]/d[DD])-(G3C0*d[L]))-d[phi])/(((((G3C7+G3C7)+d[phi])/2.0)+(d[i]-d[phi]))/2.0))
    y = y + (((((G4C7*G4C7)/((d[c]+G4C0)/2.0))+((d[L]-d[DD])*d[i]))/2.0)-(((G4C2+G4C8)+(G4C9*d[i]))/2.0))

    return y

def calculate():
    inputs = [float(entry.get()) for entry in input_entries]
    result = gepModelqu(inputs)
    result_label.config(text=f"Result: {result}")

# Create the main window
window = tk.Tk()
window.title("GUI for gepModelqu")

# Add a text label at the top
header_label = tk.Label(window, text="Reference: Prediction of grouted soil nail pullout bond strength using gene expression programming by Myoung-Soo Won, Shamsher Sadiq , Sung-Uk Seo and Jun-Yong Park")
header_label.pack(padx=10, pady=10)

# Create input labels and entry fields
#input_labels = ['Length (m)', 'Drill hole diameter (m)', 'Angle of inclination (degree)', 'Overburden stress (kPa)', 'Cohesion (kPa)', 'Friction Angle (degree)']
input_labels = ['Length (m) (3-27)', 'Drill hole diameter (m) (0.1, 0.12 & 0.15)', 'Angle of inclination (degree) (5-45)', 'Overburden stress (kPa) (35-560)', 'Cohesion (kPa) (0-15)', 'Friction Angle (degree) (31-45)']
input_entries = []

for i, label in enumerate(input_labels):
    label = tk.Label(window, text=label)
    label.grid(row=i, column=0, padx=10, pady=10)
    entry = tk.Entry(window)
    entry.grid(row=i, column=1, padx=10, pady=10)
    input_entries.append(entry)

# Create a calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=len(input_labels), column=0, columnspan=2, padx=10, pady=10)

# Create a label to display the result
result_label = tk.Label(window, text="Pullout Bond Strength (kPa) ")
result_label.grid(row=len(input_labels)+1, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI main loop
window.mainloop()
