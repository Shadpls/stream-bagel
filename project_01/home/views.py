from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


# def test(request):
#     return HttpResponse("<p>Hello!</p>")

@api_view(['GET'])
def getData(request):
    person = { 'name': 'Dennis', 'age': 28 }
    return Response(person)

