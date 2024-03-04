import tkinter as tk

def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit/1.8) - 32

def convert_temperature():
    try:
        celsius_value = float(entry.get())
        fahrenheit_value = celsius_to_fahrenheit(celsius_value)
        output_label.config(text=f"{celsius_value}°C is {fahrenheit_value:.2f}°F")
    except ValueError:
        output_label.config(text="Please enter a valid temperature.")

# Create the main window
app = tk.Tk()
app.title("Temperature Converter")

# Create and place widgets
label = tk.Label(app, text="Enter Temperature in Celsius:")
label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=10)

convert_button = tk.Button(app, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)

output_label = tk.Label(app, text="")
output_label.pack(pady=10)

# Start the application
app.mainloop()