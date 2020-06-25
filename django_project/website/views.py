from django.shortcuts import render

# Create your views here.

def websitehome(request):
    print('testing>>>>>>>.')
    return render(request,'website/website.html')

def selenium(request):
    return render(request,'courses/selenium.html')
