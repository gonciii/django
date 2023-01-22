
#render :bütünü ile gönderdiğimiz olucak.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def create_category(request):  # ...../category/create
    return HttpResponse("<h1>Merhaba Dünya!<h1/>")


def list_category(request):   #...../category/list
    return render(request,'htmldosyasi')

