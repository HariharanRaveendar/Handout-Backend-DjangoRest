from django.urls import path
from .views import *
urlpatterns = [
    path('DonateFood/',DonateFood,name="DonateFood"),
    path('DonateCloth/',DonateCloth,name="DonateCloth"),
    path('DonateBook/',DonateBook,name="DonateBook"),
    path('GetFoodInfo/<int:id>/',GetFoodInfo,name="GetFoodInfo"),
    path('GetClothInfo/<int:id>/',GetClothInfo,name="GetClothInfo"),
    path('GetBookInfo/<int:id>/',GetBookInfo,name="GetBookInfo"),


]
