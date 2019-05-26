from django.shortcuts import render
from teoapp.models import PostData, PostAuthor, PostContent
from teoapp.serializers import PostContentSerializer, AuthorsSerializer, AuthorsListSerializer
from rest_framework import viewsets
from rest_framework.response import Response
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, action
from rest_framework import status


class PostContentViewSet(viewsets.ModelViewSet):
    queryset = PostContent.objects.all()
    serializer_class = PostContentSerializer
    http_method_names = ['get', 'head']

class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = PostAuthor.objects.all()
    serializer_class = AuthorsSerializer
    lookup_field = 'nameId'
    http_method_names = ['get', 'head']
    #użycie dwóch serializatorów by przekazywać rózne informacje do views
    def get_serializer_class(self):
        if self.action == 'list':
            return AuthorsListSerializer
        return AuthorsSerializer
    def retrieve(self, request, nameId=None,  *args, **kwargs):
        obj = PostAuthor.objects.get(nameId=nameId)
        if nameId:
            serializer = self.serializer_class(obj)
            return Response(serializer.data)
