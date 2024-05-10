from django.db import models

# Create your models here.
class Website(models.Model):
    newsWebsiteName = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    link = models.TextField( blank=True, null=True)

    def __str__(self):
        return self.newsWebsiteName+' - '+self.category

class Article(models.Model):
    title = models.CharField(max_length=255,default="", blank=True, null=True)
    image = models.TextField(blank=True, default="",null=True)
    image_title = models.CharField(max_length=255,default="", blank=True, null=True)
    paragraphs = models.TextField(blank=True, default="", null=True)#required array
    publish_time = models.DateTimeField()
    author_name = models.CharField(max_length=255,default="", blank=True,null=True)
