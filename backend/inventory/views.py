from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Product
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class InventoryView(View):
    
    def get(self, request):
        objects = list(Product.objects.values())
        return JsonResponse( objects, safe=False )
    
    def post(self, request):
        return JsonResponse({'post':'Ok post method!'})

    def put(self, request):
        return JsonResponse({'put':'Ok put method!'})

    def delete(self, request):
        return JsonResponse({'delete':'Ok delete method!'})