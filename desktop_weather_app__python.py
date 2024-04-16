import tkinter as tk


# initialize window

root = tk.Tk()
root.geometry("400x400")  # size of the window by default
root.resizable(0, 0)  # to make the window size fixed
root.title("Weather App")  # title of window

# style window
city_head = tk.Label(root, text='Enter City Name', font='Arial 12 bold').pack(pady=10)  # to generate label heading
inp_city = tk.Entry(root, textvariable="--- Placeholder City Value ---", width=24, font='Arial 14 bold').pack()  # entry field

tk.Button(root, command="--- Placeholder Show Weather Function ---", text="Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5).pack(pady=20)

weather_now = tk.Label(root, text="The Weather is: ", font='arial 12 bold').pack(pady=10)

tfield = tk.Text(root, width=46, height=10)
tfield.pack()

root.mainloop()
