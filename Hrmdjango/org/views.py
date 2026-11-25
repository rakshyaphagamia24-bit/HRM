from django.shortcuts import render
from django.http import JsonResponse


def org_home(request):
    return JsonResponse({
        "status": "success",
        "message": "Organization API is working"
    })


def org_units(request):
    return JsonResponse({
        "status": "success",
        "message": "Organization units API is working",
        "data": []
    })
# Create your views here.
