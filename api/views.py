from django.http import JsonResponse


def health(request):
    return JsonResponse({
        "status": "ok",
        "version": "2"
    })