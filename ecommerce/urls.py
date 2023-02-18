from django.urls import path
from .views import *

app_name = 'ecommerce'
urlpatterns = [
   path('',HomePageView.as_view(),name='home')
]
