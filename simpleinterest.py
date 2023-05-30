from tkinter import *
window=Tk()

# add widgets here


window.title('Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')


app_label=Label(window, text="INTEREST CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principal_label = Label(window,text="Enter principal amount")
principal_label.place(x=20,y=90)

rate_label=Label(window, text="Rate of Interest", fg = "black", bg = "grey", font=("Calibri", 12))
rate_label.place(x=20, y=140)

rate=Entry(window, text="", bd=2, width=15)
rate.place(x=200, y=142)

time_label=Label(window, text="Time in Years", fg = "black", bg = "grey", font=("Calibri", 12))
time_label.place(x=20, y=185)

time=Entry(window, text="", bd=2, width=15)
time.place(x=200, y=187)

calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "grey",bd=4,command=calculate_interest)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result", bg = "grey", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

message=Label(result_frame,text="Your result will be displayed here", bg = "grey", font=("Calibri", 12), width=55)
message.place(x=20,y=20)
message.pack()

window.mainloop()

