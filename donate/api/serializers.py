from donate.models import Foods,Cloths,Books

from rest_framework import serializers


class FoodSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['id','donatorName','donatorMobile','donationAddress','landMark','foodType','foodName','quantity','pickupDate','preferedTime','foodDescription','latitude','longititude']


class ClothSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Cloths
        fields = ['id','donatorName','donatorMobile','donationAddress','landMark','clothsType','clothsName','quantity','pickupDate','preferedTime','clothsDescription','latitude','longititude']

class BookSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id','donatorName','donatorMobile','donationAddress','landMark','booksType','booksName','quantity','pickupDate','preferedTime','booksDescription','latitude','longititude']
