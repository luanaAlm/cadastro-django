from django.shortcuts import render


#views core
def home(request):
    return render(request, 'core/index.html')

