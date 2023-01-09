# from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
# import json
# from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
# Create your views here.
@api_view(['POST',])
def api_home(request, *args, **kwargs):
    # data = request.data # this returns json data that send through endpoint
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True): # raise exception uses if i send invalid data 
        # instance = serializer.save()
        # instance is the object that created in database from serializer calss 
        # data = serializer.data # this returns data that pass from endpoint through serializer class
        # print(data == request.data) # False as data that returned from serializer may carry null and/or blank fields
        # print(instance)
        print(serializer.data)
        return Response(serializer.data)
    return Response({"statuts":"invalid data"}, status=400)

# @api_view(['GET',])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
#         # print(instance.title)
#         # data = model_to_dict(instance, fields=['id','title','content','price','sale_price']) # we replace this step by creating a serializers.py
#         # model instance (model_data) 
#         # turns into python dict
#         # and return in JSON format
#     return Response(data)
#     # json_data_str = json.dumps(data)        

#     # return HttpResponse(json_data_str) # in case JsonResponse 'Content-Type': 'application/json',  --  in case HttpResponse 'Content-Type': 'text/html;


# _______________________________________________________________________________________________________


# def api_home(request, *args, **kwargs):
#     # request is a instance from HttpRequest --> django
#     body = request.body
#     data = {}
#     try:
#         data = json.loads(body) # turns request in json in string format into python dictionary
#     except:
#         pass
#     # print(body) # print dictionary as string b'{"key":"value"}'
#     print(request.GET) # to print request params that have send in endpoint 
#     print(request.POST) # to print object that have created through endpoint
#     print(data.keys()) # print dictionary as string b'{"key":"value"}'
#     data['content_type']=request.content_type
#     # json.dumps(request.headers) return with json format 
#     # json.dumps((dict(request.headers)) return with python dictionary format 
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     print(data)
#     return JsonResponse(data)
