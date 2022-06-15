from unittest import result
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout





from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        myuser.save()
        
        return redirect('signin')
        
        
    return render(request, "signup.html")



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)   

        if user is not None:
            login(request, user)
            # messages.info(request, 'Welcome to my Website')
            return redirect('weather_data')
        else:
            # messages.warning(request, "Invalid credentials")
            return redirect('home')



    return render(request, "signin.html")


API_KEY = "rW7eqasgUvIPmsLYMcKJC2fAHQavA2nd"
import urllib
import json

def getLocation(City_Name):
    search_address = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey="+API_KEY+"&q="+City_Name+"&details=true"
    print("search_address==>>",search_address)

    with urllib.request.urlopen(search_address) as search_address:
        data = json.loads(search_address.read().decode())


    location_key = data[0]['Key']
    city_name = data[0]['EnglishName']
    region_name = data[0]['Region']['EnglishName']
    country_name = data[0]['Country']['EnglishName']
    data = {"city_name":city_name,"location_key":location_key,"region_name":region_name,"country_name":country_name}
    
    return(data)


import requests
import datetime 

def weather_data(request):
    print("calling search")
    if 'city' in request.GET:
        City_Name = request.GET['city']
        print("City_Name==>>",City_Name)
        # fetch the weather from AccuWeather

        location_key = getLocation(City_Name)
        print("dataaa",location_key)
        
        daily_forcastURL = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"+location_key['location_key']+"?apikey="+API_KEY+"&details=True"
# 
        response = requests.get(daily_forcastURL)
        weather_data = response.json().get('DailyForecasts',{})
        print("weather_data==>",type(weather_data))
       
        for i in weather_data:

            now = datetime.datetime.now()
            date = now.strftime("%B %d, %Y %H:%M:%S")
            
            region = location_key['region_name']
            country = location_key['country_name']
            min_temp = i['Temperature']['Minimum']['Value'] 
            max_temp = i['Temperature']['Maximum']['Value']
            unit = i['Temperature']['Minimum']['Unit']
            LongPhrase =  i['Day']['LongPhrase']
            rain_probability = i['Day']['RainProbability']

           
        all_data = {"date":date,"rain_probability":rain_probability , "LongPhrase":LongPhrase, "min_temp":min_temp,"max_temp":max_temp,"unit":unit,"region":region,"country":country}
        print("type==",type(all_data))
        print("all_data",all_data)

        return render(request, "weather.html", {"all_data":all_data})

    else:
        return render(request, "weather.html")
        





def search(request):
    print("calling weather")
    # if 'city' in request.GET:

    # #     City_Name = request.GET['city']
    #     print("City_Name=>",request.GET['city'])
    # fetch the weather from AccuWeather
        # location_key = getLocation(City_Name)

        # daily_forcastURL = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"+location_key+"?apikey="+API_KEY+"&details=True"

        # with urllib.request.urlopen(daily_forcastURL) as daily_forcastURL:
        #     data = json.loads(daily_forcastURL.read().decode('utf-8'))
        
        # for i in data['DailyForecasts']:

        #     now = datetime.now()
        #     date = now.strftime("%B %d, %Y %H:%M:%S")
            
        #     min_temp = i['Temperature']['Minimum']['Value'] 
        #     max_temp = i['Temperature']['Maximum']['Value']
        #     unit = i['Temperature']['Minimum']['Unit']
        #     short_phase =  i['Day']['ShortPhrase']
        #     rain_probability = i['Day']['RainProbability']

    return render(request, "weather.html")





def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')



# API_KEY = "rdQ3rQrnNNrat4dp2C2iZuInGvzAHxwY"

# def getLocation(City_Name):
#     search_address = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey="+API_KEY+"&q="+City_Name+"&details=true"
#     with urllib.request.urlopen(search_address) as search_address:
#         data = json.loads(search_address.read().decode())
#     location_key = data[0]['Key']
#     city_name = data[0]['EnglishName']
#     region_name = data[0]['Region']['EnglishName']
#     country_name = data[0]['Country']['EnglishName']
#     return(location_key)

# from datetime import date, datetime


def weather(request):
    if 'city' in request.GET:
        City_Name = request.GET['city']
        print("City_Name=>",City_Name)
    # fetch the weather from AccuWeather
        # location_key = getLocation(City_Name)

        # daily_forcastURL = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"+location_key+"?apikey="+API_KEY+"&details=True"

        # with urllib.request.urlopen(daily_forcastURL) as daily_forcastURL:
        #     data = json.loads(daily_forcastURL.read().decode('utf-8'))
        
        # for i in data['DailyForecasts']:

        #     now = datetime.now()
        #     date = now.strftime("%B %d, %Y %H:%M:%S")
            
        #     min_temp = i['Temperature']['Minimum']['Value'] 
        #     max_temp = i['Temperature']['Maximum']['Value']
        #     unit = i['Temperature']['Minimum']['Unit']
        #     short_phase =  i['Day']['ShortPhrase']
        #     rain_probability = i['Day']['RainProbability']


        return render(request, 'weather.html')


# decode_data = json.loads(resp.data.decode('utf-8'))
#             User_Instance["IP_ADDRESS"] = getClientIp(request)  
#             User_Instance["IP_CITY"] = decode_data['city']
#             User_Instance["IP_COUNTRY"] = decode_data['country']