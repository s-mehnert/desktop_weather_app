import tkinter as tk
import requests
from datetime import datetime
import pytz

# initialize window

root = tk.Tk()
root.geometry("400x500")  # size of the window by default
root.resizable(0, 0)  # to make the window size fixed
root.title("Weather App")  # title of window

# create functionality to change time format


def time_format_for_location(utc_with_tz):
    local_time = datetime.fromtimestamp(utc_with_tz, pytz.utc)
    return local_time.time()

# style window


city_value = tk.StringVar(root, "")


# to generate label heading
city_head = tk.Label(root, text='Enter City Name', font='Arial 12 bold').pack(pady=10)
# entry field
inp_city = tk.Entry(root, textvariable=city_value, width=24, font='Arial 14 bold').pack()

# create functionality for retrieving weather data from OpenWeather.com

api_key = ""
with open("API_key.txt") as key:
    api_key = key.read()


def show_weather(city_name=None):
    # Get city name from user from the input field (later in the code)
    if not city_name:
        city_name = city_value.get()
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    weather_url = base_url + city_name + '&appid=' + api_key  # API url
    response = requests.get(weather_url)  # Get the response from fetched url
    weather_info = response.json()  # changing response from json to python readable
    tfield.delete("1.0", "end")  # to clear the text field for every new output

    # as per API documentation, if the code is 200, it means that weather data was
    # successfully fetched
    if weather_info['cod'] == 200:
        kelvin = 273  # value of kelvin

        # -----------Storing the fetched values of weather of a city

        # converting default kelvin value to Celcius
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        humidity = weather_info['main']['humidity']
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

# assigning Values to our weather varaible, to display as output

        weather = f"""
        Weather of: {city_name}
        Temperature (Celsius): {temp}°
        Feels like in (Celsius): {feels_like_temp}°
        Humidity: {humidity}%
        Sunrise at {sunrise_time}
        Sunset at {sunset_time}
        Cloud: {cloudy}%
        Info: {description}
        """
    else:
        weather = f"""
        Weather for

        {city_name.upper()}

        not found!


        Please, check your spelling!
        """

    tfield.insert("1.0", weather)  # to insert or send value in our Text Field to display output


tk.Button(root, command=show_weather, text="Check Weather", font="Arial 10", bg='lightblue',
          fg='black', activebackground="teal", padx=5, pady=5).pack(pady=20)

# Displaying weather data

weather_now = tk.Label(root, text="The Weather is: ", font='arial 12 bold').pack(pady=10)

tfield = tk.Text(root, width=46, height=10)
tfield.pack()

fav1 = tk.Button(root, command=lambda: show_weather("Avignon"), text="Avignon", font="Arial 10", 
                 bg='lightyellow', fg='black', activebackground="teal", padx=5, pady=5)


fav2 = tk.Button(root, command=lambda: show_weather("Kitzbühel"), text="Kitzbühel",
                 font="Arial 10", bg='thistle', fg='black', activebackground="teal",
                 padx=5, pady=5)

fav3 = tk.Button(root, command=lambda: show_weather("Amsterdam"), text="Amsterdam",
                 font="Arial 10", bg='aquamarine', fg='black', activebackground="teal",
                 padx=5, pady=5)

fav1.pack(side="left", expand=True)
fav2.pack(side="left", expand=True)
fav3.pack(side="left", expand=True)

root.mainloop()
