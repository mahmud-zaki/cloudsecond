from django.shortcuts import render, redirect
import os
import json
from django.conf import settings
from .models import Userpreferences
from django.contrib import messages
# Create your views here.

def index(request):
    
    exists= Userpreferences.objects.filter(user=request.user).exists
    user_preferences = None
    
    if exists:
        user_preferences = Userpreferences.objects.get(user=request.user).currency
    
    if request.method== 'GET':
        currency_data = []
    
        file_path = os.path.join(settings.BASE_DIR, 'currencies.json')
    
        with open(file_path, 'r') as json_file:
        
            data=json.load(json_file)
        
            for k,v in data.items():
                currency_data.append({'name': k, 'value': v})
    
        return render(request, 'preferences/index.html', {'currencies': currency_data})
    else:
        if exists:
            currency = request.POST['currency']
            user_preferences.currency=currency
            user_preferences.save()
        Userpreferences.objects.create(user=request.user, currency=currency)
        messages.success(request, 'Changed Saved')
