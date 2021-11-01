from rest_framework import serializers

from favorite.models import FavoriteNews, FavoriteLaw, FavoritePublication


class FavoriteNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteNews
        fields = '__all__'

class FavoriteLawSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteLaw
        fields = '__all__'

class FavoritePublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePublication
        fields = '__all__'
