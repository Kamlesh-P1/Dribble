from django.shortcuts import render
def home_view(request):
    return render(request, 'project.html')
def signup(request):
    return render(request, 'signup.html')
