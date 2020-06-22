from django.shortcuts import render

# Create your views here.

def websitehome(request):
    return render(request,'website/website.html')
