from django.shortcuts import render
import requests
import json
from .models import Countries

# Create your views here.

    
def home(request):
    cou=request.POST.get('country')
    print(cou)
    url = "https://covid-193.p.rapidapi.com/statistics"
    querystring={"country":cou}
    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "YOUR_API_KEY"
        }

    response = requests.request("GET", url, headers=headers,params=querystring).json()
    
    data=response['response']
    d=data[0]
    context={
        'all':d['cases']['total'],
        'recovered':d['cases']['recovered'],
        'deaths':d['cases']['total'],
        'new':d['cases']['new'],
        'critical':d['cases']['critical'],
        'country':cou
        
    }
    return render(request,'covidapp/index.html',context)