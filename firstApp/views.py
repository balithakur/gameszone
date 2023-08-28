from django.shortcuts import render

# Create your views here.

def home(request):
    #return HttpResponse("this is homepage")
    return render(request, 'navbar.html')