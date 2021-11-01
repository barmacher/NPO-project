from django.contrib.auth.models import User
from django.db import models
from main.models import News, Law, Publication



class FavoriteNews(models.Model):

    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class FavoriteLaw(models.Model):
    law = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class FavoritePublication(models.Model):
    publication = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
