import tkinter as tk

def format_number(number):
    # Remove any non-digit characters from the number
    digits = ''.join(filter(str.isdigit, number))
    
    # Format the number in the pattern "(xxx) xxx - xxxx"
    formatted_number = "({}) {} - {}".format(digits[:3], digits[3:6], digits[6:])

    return formatted_number

def slider_changed(event):
    value = scale.get()
    formatted_value = format_number(str(value))
    formatted_label.config(text=formatted_value)

window = tk.Tk()

# Set the range from 905 xxx xxxx to 905 999 9999
scale = tk.Scale(window, from_=9050000000, to=9059999999, resolution=1, orient=tk.HORIZONTAL, showvalue=0, length=300)
scale.pack()

formatted_label = tk.Label(window, text="")
formatted_label.pack()

scale.bind("<B1-Motion>", slider_changed)

window.mainloop()
