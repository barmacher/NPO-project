from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField()
    short_description = models.TextField()
    full_description = models.TextField()
    image = models.ImageField(upload_to='news', null=True, blank=True)
    link = models.URLField()
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class ImageNews(models.Model):
    image = models.ImageField(upload_to='news')
    news = models.ForeignKey(News, on_delete=models.CASCADE,
                             related_name='images')

LAW_TYPES = (
    (1, 'Действующее законодательство'),
    (2, 'Проекты нормативных-правовых актов'),
    (3,'Международные документы')
)

class Law(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    full_description = models.TextField()
    publication_date = models.DateTimeField()
    file = models.FileField(upload_to='files')
    type = models.IntegerField(choices=LAW_TYPES, default=1)

    def __str__(self):
        return self.title

PUBLICATION_TYPES = (
    (1, 'Публикации ICNL'),
    (2, 'Другие публикации')
)

class Publication(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    full_description = models.TextField()
    publication_date = models.DateTimeField()
    file = models.FileField(upload_to='files')
    type = models.IntegerField(choices=PUBLICATION_TYPES, default=1)

    def __str__(self):
        return self.title