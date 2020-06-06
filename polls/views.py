from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    print(request)
    return HttpResponse("Hellow, world. You're at the polls index.")


def Test_Index(request):
    return HttpResponse("변경되었는가??")