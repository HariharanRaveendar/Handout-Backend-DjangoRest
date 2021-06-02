from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from donate.models import Foods,Cloths,Books
from .serializers import FoodSerilizers,ClothSerilizers,BookSerilizers

@api_view(['GET'])
def GetBookInfo(request,id):
    if request.method == 'GET':
        data = Books.objects.get(pk=id)
        res={}
        res['DonarName']=data.donatorName
        res['donatorMobile']=data.donatorMobile
        res['donationAddress']=data.donationAddress
        res['landMark']=data.landMark
        res['booksType']=data.booksType
        res['booksName']=data.booksName
        res['quantity']=data.quantity
        res['pickupDate']=data.pickupDate
        res['preferedTime']=data.preferedTime
        res['booksDescription']=data.booksDescription
        res['longititude']=data.longititude
        res['latitude']=data.latitude
        return Response(res)


@api_view(['GET'])
def GetClothInfo(request,id):
    if request.method == 'GET':
        data = Cloths.objects.get(pk=id)
        res={}
        res['DonarName']=data.donatorName
        res['donatorMobile']=data.donatorMobile
        res['donationAddress']=data.donationAddress
        res['landMark']=data.landMark
        res['clothsType']=data.clothsType
        res['clothsName']=data.clothsName
        res['quantity']=data.quantity
        res['pickupDate']=data.pickupDate
        res['preferedTime']=data.preferedTime
        res['clothsDescription']=data.clothsDescription
        res['longititude']=data.longititude
        res['latitude']=data.latitude
        return Response(res)

@api_view(['GET'])

def GetFoodInfo (request,id):
    if request.method == 'GET':
        data = Foods.objects.get(pk=id)
        res={}
        res['DonarName']=data.donatorName
        res['donatorMobile']=data.donatorMobile
        res['donationAddress']=data.donationAddress
        res['landMark']=data.landMark
        res['foodType']=data.foodType
        res['foodName']=data.foodName
        res['quantity']=data.quantity
        res['pickupDate']=data.pickupDate
        res['preferedTime']=data.preferedTime
        res['foodDescription']=data.foodDescription
        res['longititude']=data.longititude
        res['latitude']=data.latitude
        return Response(res)


@api_view(["POST","GET"])
def DonateFood(request):
    if request.method == 'POST':
        print(request.data)
        serializer = FoodSerilizers(data=request.data)
        if serializer.is_valid():
            name = serializer.data['donatorName']
            mobilenumber = serializer.data['donatorMobile']
            donationAddress = serializer.data['donationAddress']
            landMark = serializer.data['landMark']
            foodType = serializer.data['foodType']
            foodName = serializer.data['foodName']
            quantity = serializer.data['quantity']
            pickupDate = serializer.data['pickupDate']
            preferedTime = serializer.data['preferedTime']
            foodDescription = serializer.data['foodDescription']
            latitude = serializer.data['latitude']
            longititude = serializer.data['longititude']
            data = Foods.objects.create(
                donatorName=name,
                donatorMobile=mobilenumber,
                donationAddress=donationAddress,
                landMark=landMark,
                foodType=foodType,
                foodName=foodName,
                quantity=quantity,
                pickupDate=pickupDate,
                preferedTime=preferedTime,
                foodDescription=foodDescription,
                longititude=longititude,
                latitude=latitude,
            )
            data.save()
            print(data)
            return Response("Successfully Donated")
        else:
            return Response(serializer.errors)
    elif request.method == 'GET':
        data = Foods.objects.all()
        serializer = FoodSerilizers(data, many=True)
        return Response(serializer.data)

@api_view(["POST","GET"])
def DonateCloth(request):
    if request.method == 'POST':
        serializer = ClothSerilizers(data=request.data)
        if serializer.is_valid():
            name = serializer.data['donatorName']
            mobilenumber = serializer.data['donatorMobile']
            donationAddress = serializer.data['donationAddress']
            landMark = serializer.data['landMark']
            clothsType = serializer.data['clothsType']
            clothsName = serializer.data['clothsName']
            quantity = serializer.data['quantity']
            pickupDate = serializer.data['pickupDate']
            preferedTime = serializer.data['preferedTime']
            clothsDescription = serializer.data['clothsDescription']
            latitude = serializer.data['latitude']
            longititude = serializer.data['longititude']
            data = Cloths.objects.create(
                donatorName=name,
                donatorMobile=mobilenumber,
                donationAddress=donationAddress,
                landMark=landMark,
                clothsType=clothsType,
                clothsName=clothsName,
                quantity=quantity,
                pickupDate=pickupDate,
                preferedTime=preferedTime,
                clothsDescription=clothsDescription,
                longititude=longititude,
                latitude=latitude,
            )
            data.save()
            print(data)
            return Response("Successfully Donated")
        else:
            return Response(serializer.errors)
    elif request.method == 'GET':
        data = Cloths.objects.all()
        serializer = ClothSerilizers(data, many=True)
        return Response(serializer.data)

@api_view(["POST","GET"])
def DonateBook(request):
    if request.method == 'POST':
        serializer = BookSerilizers(data=request.data)
        if serializer.is_valid():
            name = serializer.data['donatorName']
            mobilenumber = serializer.data['donatorMobile']
            donationAddress = serializer.data['donationAddress']
            landMark = serializer.data['landMark']
            booksType = serializer.data['booksType']
            booksName = serializer.data['booksName']
            quantity = serializer.data['quantity']
            pickupDate = serializer.data['pickupDate']
            preferedTime = serializer.data['preferedTime']
            booksDescription = serializer.data['booksDescription']
            latitude = serializer.data['latitude']
            longititude = serializer.data['longititude']
            data = Books.objects.create(
                donatorName=name,
                donatorMobile=mobilenumber,
                donationAddress=donationAddress,
                landMark=landMark,
                booksType=booksType,
                booksName=booksName,
                quantity=quantity,
                pickupDate=pickupDate,
                preferedTime=preferedTime,
                booksDescription=booksDescription,
                longititude=longititude,
                latitude=latitude,
            )
            data.save()
            print(data)
            return Response("Successfully Donated")
        else:
            return Response(serializer.errors)
    elif request.method == 'GET':
        data = Books.objects.all()
        serializer = BookSerilizers(data, many=True)
        return Response(serializer.data)