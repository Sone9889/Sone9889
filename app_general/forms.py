from django import forms
from django.db.models.base import Model
from  app_foods.models import Food
from .models import Subscription

class FoodMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.titel
    
    
class SubscriptionForm(forms.Form):
    # name = forms.CharField(max_length=60, required=True, label='Name and LastName')
    # email = forms.EmailField(max_length=60, required=True, label='Enter Email')
    # food_set =FoodMultipleChoiceField(
    #     queryset=Food.objects.order_by('-is_premium'),
    #     required=True,
    #     label='Menu of interest',
    #     widget=forms.CheckboxSelectMultiple
    #     )
    accepted = forms.BooleanField(
        required=True, label='Agree to the terms'
        )
    
class SubscriptionModelForm(forms.ModelForm):
        food_set =FoodMultipleChoiceField(
        queryset=Food.objects.order_by('-is_premium'),
        required=True,
        label='Menu of interest',
        widget=forms.CheckboxSelectMultiple
        )

        accepted = forms.BooleanField(
        required=True, label='Agree to the terms'
        )

        class Meta:
            model = Subscription
            fields = ['name', 'email', 'food_set', 'accepted']
            labels = {
                 'name': 'Name and LastName',
                 'email': 'Enter Email',
                 'food_set': 'Menu of interest',
            }
            