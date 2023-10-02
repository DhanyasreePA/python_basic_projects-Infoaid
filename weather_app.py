logo="""
                                                  
WWWWWWWW                           WWWWWWWW                                        tttt         hhhhhhh                                                                                                                   
W::::::W                           W::::::W                                     ttt:::t         h:::::h                                                                                                                   
W::::::W                           W::::::W                                     t:::::t         h:::::h                                                                                                                   
W::::::W                           W::::::W                                     t:::::t         h:::::h                                                                                                                   
 W:::::W           WWWWW           W:::::W eeeeeeeeeeee    aaaaaaaaaaaaa  ttttttt:::::ttttttt    h::::h hhhhh           eeeeeeeeeeee    rrrrr   rrrrrrrrr          aaaaaaaaaaaaa  ppppp   ppppppppp   ppppp   ppppppppp   
  W:::::W         W:::::W         W:::::Wee::::::::::::ee  a::::::::::::a t:::::::::::::::::t    h::::hh:::::hhh      ee::::::::::::ee  r::::rrr:::::::::r         a::::::::::::a p::::ppp:::::::::p  p::::ppp:::::::::p  
   W:::::W       W:::::::W       W:::::We::::::eeeee:::::eeaaaaaaaaa:::::at:::::::::::::::::t    h::::::::::::::hh   e::::::eeeee:::::eer:::::::::::::::::r        aaaaaaaaa:::::ap:::::::::::::::::p p:::::::::::::::::p 
    W:::::W     W:::::::::W     W:::::We::::::e     e:::::e         a::::atttttt:::::::tttttt    h:::::::hhh::::::h e::::::e     e:::::err::::::rrrrr::::::r                a::::app::::::ppppp::::::ppp::::::ppppp::::::p
     W:::::W   W:::::W:::::W   W:::::W e:::::::eeeee::::::e  aaaaaaa:::::a      t:::::t          h::::::h   h::::::he:::::::eeeee::::::e r:::::r     r:::::r         aaaaaaa:::::a p:::::p     p:::::p p:::::p     p:::::p
      W:::::W W:::::W W:::::W W:::::W  e:::::::::::::::::e aa::::::::::::a      t:::::t          h:::::h     h:::::he:::::::::::::::::e  r:::::r     rrrrrrr       aa::::::::::::a p:::::p     p:::::p p:::::p     p:::::p
       W:::::W:::::W   W:::::W:::::W   e::::::eeeeeeeeeee a::::aaaa::::::a      t:::::t          h:::::h     h:::::he::::::eeeeeeeeeee   r:::::r                  a::::aaaa::::::a p:::::p     p:::::p p:::::p     p:::::p
        W:::::::::W     W:::::::::W    e:::::::e         a::::a    a:::::a      t:::::t    tttttth:::::h     h:::::he:::::::e            r:::::r                 a::::a    a:::::a p:::::p    p::::::p p:::::p    p::::::p
         W:::::::W       W:::::::W     e::::::::e        a::::a    a:::::a      t::::::tttt:::::th:::::h     h:::::he::::::::e           r:::::r                 a::::a    a:::::a p:::::ppppp:::::::p p:::::ppppp:::::::p
          W:::::W         W:::::W       e::::::::eeeeeeeea:::::aaaa::::::a      tt::::::::::::::th:::::h     h:::::h e::::::::eeeeeeee   r:::::r                 a:::::aaaa::::::a p::::::::::::::::p  p::::::::::::::::p 
           W:::W           W:::W         ee:::::::::::::e a::::::::::aa:::a       tt:::::::::::tth:::::h     h:::::h  ee:::::::::::::e   r:::::r                  a::::::::::aa:::ap::::::::::::::pp   p::::::::::::::pp  
            WWW             WWW            eeeeeeeeeeeeee  aaaaaaaaaa  aaaa         ttttttttttt  hhhhhhh     hhhhhhh    eeeeeeeeeeeeee   rrrrrrr                   aaaaaaaaaa  aaaap::::::pppppppp     p::::::pppppppp    
                                                                                                                                                                                   p:::::p             p:::::p            
                                                                                                                                                                                   p:::::p             p:::::p            
                                                                                                                                                                                  p:::::::p           p:::::::p           
                                                                                                                                                                                  p:::::::p           p:::::::p           
                                                                                                                                                                                  p:::::::p           p:::::::p           
                                                                                                                                                                                  ppppppppp           ppppppppp           

"""
import requests

print(logo)
api_key = "d0efda27d572be5b7d5733d37e159624"
base_url = "https://api.openweathermap.org/data/2.5/weather"
forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather_data(city_name):
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data.get("main") and data.get("weather"):
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        weather_condition = data["weather"][0]["description"]

        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Condition: {weather_condition}")

       
        forecast_response = requests.get(forecast_url, params=params)
        forecast_data = forecast_response.json()
        forecast_list = forecast_data.get("list")

        if forecast_list:
            print("\nForecast for the next few days:")
            for forecast in forecast_list:
                dt_txt = forecast["dt_txt"]
                temp = forecast["main"]["temp"]
                condition = forecast["weather"][0]["description"]
                print(f"{dt_txt}: {temp}°C, {condition}")
        else:
            print("Forecast data unavailable.")
    else:
        print("City not found or weather data unavailable.")

while True:
    city_name = input("Enter a city name (or 'exit' to quit): ")
    
    if city_name.lower() == "exit":
        break

    get_weather_data(city_name)
                                                                                                                                                                                                                          
