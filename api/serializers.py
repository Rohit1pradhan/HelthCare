from rest_framework import serializers

from api.models import User, HelthCare


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name','email','age','mobile','password']
    def validate(self, attrs):
        email=attrs.get('email')
        data = User.objects.get(email=attrs.get('email'))
        if data is not None:
            raise serializers.ValidationError('you are a register user you can not register with same email id more then one time')
        else:
            return attrs


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','password']

    def validate(self, attrs):
        password=attrs.get('password')
        try:
            data=User.objects.get(email=attrs.get('email'))
        except User.DoesNotExist:
            data=None
        if data==None:
            raise serializers.ValidationError('wrong mail id or you are not a register user')
        password1=data.password
        if password!=password1:
            raise serializers.ValidationError('incorrect password')
        else:
            return attrs

class madicinerializer(serializers.ModelSerializer):
    class Meta:
        model=HelthCare
        fields=['id','user','madicine','timing']

    def validate(self, attrs):
        try:
            data=User.objects.get(id=attrs.get('user'))
        except User.DoesNotExist:
            data=None
        if data==None:
            raise serializers.ValidationError('invalid id')
        else:
            return attrs

class updateserializer(serializers.ModelSerializer):
    class Meta:
        model= HelthCare
        fields=['user','madicine','timing']

    def validate(self, attrs):
        try:
            data=User.objects.get(id=attrs.get('user'))
            print(data)
        except User.DoesNotExist:
            data=None
        if data==None:
            raise serializers.ValidationError('invalid id')

        name=attrs.get('madicine')
        odata=HelthCare.objects.filter(user=attrs.get('user'))
        l = []
        for i in odata:
            l.append(i.madicine)
            l.append(i.timing)
        d = {}
        for j in range(0, len(l), 2):
            d[l[j]] = l[j + 1]
        if name not in d:
            raise serializers.ValidationError('no medician found from this name')

        return attrs


class updatHelthCareSerializer(serializers.ModelSerializer):
    class Meta:
        model= HelthCare
        fields=['user','madicine','timing']


class deletemadicineserializer(serializers.ModelSerializer):
    timing=serializers.TimeField(default=None)
    class Meta:
        model = HelthCare
        fields = ['user', 'madicine', 'timing']

    def validate(self, attrs):
        try:
            data=User.objects.get(id=attrs.get('user'))
            print(data)
        except User.DoesNotExist:
            data=None
        if data==None:
            raise serializers.ValidationError('invalid id')

        name=attrs.get('madicine')
        odata=HelthCare.objects.filter(user=attrs.get('user'))
        l = []
        for i in odata:
            l.append(i.madicine)
            l.append(i.timing)
        d = {}
        for j in range(0, len(l), 2):
            d[l[j]] = l[j + 1]
        if name not in d:
            raise serializers.ValidationError('no medician found from this name')

        return attrs






