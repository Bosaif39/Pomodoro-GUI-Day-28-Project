from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50,pady=50)

# is equal to label
my_label= Label(font=("Arial",14,"bold"))
my_label.grid(column=0,row=1)
my_label.config(text="is equal to")


# Miles label
my_label2= Label(font=("Arial",14,"bold"))
my_label2.grid(column=3,row=0)
my_label2.config(text="Miles")


# Km label
my_label3= Label(font=("Arial",14,"bold"))
my_label3.grid(column=3,row=1)
my_label3.config(text="Km")


# Results
Results= Label(font=("Arial",14,"bold"))
Results.grid(column=1,row=1)
Results.config(text=0,padx=50,pady=50)

# Function to convert miles to kilometers
def calculate_miles():
    miles = float(inputEntery.get())
    kilometers = miles * 1.60934
    kilometers = round(kilometers, 2)
    Results.config(text=kilometers)


button = Button(text="Calculate", command=calculate_miles)
button.grid(column=1,row=3)


inputEntery = Entry(width=10)
inputEntery.grid(column=1, row=0)


window.mainloop()
