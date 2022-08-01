# account/models.py

from django.db import models
from django.contrib.auth import get_user_model

# Todo: extend the base user model and override to __str__ method to return name
User = get_user_model()

class Category(models.Model):
    """Every Available category"""
    category_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'categories'


class QRCollection(models.Model):
    """All qr collections available"""
    qr_user = models.ForeignKey(User, on_delete=models.CASCADE, )
    url_to_qr_code = models.URLField(max_length=250, unique=True,)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    
    qr_code = models.ImageField(upload_to='upload/')
    qr_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.qr_user}\'s {self.category} QR'

    #? def save() override save method and cleanup qr_name before saving so it can be easily accesible

    class Meta:
        db_table = 'qr_collection'
        verbose_name_plural = 'qr_collections'

class UserCollection(models.Model):
    """A simple abstraction of the Collections for a user"""
    qr_user = models.OneToOneField(User, on_delete=models.CASCADE, )
    qr_collection = models.ForeignKey(QRCollection, on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.qr_user)

    class Meta:
        db_table = 'user_collection'
        verbose_name_plural = 'user_collections'

