from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from hardware_shop.models import Product, User, Order
from hardware_shop.serializers import ProductSerializer, UserSerializer, OrderSerializer


@csrf_exempt
def productApi(request, productId):
    if request.method == 'GET':
        try:
            product = Product.objects.get(productId=productId)
            product_serializer = ProductSerializer(product)
            return JsonResponse(product_serializer.data, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Product not found'}, status=404)

    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            product_serializer = ProductSerializer(data=data)
            if product_serializer.is_valid():
                product_serializer.save()
                return JsonResponse(product_serializer.data, status=201)
            else:
                return JsonResponse({'message': 'Invalid input'}, status=405)
        except ValidationError:
            return JsonResponse({'message': 'Invalid input'}, status=405)

    elif request.method == 'PUT':
        try:
            product = Product.objects.get(productId=productId)
            data = JSONParser().parse(request)
            product_serializer = ProductSerializer(product, data=data)
            if product_serializer.is_valid():
               product_serializer.save()
               return JsonResponse(product_serializer.data, status=200)
            else:
               return JsonResponse({'message': 'Invalid input'}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Product not found'}, status=404)

        except ValidationError:
            return JsonResponse({'message': 'Invalid input'}, status=400)

    elif request.method == 'DELETE':
        try:
            product = Product.objects.get(productId=productId)
            product.delete()
            return JsonResponse({'message': 'Product deleted successfully'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Invalid product value'}, status=400)


def userApi(request, userId):
    if request.method == 'GET':
        try:
            user = User.objects.get(userId=userId)
            user_serializer = UserSerializer(user)
            return JsonResponse(user_serializer.data, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'User not found'}, status=404)

    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user_serializer = UserSerializer(data=data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse(user_serializer.data, status=201)
            else:
                return JsonResponse({'message': 'Invalid input'}, status=405)
        except ValidationError:
            return JsonResponse({'message': 'Invalid input'}, status=405)

    elif request.method == 'PUT':
        try:
            user = User.objects.get(userId=userId)
            data = JSONParser().parse(request)
            user_serializer = UserSerializer(user, data=data)
            if user_serializer.is_valid():
               user_serializer.save()
               return JsonResponse(user_serializer.data, status=200)
            else:
               return JsonResponse({'message': 'Invalid input'}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Product not found'}, status=404)

        except ValidationError:
            return JsonResponse({'message': 'Invalid input'}, status=400)

    elif request.method == 'DELETE':
        try:
            user = User.objects.get(userId=userId)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Invalid userId'}, status=400)

