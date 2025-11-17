from django.http import HttpResponse;
from django.shortcuts import render

def home(Request):
    # return HttpResponse("Hello, Django!")
    return render(Request, 'index.html') #yyou have to first intialize or configure template in settings.py

def about(Request):
    return render(Request, 'website/index.html')

def contact(Request):
    return HttpResponse("This is contact page")