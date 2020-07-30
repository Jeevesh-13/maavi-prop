from django.shortcuts import render
from ticket_app.forms import Customer_info

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# Create your views here.

def index(request):
    if request.method == 'POST':
        cus_form = Customer_info(request.POST)
        if cus_form.is_valid():
            cus_form.save()
            cus_form = Customer_info()
            return render(request,'ticket_app/base1.html',{'cus_form':cus_form})
        else:
            print(cus_form.errors)
    else:
        cus_form = Customer_info()
    return render(request,'ticket_app/base1.html',{'cus_form':cus_form})
