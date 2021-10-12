from django.db import models


class News(models.Model):
   image = models.ImageField(upload_to='static_image')
