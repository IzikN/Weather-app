
# Create your views here
import requests
from django.shortcuts import render

def home(request):
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.POST.get('city')
        
        # OpenWeatherMap API Key 
        api_key = '6c4bb55a4a09f501d60f6181222ea2ca'
        
        # URL for the weather API
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        # Fetch the weather data from the API
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # If the city is found
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
            }
        else:
            # If the city is not found
            error_message = "City not found or API error."

    return render(request, 'home.html', {'weather_data': weather_data, 'error_message': error_message})
