from django.views.generic.base import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]