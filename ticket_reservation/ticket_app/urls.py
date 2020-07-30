from django.urls import path
from ticket_app import views
app_name = 'ticket_app'

urlpatterns = [
path('',views.index,name='index'),
]
