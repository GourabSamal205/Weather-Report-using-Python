# 🌦 Weather Report using Python

A simple and user-friendly **Weather Report Application** built with **Python**, **Tkinter**, and the **OpenWeatherMap API**. This desktop application allows users to enter a city name and instantly view real-time weather information, including temperature, humidity, feels-like temperature, and weather conditions.

---

## 📌 Features

* 🌍 Search weather by city name
* 🌡 Display current temperature (°C)
* 🤔 Show "Feels Like" temperature
* 💧 Display humidity percentage
* ☁ Show current weather condition
* ⚠ Error handling for invalid city names
* 🖥 Simple and intuitive GUI built with Tkinter

---

## 🛠 Technologies Used

* Python 3.x
* Tkinter (GUI)
* Requests Library
* OpenWeatherMap API

---

## 📂 Project Structure

```
Weather-Report-using-Python/
│
├── weather_app.py
├── README.md
├── requirements.txt
└── screenshots/
    └── app.png
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/GourabSama1205/Weather-Report-using-Python.git
```

### 2. Navigate to the Project Folder

```bash
cd Weather-Report-using-Python
```

### 3. Install Dependencies

```bash
pip install requests
```

---

## ▶️ Run the Application

```bash
python weather_app.py
```

---

## 🔑 API Key

This project uses the **OpenWeatherMap API**.

Replace the API key in the code with your own:

```python
API_KEY = "YOUR_API_KEY"
```

You can get a free API key by creating an account on the OpenWeatherMap website.

---

## 📷 Application Preview

Add a screenshot of your application inside the `screenshots` folder and display it here:

```markdown
![Weather App](screenshots/app.png)
```

---

## 📖 How It Works

1. Enter the name of a city.
2. Click the **Get Weather** button.
3. The application sends a request to the OpenWeatherMap API.
4. Weather details are retrieved and displayed on the screen.
5. If the city name is invalid or the request fails, an error message is shown.

---

## 📚 Concepts Used

* GUI Programming with Tkinter
* REST API Integration
* HTTP Requests
* JSON Data Handling
* Exception Handling
* Functions
* User Input Validation

---

## 🔮 Future Enhancements

* 🌍 Auto-detect current location
* 📅 7-day weather forecast
* 🌙 Dark mode
* 🌐 Multiple language support
* 📍 Search history
* 🌡 Temperature unit switch (°C / °F)
* 🌅 Weather icons and animations

---

## 👨‍💻 Author

**Gourab Samal**

GitHub: https://github.com/GourabSama1205

---

## 📄 License

This project is licensed under the MIT License.
