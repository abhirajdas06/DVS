from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello Home")
    return render(request, "home/index.html")

def about(request):
    # return HttpResponse("Hello Home")
    return render(request, "home/about.html")

def contact(request):
    # return HttpResponse("Hello Home")
    return render(request, "home/contact.html")