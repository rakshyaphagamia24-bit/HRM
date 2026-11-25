from django.shortcuts import render
from django.http import JsonResponse


def health_check(request):
    return JsonResponse({
        "status": "success",
        "message": "Workforce API is running",
        "version": "v1"
    })
# Create your views here.
