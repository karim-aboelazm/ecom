from django.urls import path
from .views import *

app_name = 'ecommerce'
urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('all-cars/',AllCarsPageView.as_view(),name='all_cars'),
    path('one-cars/<int:pk>',OneCarDetail.as_view(),name='one_car')

]
