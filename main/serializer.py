from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from favorite.models import FavoriteNews, FavoriteLaw, FavoritePublication
from main.models import News, ImageNews, Law, Publication, LAW_TYPES


class ImageNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNews
        fields = 'image'.split()

class NewsSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()
    images = ImageNewsSerializer(many=True)
    class Meta:
        model = News
        fields = ['id', 'image', 'title', 'short_description', 'full_description', 'images','link', 'is_main','is_favorite']

    def get_is_favorite(self,news):
        request = self.context['request']
        print(request.user,news)
        return bool(request.user.is_authenticated and FavoriteNews.objects.filter(news=news, user=request.user))

class NewsCreateValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    short_description = serializers.CharField(min_length=1, max_length=100)
    full_description = serializers.CharField(min_length=1, max_length=150)
    is_main = serializers.BooleanField(default=False)
    link = serializers.CharField()
    def validate_title(self, title):
        news = News.objects.filter(title=title)
        if news.count() > 0:
            raise ValidationError("news with the same title already exists")
        return title

    # def validate_is_main(self, is_main):
    #     news = News.objects.filter(is_main=True)
    #     if news.count() > 0:
    #         raise ValidationError("Только одна новость может быть главной!")
    #     return is_main

    def validate_link(self,link):
        array = link.split()
        print(len(array))
        if(len(array)>1):
            raise ValidationError("Введите рабочую ссылку!")
        return link

class LawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = '__all__'
    def get_is_favorite(self,laws):
        request = self.context['request']
        print(request.user,laws)
        return bool(request.user.is_authenticated and FavoriteLaw.objects.filter(laws = laws, user=request.user))

class LawCreateValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=100)
    short_description = serializers.CharField(min_length=1, max_length=50)
    full_description = serializers.CharField(min_length=1, max_length=100)
    type = serializers.IntegerField()
    def validate_title(self, title):
        laws = Law.objects.filter(title=title)
        if laws.count() > 0:
            raise ValidationError("law with the same title already exists")
        return title

    def validate_type(self, type):
        if type < 1 or type > 3:
            raise ValidationError("Вы можете выбрать только от 1 до 3")
        return type

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
    def get_is_favorite(self,publications):
        request = self.context['request']
        print(request.user,publications)
        return bool(request.user.is_authenticated and FavoritePublication.objects.filter(publications=publications, user=request.user))

class PublicationValidateCreateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=100)
    short_description = serializers.CharField(min_length=1, max_length=50)
    full_description = serializers.CharField(min_length=1, max_length=100)
    type = serializers.IntegerField()
    def validate_title(self, title):
        publication = Publication.objects.filter(title=title)
        if publication.count() > 0:
            raise ValidationError("publication with the same title already exists")
        return title
    def validate_type(self, type):
        if type < 1 or type > 2:
            raise ValidationError("Вы можете выбрать только от 1 до 2")
        return type

