from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('MOVIE_API_KEY')

# @api_view(['GET'])
# def getData(request):
#     person = { 'name': 'Dennis', 'age': 28 }
#     return Response(person)

def getData(request):
    
    url = "https://streaming-availability.p.rapidapi.com/search/title"

    querystring = {"title": "Batman", "country": "us",  }

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return render(request, "test.html", { 'response': response})
