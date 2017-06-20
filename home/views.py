# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from rest_framework.generics import GenericAPIView
from rest_framework import mixins,viewsets
from models import AuthUser,Beacon
from serializers import BeaconSerializer,UserSerializer

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'home/post_list.html', {'posts': posts})



class UserViewSet(GenericAPIView, mixins.ListModelMixin):
    queryset = AuthUser.objects.all()
    serializer_class = UserSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

### beacon data


class BeaconViewSet(GenericAPIView, mixins.ListModelMixin):
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)