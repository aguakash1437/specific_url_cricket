from django.shortcuts import render

# Create your views here.
def saca(request):
    return render(request,'saca.html')


def south(request):
    return render(request,'south.html')