
#render :bütünü ile gönderdiğimiz olucak.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def create_category(request):  # ...../category/create
    return HttpResponse("<h1>Merhaba Dünya!<h1/>")


def list_category(request):   #...../category/list
    return render(request,'category/list.html')

# /category/detail url'ine cevap verecek bir action yapınız.
# detail.html render edilsin.

def detail_category(request):    #..../category/detail
    return render(request,'category/detail.html')