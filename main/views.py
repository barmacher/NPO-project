import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import News, Law, Publication
from main.serializer import NewsSerializer, LawSerializer, PublicationSerializer, LawCreateValidateSerializer, \
    NewsCreateValidateSerializer, PublicationValidateCreateSerializer


class NewsListAPIView(ListAPIView):
    # def get(self, request):
    #
    #     news = News.objects.all()
    #     data = NewsSerializer(news, many=True, context={
    #         'request': request
    #     }).data
    #     return Response(data=data)
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination
    def post(self,request):
        form = request.data
        serializer = NewsCreateValidateSerializer(data=form)
        if not serializer.is_valid():
            return Response(
                data={'message':'error',
                      'errors': serializer.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )

        title = form['title']
        short_description = form['short_description']
        full_description = form['full_description']


        link = form['link']
        News.objects.create(title = title, short_description=short_description, full_description=full_description, publication_date = datetime.datetime.now(), link=link)
        return Response(data={'message': 'News added!'})


class LawListAPIView(APIView):

    # def get(self, request):
    #     laws = Law.objects.all()
    #     data = LawSerializer(laws, many=True, context={
    #         'request': request
    #     }).data
    #     return Response(data=data)
    queryset = Law.objects.all()
    serializer_class = LawSerializer
    pagination_class = PageNumberPagination
    def post(self, request):
        form = request.data
        serializer = LawCreateValidateSerializer(data=form)
        if not serializer.is_valid():
            return Response(
                data={'message': 'error',
                      'errors': serializer.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        title = form['title']
        short_description = form['short_description']
        full_description = form['full_description']
        type = form['type']
        Law.objects.create(title=title, short_description=short_description, full_description=full_description,
                            publication_date=datetime.datetime.now(), type=type)
        return Response(data={'message': 'Law added!'})


class PublicationListAPIView(APIView):
    # def get(self, request):
    #     publications = Publication.objects.all()
    #     data = PublicationSerializer(publications, many=True, context={
    #         'request': request
    #     }).data
    #     return Response(data=data)
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    pagination_class = PageNumberPagination
    def post(self, request):
        form = request.data
        serializer = PublicationValidateCreateSerializer(data=form)
        if not serializer.is_valid():
            return Response(
                data={'message': 'error',
                      'errors': serializer.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        title = form['title']
        short_description = form['short_description']
        full_description = form['full_description']
        type = form['type']
        Publication.objects.create(title=title, short_description=short_description, full_description=full_description,
                                   publication_date=datetime.datetime.now(), type=type)
        return Response(data={'message': 'Publication added!'})

class NewsDetailUpdateDeleteAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class LawsDetailUpdateDeleteAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Law.objects.all()
    serializer_class = LawSerializer
class PublicationsDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

