import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Addition Calculator")

optionLabel = tk.Label(
    window, text="Enter '1' to literally add the numbers together or '2' for real addition:")
optionLabel.pack()

optionEntry = tk.Entry(window)
optionEntry.pack()

# meme option: combine the numbers... literally

# function for concatenating numbers together

def memeAddition():
    # Get the integer inputs from the Entry fields
    int1 = int(entry1.get())
    int2 = int(entry2.get())

    # Convert the integers to strings
    int1Str = str(int1)
    int2Str = str(int2)

    # Concatenate the strings
    strResult = int1Str + int2Str

    # Update the label with the result
    memeLabel.config(text="Your result is: " + strResult)

# OR user can actually add the results together

def realAddition():
    # Get the integer input from the Entry fields
    int1 = int(entry3.get())
    int2 = int(entry4.get())

    # Calculate the sum
    intSum = int1 + int2

    # Update the label with the result
    additionResult.config(text="Your result is: " + str(intSum))

# user can go back to the main option selection page
def resetOption():

    optionLabel.pack()
    optionEntry.pack()
    submitButton.pack()

# Function to handle the submission of the option
def optionSelection():
    global entry1, entry2, entry3, entry4, additionResult, memeLabel 
    option = optionEntry.get()

    if option == "1":  # do memeAddition

        # hide previous labels 
        optionLabel.pack_forget()
        optionEntry.pack_forget()
        submitButton.pack_forget()

        # Create the first integer label and Entry field
        label1 = tk.Label(window, text="Enter a number:")
        label1.pack()

        entry1 = tk.Entry(window)
        entry1.pack()

        # Create the second integer label and Entry field
        label2 = tk.Label(window, text="Enter another number:")
        label2.pack()

        entry2 = tk.Entry(window)
        entry2.pack()

        # Create the Concatenate button
        concatenateButton = tk.Button(window, text="Add", command=memeAddition)
        concatenateButton.pack()

        resetButton = tk.Button(window, text="Reset", command=resetOption)
        resetButton.pack() 

        # Create the result label
        memeLabel = tk.Label(window, text="Your result is:")
        memeLabel.pack()

    elif option == "2":  # do realAddition 

        # hide the previous labels 
        optionLabel.pack_forget()
        optionEntry.pack_forget()
        submitButton.pack_forget()

        label3 = tk.Label(window, text="Enter a number")
        label3.pack()

        entry3 = tk.Entry(window)
        entry3.pack()

        label4 = tk.Label(window, text="Enter another number")
        label4.pack()

        entry4 = tk.Entry(window)
        entry4.pack()

        # Create the Add Together button
        addTogether = tk.Button(window, text="Add", command=realAddition)
        addTogether.pack()

        # Create the result label
        additionResult = tk.Label(window, text="Your result is: ")
        additionResult.pack()

        # Create the reset button 
        resetButton = tk.Button(window, text="Reset", command=resetOption) 
        resetButton.pack() 

submitButton = tk.Button(window, text="Submit", command=optionSelection)
submitButton.pack()

# Start the main GUI loop
window.mainloop()
