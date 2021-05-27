from django.db import models

# Create your models
class page(models.Model):
    title=models.CharField(max_length=123)
    description=models.TextField(max_length=760)
    img=models.ImageField(upload_to='field',default='1.jpg')

    def __str__(self):
        return self.title

class Slider_Images(models.Model):
    title=models.CharField(max_length=200)
    slide_image=models.ImageField(upload_to='banner')

    def __str__(self):
        return self.title