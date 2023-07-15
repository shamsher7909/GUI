import tkinter as tk
from math import *


def gepModelquCDV(d):
    G1C8 = 6.87596334712375
    G1C1 = -8.55766644207196
    G2C8 = 1.13006236062298
    G3C9 = -2.18413331200995
    G3C5 = -4.2007986627629
    G3C8 = -8.63726788513352
    G4C2 = 12.7326139438523

    L = 0
    DD = 1
    i = 2
    sigma_v = 3
    c = 4
    phi = 5

    y = 0.0

    y = (d[L] + (d[c] * ((((d[DD] + G1C1) / 2.0) + d[phi]) - ((G1C8 + d[i]) / 2.0))))
    y = y + (d[phi] + ((d[phi] / (((G2C8 + d[phi]) / 2.0) - d[i])) + d[i]))
    y = y + (d[sigma_v] + (((d[c] + d[c]) / ((G3C5 + d[L]) / 2.0)) / (((G3C8 + d[L]) / 2.0) / G3C9)))
    y = y + (d[phi] - ((((d[sigma_v] - G4C2) / (d[i] / G4C2)) + ((d[c] - d[i]) - d[i])) / 2.0))

    return y


def gepModelquCDG(d):
    G1C7 = -4.44392270981758
    G2C4 = 4.7300637836848
    G3C6 = -8.25794298059705
    G3C7 = -11.7200323981344
    G4C3 = 1.62723902248498
    G4C1 = -2.94975191167232
    G5C9 = -4.96871080965606
    G5C3 = -13.5341812043083
    G5C8 = -10.6186525156419

    L = 0
    DD = 1
    i = 2
    sigma_v = 3
    c = 4
    phi = 5

    y = 0.0

    y = (((G1C7 * d[i]) + d[L]) + (((d[phi] + d[phi]) + d[phi]) / (d[sigma_v] / d[phi])))
    y = y + ((d[i] / d[DD]) - (((d[phi] + d[phi]) - d[sigma_v]) / (((d[i] + G2C4) / 2.0) - d[i])))
    y = y + (((((d[sigma_v] + d[L]) / 2.0) + G3C7) + d[L]) / 2.0) / (G3C6 + ((d[c] + d[L]) / 2.0)) + d[sigma_v]) / 2.0)
    y = y + (((((d[L] * d[L]) + d[c]) / d[L]) + (((d[L] + G4C1) / 2.0) * G4C3)) / d[DD])
    y = y + (((((d[L] * G5C3) + (d[phi] * d[i])) / 2.0) / ((G5C8 + d[i]) + d[c])) - (((G5C9 + d[i]) / 2.0) + (G5C3 + d[i])))

    return y


def calculate():
    soil_type = var.get()
    variables = [
        float(entry_L.get()),
        float(entry_DD.get()),
        float(entry_i.get()),
        float(entry_sigma_v.get()),
        float(entry_c.get()),
        float(entry_phi.get())
    ]

    if soil_type == "CDV":
        result = gepModelquCDV(variables)
    elif soil_type == "CDG":
        result = gepModelquCDG(variables)
    else:
        result = "Invalid soil type"

    result_label.config(text="Result: " + str(result))


# Create the GUI
window = tk.Tk()
window.title("Soil Model Calculator")

# Create a popup menu for soil type selection
var = tk.StringVar(window)
var.set("CDV")  # Default soil type

popup_menu = tk.OptionMenu(window, var, "CDV", "CDG")
popup_menu.pack()

# Create input fields for variables
entry_L = tk.Entry(window)
entry_L.pack()
entry_DD = tk.Entry(window)
entry_DD.pack()
entry_i = tk.Entry(window)
entry_i.pack()
entry_sigma_v = tk.Entry(window)
entry_sigma_v.pack()
entry_c = tk.Entry(window)
entry_c.pack()
entry_phi = tk.Entry(window)
entry_phi.pack()

# Create a button to calculate the result
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="Result: ")
result_label.pack()

window.mainloop()
