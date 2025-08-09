from django.urls import path
from . import views

# Local Routing Configuration File
urlpatterns = [
    path('', views.email_list, name='email_list'),
]
