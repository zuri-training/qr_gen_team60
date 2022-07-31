# account/models.py

import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'categories'


class QRCollection(models.Model):
    qr_user = models.ForeignKey(User, on_delete=models.CASCADE, )
    url_to_qr_code = models.URLField(max_length=250, unique=True,)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(upload_to='upload/')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'qr_collection'
        verbose_name_plural = 'qr_collections'

class UserCollection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    qr_user = models.ForeignKey(User, on_delete=models.CASCADE, )
    qr_collection = models.ForeignKey(QRCollection, on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.qr_user)

    class Meta:
        db_table = 'user_collection'
        verbose_name_plural = 'user_collections'

