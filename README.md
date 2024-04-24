# Desktop Weather App

The App allows you to enter a city, fetches the according current weather data from the [Open Weather API](https://openweathermap.org/) and displays them in curated form in the text field. Further, there are three favorite places quick buttons. At the moment these are hard-coded to display weather data for Avignon, Kitzbühel and Amsterdam. For a future release these should be adjustable according to the user's preferences.

## Installation

To pull data from the OpenWeather API you will need an API key. You can register for a free account at https://openweathermap.org/ and generate your personal API key. Then copy it and save it in a text file named "API_key". This file should be located in the same folder as the desktop application Python file.

The packages that need to be installed additionally to Python are
- tkinter
- requests
- datetime
- pytz
The full list of dependencies can be found in and installed directly from the requirements document.

```bash
pip install -r requirements.txt
```

## Usage

Running the script in the terminal will open the Desktop App and a separate window will pop up. Enter the name of the city you would like to get weather data for and press the "Check Weather" button.

```bash
python desktop_weather_app__python.py.py
```

Closing the window will also terminate the script running in the terminal.

As the favorite places buttons are hard-coded at the moment, in order to change them you would have to do so directly in the Python file.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## Attribution

This project was inspired by Pranjal Srivastava. 
Article: https://www.askpython.com/python/examples/gui-weather-app-in-python


## License

[MIT](https://choosealicense.com/licenses/mit/)