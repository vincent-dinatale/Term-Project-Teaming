from flask import Flask, render_template, request
from config import WEATHER_APIKEY

import requests

app = Flask(__name__)  

def get_playlist_url(temperature, weather_conditions):
    # Determine the playlist URL based on temperature and weather conditions
    if temperature < 5:
        return "https://open.spotify.com/embed/playlist/6LyJiKTzvOm4h3Eub36wYE?utm_source=generator"
    elif 5 <= temperature < 15:
        if "snow" in weather_conditions.lower():
            return "https://open.spotify.com/embed/playlist/6o6hH1TsIQuPn8tUircyld?utm_source=generator"
        elif "mist" in weather_conditions.lower():
            return "https://open.spotify.com/embed/playlist/78fp8BwhXDslBEz5KL6pes?utm_source=generator"
        else:
            return "https://open.spotify.com/embed/playlist/37i9dQZF1EIdweJIvlLS4r?utm_source=generator"
    elif 15 <= temperature < 25:
        if "thunderstorm" in weather_conditions.lower():
            return "https://open.spotify.com/embed/playlist/37i9dQZF1EIeOmlQSSmx93?utm_source=generator"
        elif "rain" in weather_conditions.lower() or "shower rain" in weather_conditions.lower():
            return "https://open.spotify.com/embed/playlist/47S4MBG0EEXwA0GdJUA4Ur?utm_source=generator"
        elif "broken clouds" in weather_conditions.lower():
            return "https://open.spotify.com/embed/playlist/0xMhPiF5Y9OcYsjTt1jXUa?utm_source=generator"
        else:
            return "https://open.spotify.com/embed/playlist/55YMlBhwDjoEGXhCroFt5f?utm_source=generator"
    elif 25 <= temperature < 35:
        if "clear sky" in weather_conditions.lower():
            return "https://open.spotify.com/embed/playlist/7iIExgD1GMlnI4VD0S2XKG?utm_source=generator"
        elif "few clouds" in weather_conditions.lower() or "overcast clouds" in weather_conditions.lower():
            return "https://open.spotify.com/embed/playlist/37i9dQZF1EIgxHuuVqSn9D?utm_source=generator"
        else:
            return "https://open.spotify.com/embed/playlist/0FusURoHRX7F4TGpQInoYc?utm_source=generator"
    else:
        return "https://open.spotify.com/embed/playlist/37i9dQZF1EIhAIcvkNTvTZ?utm_source=generator"


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/weather')
def weather():
    location = request.args.get('location')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_APIKEY}&units=imperial'
    response = requests.get(url).json()

    temperature = response['main']['temp']
    weather_conditions = response['weather'][0]['description']
    feels_like = response['main']['feels_like']
    temp_min = response['main']['temp_min']
    temp_max = response['main']['temp_max']
    humidity = response['main']['humidity']
    wind = response['wind']['speed']
    
    # Check if 'gust' is available in the response
    gust = response['wind'].get('gust', 'none')

    # Get the playlist URL based on temperature and weather conditions
    playlist_url = get_playlist_url(temperature, weather_conditions)

    return render_template('weather.html', location=location, temperature=temperature, 
                           weather_conditions=weather_conditions, feels_like=feels_like, 
                           temp_min=temp_min, temp_max=temp_max, humidity=humidity, 
                           wind=wind, gust=gust, playlist_url=playlist_url)


if __name__ == '__main__':
    app.run(debug=True)
