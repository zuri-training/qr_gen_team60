

from rest_framework import serializers
from qr_generator.models import  QRCollection, UserCollection

class QRCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCollection
        fields = ('qr_user', 'id','url_to_qr_code', 'time_created', 'category', 'qr_code') #didn't add qr_code because the url is already there


class UserCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCollection
        fields = ('id', 'qr_collection', 'qr_user',)