from django.shortcuts import render

# Create your views here.
def landingpage(request):
    return render(request, 'landingpage.html')


def homepage(request):
    #return HttpResponse("this is homepage")
    return render(request, 'home.html')