from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from api.models import HelthCare, User
from api.serializers import UserSerializer, UserLoginSerializer, madicinerializer, updateserializer, \
    updatHelthCareSerializer, deletemadicineserializer


class register(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg": "registration sucessfully"})
        return Response(serializer.errors)
class login(APIView):
    def post(self,request):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({"msg":"login successfully"})
        return Response(serializer.errors)

class madicine(APIView):
    def post(self,request):
        serializer=madicinerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg":"medicine added"})
        return Response(serializer.errors)

dataSend=0
def data1(request):
    global dataSend
    dataSend=request

username=''
email=''
class activation(APIView):
    def get(self,request):
        id=request.GET.get('id')
        odata=User.objects.get(id=id)
        global username
        username=str(odata.name)
        global email
        email=odata.email
        data=HelthCare.objects.filter(user=id)
        l=[]
        for i in data:
            l.append(i.madicine)
            l.append(i.timing)
        d={}
        for j in range(0,len(l),2):
            d[l[j]]=l[j+1]
        data1(d)
        import app
        return Response(d)

class updateMedicianTiming(APIView):
    def put(self,request):
        serilizer=updateserializer(data=request.data)
        if serilizer.is_valid(raise_exception=True):
            data = request.data
            name = data.get('madicine')
            odata = HelthCare.objects.get(madicine=name)
            serializer1=updatHelthCareSerializer(odata,data=request.data,partial=True)
            if serializer1.is_valid():
                serializer1.save()
                return Response({'msg':'dtime changed successfully'})
        return Response(serilizer.errors)

class deleteMedician(APIView):
    def delete(self,request):
        serializer=deletemadicineserializer(data=request.data)
        if serializer.is_valid():
            data = request.data
            name = data.get('madicine')
            odata = HelthCare.objects.get(madicine=name)
            odata.delete()
            return Response({'msg':'madicine delete sucessfully'})
        return Response(serializer.errors)








