from django.shortcuts import render

def home(request):
    return render(request, 'Gpt2Integration/home.html')

# Create your views here.
