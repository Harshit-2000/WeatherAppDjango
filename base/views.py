from django.shortcuts import get_object_or_404, render
import requests
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile, Location
from utils.utils import fetch_data

# Create your views here.


def index(request):
    try:
        if request.method == 'POST':
            city_name = request.POST.get('city')

            # fetch current and broadcast data from the API
            data = fetch_data(city_name)
            
            # show 404 page if city not found
            if data['current']['cod'] == '404':
                return render(request, 'base/404.html')

            current_weather = data['current']
            forecast = data['forecast']
            
            context = {
                'current' : current_weather,
                'forecast' : forecast,
                'data' : True
            }
        else:
            context = {'data' : False}

        return render(request, 'base/home.html', context = context)
    
    except Exception as e:
        print(e)
     
        return render(request, 'base/404.html')
    


@login_required(login_url='login')
def get_favorite(request, location_name):
    try: 
        
        data = fetch_data(location_name)
        if data['current']['cod'] == '404':
            return render(request, 'base/404.html')

        current_weather = data['current']
        forecast = data['forecast']
        
        context = {
            'current' : current_weather,
            'forecast' : forecast,
            'data' : data['data']
        }
        return render(request, 'base/home.html', context = context)
    
    except Exception as e:
        print(e)
        return render(request, 'base/404.html')


@login_required(login_url='login')
def add_favorite(request, location_name):

    print(location_name)
    # get or create a location object
    location, created = Location.objects.get_or_create(name = location_name)


    # get or create a profile object and add favourite
    profile, created = Profile.objects.get_or_create(user=request.user)
    profile.favorites.add(location)


    return redirect('/favorites/')


@login_required(login_url='login')
def favorites(request):
    # get profile and return the list of all favourites

    profile = get_object_or_404(Profile, user=request.user)
    
    favorites = profile.favorites.all()

    context = {'favorites': favorites}

    return render(request, 'base/favorites.html', context)
