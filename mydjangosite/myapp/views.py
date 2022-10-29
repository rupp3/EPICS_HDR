from django.shortcuts import render

# Create your views here.


def index(request):
    #thirdparameter needs to be a dict
    return render(request, "myapp/index.html", {})


