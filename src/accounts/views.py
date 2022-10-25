from django.http import JsonResponse

def create(request):
    return JsonResponse({ 'create': 'created' })

def retrieve(request):
    return JsonResponse({ 'retrieve': 'retrieved' })

def update(request):
    return JsonResponse({ 'update': 'updated' })

def delete(request):
    return JsonResponse({ 'delete': 'deleted' })
