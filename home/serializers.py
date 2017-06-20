from rest_framework import serializers,mixins
from models import Beacon,AuthUser



class BeaconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beacon
        fields = ('seq','uuid','value')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('id','email','score')




