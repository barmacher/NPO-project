from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from favorite.models import FavoriteNews, FavoriteLaw, FavoritePublication
from favorite.serializers import FavoriteNewsSerializer, FavoritePublicationSerializer, FavoriteLawSerializer


class FavoriteNewsListAPIView(APIView):
    def get(self, request):
        favorite_news = FavoriteNews.objects.all()
        data = FavoriteNewsSerializer(favorite_news, many=True, context={
            'request': request
        }).data
        return Response(data=data)

    def post(self,request):
        pass

class FavoriteLawListAPIView(APIView):
    def get(self, request):
        favorite_laws = FavoriteLaw.objects.all()
        data = FavoriteLawSerializer(favorite_laws, many=True, context={
            'request': request
        }).data
        return Response(data=data)

    def post(self,request):
        pass

class FavoritePublicationListAPIView(APIView):
    def get(self, request):
        favorite_publication = FavoritePublication.objects.all()
        data = FavoritePublicationSerializer(favorite_publication, many=True, context={
            'request': request
        }).data
        return Response(data=data)

    def post(self,request):
        pass