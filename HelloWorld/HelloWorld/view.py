# editing view.py file
from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse

def print(request):
      return HttpResponse("Message:Hello World!")

