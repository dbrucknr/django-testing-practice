import json
from django.http import JsonResponse
from django.core import serializers

def create(request):
    return JsonResponse({ 'create': 'created' })

def retrieve(request):
    return JsonResponse({ 'retrieve': 'retrieved' })

def update(request):
    return JsonResponse({ 'update': 'updated' })

def delete(request):
    return JsonResponse({ 'delete': 'deleted' })
