from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('signp',views.signup,name='ok')
]