from django.shortcuts import render

# Create your views here.
def say_home(request):
    return render(request, 'home.html')