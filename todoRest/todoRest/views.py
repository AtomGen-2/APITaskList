from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def hello(request):
    # safe = False is used to maintain that if non-dictionary type objects is passed, it should not throw an errror
    return JsonResponse("helloWorld", safe=False)