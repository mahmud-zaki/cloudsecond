from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/authentication/login')
def index(request):
    return render(request, 'cloud_s/index.html')
def add_cloud_s(request):
    return render(request, 'cloud_s/add_cloud_s.html')