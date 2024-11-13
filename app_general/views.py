from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http.response import HttpResponse
from django.shortcuts import render
from app_foods.models import Food
from app_general.forms import SubscriptionForm, SubscriptionModelForm
from .models import Subscription



# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')

def about(request):
    return render(request, 'app_general/about.html')

def subscription(request): 
    if request.method == "POST": 
        form = SubscriptionModelForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return HttpResponseRedirect(reverse('subscription_thankyou')) 
        
        else:  
            context = {'form': form} 
        return render(request, 'app_general/subscription_form.html', context) 
    
    else: 
        form = SubscriptionModelForm()

    context = {'form': form} 
    return render(request, 'app_general/subscription_form.html', context)

def subscription_thankyou(request): 
    return render(request, 'app_general/subscription_thankyou.html')