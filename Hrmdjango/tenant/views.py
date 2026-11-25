from django.shortcuts import render
from django.http import JsonResponse


def tenant_list(request):
    return JsonResponse({
        "status": "success",
        "message": "Tenant API is working",
        "data": []
    })
# Create your views here.
