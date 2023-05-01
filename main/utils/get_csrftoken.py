import django
from django.http import JsonResponse


def getcsrftoken(request):
    res = {
        'csrftoken': django.middleware.csrf.get_token(request)
    }
    return JsonResponse(res)
