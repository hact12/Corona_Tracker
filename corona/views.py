import requests
from django.shortcuts import render
from urllib.request import urlopen
import json
from .models import Country



def home(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        country = Country(name=name)
        country.save()
    
    country=Country.objects.last()
    print(country)
    url = "https://covid-193.p.rapidapi.com/statistics"
    
    querystring = {"country":"UK"}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    
    data = response['response']
    s = data[0]
    # print(s)
    # print(type(s))
   

    context = {
        'all': s['cases']['total'],
        'recovered': s['cases']['recovered'],
        'deaths': s['deaths']['total'],
        'new': s['cases']['new'],
        'serious': s['cases']['critical'],
        'country':s['country'],
    }

    
   

    return render(request, 'corona/index.html', context)
