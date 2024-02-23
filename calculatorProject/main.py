import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, tk.END)
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "ERROR")
        pass

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, tk.END)

root = tk.Tk()
root.geometry("330x420")
root.title("Calculator")
root.configure(background="#24689F")

frame = tk.Frame(root, bg="#24689F")
frame.place(relx=0.5, rely=0.5, anchor="center")

text_result = tk.Text(frame, height=2, width=16, font=("Bahnschrift", 24))
text_result.grid(columnspan=5, pady=(0, 30))
# Define common parameters for buttons
button_params = {"width": 5, "font": ("Bahnschrift", 14)}

# Create buttons with space between them
btn_9 = tk.Button(frame, text="9", command=lambda: add_to_calculation(9), **button_params)
btn_9.grid(row=3, column=2, padx=5, pady=5)

btn_8 = tk.Button(frame, text="8", command=lambda: add_to_calculation(8), **button_params)
btn_8.grid(row=3, column=1, padx=5, pady=5)

btn_7 = tk.Button(frame, text="7", command=lambda: add_to_calculation(7), **button_params)
btn_7.grid(row=3, column=0, padx=5, pady=5)

btn_6 = tk.Button(frame, text="6", command=lambda: add_to_calculation(6), **button_params)
btn_6.grid(row=4, column=2, padx=5, pady=5)

btn_5 = tk.Button(frame, text="5", command=lambda:add_to_calculation(5), **button_params)
btn_5.grid(row=4, column=1, padx=5, pady=5)

btn_4 = tk.Button(frame, text="4", command=lambda: add_to_calculation(4), **button_params)
btn_4.grid(row=4, column=0, padx=5, pady=5)

btn_3 = tk.Button(frame, text="3", command=lambda:add_to_calculation(3), **button_params)
btn_3.grid(row=5, column=2, padx=5, pady=5)

btn_2 = tk.Button(frame, text="2", command=lambda:add_to_calculation(2), **button_params)
btn_2.grid(row=5, column=1, padx=5, pady=5)

btn_1 = tk.Button(frame, text="1", command=lambda: add_to_calculation(1), **button_params)
btn_1.grid(row=5, column=0, padx=5, pady=5)

btn_0 = tk.Button(frame, text="0", command=lambda: add_to_calculation(0), **button_params)
btn_0.grid(row=6, column=0, padx=5, pady=5)

btn_plus = tk.Button(frame, text="+", command=lambda: add_to_calculation("+"), **button_params, bg="#B2AFAF")
btn_plus.grid(row=2, column=4, padx=5, pady=5)

btn_minus = tk.Button(frame, text="-", command=lambda: add_to_calculation("-"), **button_params, bg="#B2AFAF")
btn_minus.grid(row=3, column=4, padx=5, pady=5)

btn_multiply = tk.Button(frame, text="*", command=lambda: add_to_calculation("*"), **button_params, bg="#B2AFAF")
btn_multiply.grid(row=4, column=4, padx=5, pady=5)

btn_divide = tk.Button(frame, text="/", command=lambda: add_to_calculation("/"), **button_params, bg="#B2AFAF")
btn_divide.grid(row=5, column=4, padx=5, pady=5)

btn_dot = tk.Button(frame, text=".", command=lambda:add_to_calculation("."), **button_params, bg="#B2AFAF")
btn_dot.grid(row=6, column=4, padx=5, pady=5)

btn_clear = tk.Button(frame, text="C", command=clear_field, width=13, font=("Bahnschrift", 14), bg="orange")
btn_clear.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

btn_open = tk.Button(frame, text="(", command=lambda: add_to_calculation("("), **button_params, bg="#B2AFAF")
btn_open.grid(row=6, column=1, padx=5, pady=5)

btn_close = tk.Button(frame, text=")", command=lambda: add_to_calculation(")"), **button_params, bg="#B2AFAF")
btn_close.grid(row=6, column=2, padx=5, pady=5)

btn_equal = tk.Button(frame, text="=", command=evaluate_calculation, **button_params, bg="orange")
btn_equal.grid(row=2, column=2, padx=5, pady=5)



root.mainloop()