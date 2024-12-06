from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(default = 'pic.jpg')
    alt_text = models.CharField(max_length=200)

    def __str__(self):
        return self.alt_text


class Link(models.Model):
    links = models.URLField(max_length=200, blank=True)
    def __str__(self):
        return str(self.id)

class Text(models.Model):
    title = models.CharField(max_length=2000, blank=True, null=True) 
    subtext = models.CharField(max_length=200, blank=True, null=True)
    paragraph = models.CharField(max_length=200,blank=True, null=True)

    def __str__ (self):
        return str(self.id)



