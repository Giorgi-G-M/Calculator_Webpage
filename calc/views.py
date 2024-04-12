from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def add(request, num0, num1, num2):
    if num0 == "add":
        result = num1 + num2
    elif num0 == "subtract":
        result = num1 - num2
    elif num0 == "multiply":
        result = num1 * num2
    elif num0 == "divide" and num2 != 0:
        result = num1 / num2
    return render(request,"calc/result.html",{"result":result})
