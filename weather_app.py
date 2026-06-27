import tkinter as tk
from tkinter import messagebox
import requests

# 🔑 Put your API key here
API_KEY = "1f523d218ae3a3eb237a2646f9164d78"

def get_weather():
    city = entry_city.get().strip()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        # Debug (optional)
        # print(data)

        if data.get("cod") != 200:
            messagebox.showerror("Error", data.get("message", "City not found"))
            return

        # Extract data
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        result = (
            f"📍 {city_name}, {country}\n\n"
            f"🌡 Temperature: {temp}°C\n"
            f"🤔 Feels Like: {feels_like}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"☁ Condition: {weather}"
        )

        label_result.config(text=result)

    except Exception as e:
        messagebox.showerror("Error", "Failed to fetch weather data")

# 🖥 GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("350x350")
root.resizable(False, False)

tk.Label(root, text="🌦 Weather App", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack()
entry_city = tk.Entry(root, width=30, font=("Arial", 11))
entry_city.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 11), justify="left")
label_result.pack(pady=20)

root.mainloop()