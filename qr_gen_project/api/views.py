from django.shortcuts import render
from qr_generator  import models
from django.http import JsonResponse
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# TODO: Remember to clean up this code later using DRY

@api_view(['GET']) # define it well later
def all(request, format=None):
    qr = QRCollection.objects.all() # get all collections
    qr_serializer = QRCollectionSerializer(qr, many=True) # serialize them
    return Response(qr_serializer.data) # return json

@api_view(['GET'])
def get_all_user_qr(request, pk, format=None):
    try:
        qr_user = QRCollection.objects.filter(qr_user=pk)

    except QRCollection.DoesNotExist:
        return JsonResponse({"message":"The user does not exist"})

    serializer = QRCollectionSerializer(qr_user, many=True)
    return Response(serializer.data,)


@api_view(['POST'])
def send_qr(request, ):
    if request.method == 'POST':
        serializer = QRCollectionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): # Raising Exceptions help the client know where the error is coming from
            serializer.save()
            print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)



@api_view(['GET'])
def get_qr_from_category(request, pk, category):
    try:
        qr_user = QRCollection.objects.filter(qr_user=pk, category=category)

    except QRCollection.DoesNotExist:
        return JsonResponse({"message":"The user does not exist"})

    serializer = QRCollectionSerializer(qr_user, many=True)
    return Response(serializer.data,)


@api_view(['POST'])
def get_one_qr(request, pk, category, item):
    try:
        qr_user = QRCollection.objects.get(qr_user=pk, category=category, qr_code=item)

    except QRCollection.DoesNotExist:
        return JsonResponse({"message":"The item does not exist"})

    serializer = QRCollectionSerializer(qr_user, many=True)
    return Response(serializer.data,)



@api_view(['DELETE'])
def delete_one_qr(request, pk, category, item_name):
    try:
        qr_list = QRCollection.objects.filter(qr_user=pk, category=category)
        # Build logic to delete

    except QRCollection.DoesNotExist:
        return JsonResponse({"message":"Bad Request"})

    serializer = QRCollectionSerializer(qr_list, many=True)
    return Response(serializer.data,)
    