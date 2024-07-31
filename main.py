from tkinter import *

window = Tk()
window.title("BMI Calculate")
window.minsize(width=250, height=150)
window.config(padx=30,pady=30)

my_Label = Label(text="Enter Your Weight (kg)")
my_Label.pack()

my_entry = Entry()
my_entry.pack()

my_label2 = Label(text="Enter Your Height (cm)")
my_label2.pack()

my_entry2 = Entry()
my_entry2.pack()

bmi = 0

def calculateBMI():
    weight = my_entry.get()
    height = my_entry2.get()

    if weight == "" or height == "":
        resultLabel.config(text="Enter both and height!")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = resultText(bmi)
            resultLabel.config(text=result_string)
        except:
            resultLabel.config(text="Enter valid values!!")

def resultText(bmi):
    resultString = f"Your bmi is {round(bmi,2)}. You are "
    if bmi < 16:
        resultString += "Severely Underweight"
    elif 16 < bmi < 18.4:
        resultString +="Underweight"
    elif 18.5 < bmi < 24.9:
        resultString +="Normal"
    elif 25 < bmi < 29.9:
        resultString +="Overweight"
    elif 30 < bmi < 34.9:
        resultString +="Moderately Obese"
    elif 35 < bmi < 39.9:
        resultString +="Severaly Obese"
    elif 40 < bmi:
        resultString +="Obese"
    return resultString

my_button = Button(text="Calculate", command=calculateBMI)
my_button.pack()

resultLabel = Label()
resultLabel.pack()

window.mainloop()

# Weight / height * height
