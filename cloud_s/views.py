from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'cloud_s/index.html')
def add_cloud_s(request):
    return render(request, 'cloud_s/add_cloud_s.html')