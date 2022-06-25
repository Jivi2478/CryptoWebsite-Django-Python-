from django.shortcuts import render
# Create your views here.
def firststep(request):
    return render(request,'DEMOAPP/homepage.html')