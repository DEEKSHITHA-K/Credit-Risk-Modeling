import tkinter as tk
import joblib
import sklearn
# Load the model
model = joblib.load("C:\\Users\\deeks\\Downloads\\logistic.joblib")
from tkinter import *
# from PIL import ImageTk, Image
# Define the function to detect credit card fraud

def detect_loans():
    # Get input values from the user
    RevolvingUtilizationOfUnsecuredLines = float(rev_entry.get())
    age = int(age_entry.get())
    NumberOfTime30_59DaysPastDueNotWorse = int(days_entry.get())
    DebtRatio = float(debt_entry.get())
    MonthlyIncome = int(income_entry.get())
    NumberOfOpenCreditLinesAndLoans =int(loans_entry.get())
    NumberRealEstateLoansOrLines = int(realestate_entry.get())
    NumberOfDependents = int(dep_entry.get())

    # Make the prediction using the loaded model
    y_pred = model.predict([[RevolvingUtilizationOfUnsecuredLines, age, NumberOfTime30_59DaysPastDueNotWorse, DebtRatio, MonthlyIncome, NumberOfOpenCreditLinesAndLoans, NumberRealEstateLoansOrLines, NumberOfDependents]])

    # Display the prediction result
    if y_pred == 1:
        result_label.config(text="Loan can't be paid")
    else:
        result_label.config(text="Loan can be paid")

    # Create a tkinter window




window = tk.Tk()
# window = tk.Toplevel()


# window_width = 800
# window_height = 600
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
# x = int((screen_width/2) - (window_width/2))
# y = int((screen_height/2) - (window_height/2))
# window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))



# canvas = Canvas(window, width = 300, height = 300)
# image = ImageTk.PhotoImage(Image.open("C:\\Users\\deeks\\OneDrive\\Documents\\loandefault.png"))
# # image = ImageTk.PhotoImage(Image.open("loandefault.png"))
# canvas.create_image(0,0,anchor = NW, image = image)
# canvas.mainloop()
# canv = Canvas(window, width=80, height=80, bg='white')
# canv.grid(row=2, column=3)

# img = PhotoImage(file="C:\\Users\\deeks\\OneDrive\\Documents\\loandefault.jpg")
# canv.create_image(20,20, anchor=NW, image=img)
window.title("Personal Loan Detection")
# l1 = PhotoImage(file="loandefault.png")
# bg_image = tk.PhotoImage(file="C:\\Users\\deeks\\OneDrive\\Documents\\loandefault.jpg")
# bg_label = tk.Label(window, image=bg_image)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# window.geometry("800x1200")
# Create input fields



# HEIGHT = 1300
# WIDTH = 1500
# canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)

# my_font1=('times', 20, 'bold')
# #window.title("Personal Loan Detection")
# l1 = tk.Label(window,text='Personal Loan Detection',width=20,font=my_font1)  

# l1.grid(row=0,column=0)
# b1 = tk.Button(my_w, text='Browse File', width=10,command = lambda:upload_file(),bg = 'light blue')
# b1.grid(row=2,column=1) 
# t1=tk.Text(window,width=15,height=1)
# t1.grid(row=15,column=1,padx=5)





C = Canvas(window, bg="blue", height=1500, width=1300)
filename = PhotoImage(file = "C:\\Users\\deeks\\OneDrive\\Documents\\loandefault(2).png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# C.pack(fill = BOTH, expand = True)
# C.grid(row=0, column=0, padx=(50,50), pady=(50,50), sticky="ew")
# my_label=Label(window,)
# Create input fields

title_label = tk.Label(window, text="Personal Loan Detection", bg = 'black', fg = 'white', font = 15)
title_label.grid(row=0, column=0,  padx=(50,50), pady=(50,50), sticky="ew")


rev_label = tk.Label(window, text="RevolvingUtilizationOfUnsecuredLines:", bg = 'light blue', fg = 'black', font = 15)
rev_label.grid(row=0, column=0,  padx=(50,50), pady=(50,50), sticky="ew")
rev_entry = tk.Entry(window, bg = 'pink', fg = 'black', font = 15)
rev_entry.grid(row=0, column= 1, padx=(50,50), pady=(50,50), sticky="ew")

age_label = tk.Label(window, text="Age:", bg = 'light blue', fg = 'black', font = 15)
age_label.grid(row=1, column=0, padx=(50,50), pady=(50,50), sticky="ew")
age_entry = tk.Entry(window, bg = 'pink', fg = 'black', font = 15)
age_entry.grid(row=1, column=1,padx=(50,50), pady=(50,50), sticky="ew")

days_label = tk.Label(window, text="NumberOfTime30-59DaysPastDueNotWorse:", bg = 'light blue', fg = 'black', font = 15)
days_label.grid(row=2, column=0, padx=(50,50), pady=(50,50), sticky="ew")
days_entry = tk.Entry(window, bg = 'pink', fg = 'black', font = 15)
days_entry.grid(row=2, column=1, padx=(50,50), pady=(50,50), sticky="ew")

debt_label = tk.Label(window, text="DebtRatio:", bg = 'light blue', fg = 'black', font = 15)
debt_label.grid(row=0, column=2, padx=(50,50), pady=(50,50), sticky="ew")
debt_entry = tk.Entry(window, bg = 'pink', fg = 'black', font = 15)
debt_entry.grid(row=0, column=3, padx=(50,50), pady=(50,50), sticky="ew")

income_label = tk.Label(window, text="Income:", bg = 'light blue', fg = 'black', font = 15)
income_label.grid(row=1, column=2,padx=(50,50), pady=(50,50), sticky="ew")
income_entry = tk.Entry(window, bg = 'pink', fg = 'black', font = 15)
income_entry.grid(row=1, column=3, padx=(50,50), pady=(50,50), sticky="ew")

loans_label = tk.Label(window, text="NumberOfOpenCreditLinesAnwdLoans:", bg = 'light blue', fg = 'black', font = 15)
loans_label.grid(row=2, column=2, padx=(50,50), pady=(50,50), sticky="ew")
loans_entry = tk.Entry(window, bg = 'pink', fg = 'black', font = 15)
loans_entry.grid(row=2, column=3, padx=(50,50), pady=(50,50), sticky="ew")

realestate_label = tk.Label(window, text="NumberRealEstateLoansOrLines:", bg = 'light blue', fg = 'black', font = 15)
realestate_label.grid(row=3, column=0, padx=(50,50), pady=(50,50), sticky="ew")
realestate_entry = tk.Entry(window, bg = 'pink', fg = 'black', font = 15)
realestate_entry.grid(row=3, column=1, padx=(50,50), pady=(50,50), sticky="ew")

dep_label = tk.Label(window, text="NumberOfDependents:", bg = 'light blue', fg = 'black', font = 15)
dep_label.grid(row=3, column=2, padx=(50,50), pady=(50,50), sticky="ew")
dep_entry = tk.Entry(window, bg = 'pink', fg = 'black', font = 15)
dep_entry.grid(row=3, column=3, padx=(50,50), pady=(50,50), sticky="ew")


# Create the button to detect loan status
detect_button = tk.Button(window, text="Detect Loan Status", command=detect_loans, bg = 'light green', fg = 'black', font = 15)
detect_button.grid(row=8, column=0, columnspan=2, padx=(50,50), pady=(50,50), sticky="ew")

# Create the label to display the result
result_label = tk.Label(window, text="", bg = 'orange', fg = 'black', font = 15)
result_label.grid(row=9, column=0, columnspan=2, padx=(50,50), pady=(50,50), sticky="ew")

# Start the main loop of the window
window.mainloop()
#0.766127	45	2	0.802982	9120.0	13	6	2.0