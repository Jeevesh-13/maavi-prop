from django import forms
from ticket_app.models import Customers

class Customer_info(forms.ModelForm):
    class Meta():
        model = Customers
        fields = '__all__'
