from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductVariant
from .serializers import ProductSerializer, ProductVariantSerializer

class BulkProductInsert(APIView):
    def post(self, request):
        product_data = request.data.get('products')
        if not product_data:
            return Response({'message': 'No products provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        product_serializer = ProductSerializer(data=product_data, many=True)
        if product_serializer.is_valid():
            products = product_serializer.save()
            
            # Handle file uploads
            for product in products:
                product_image = request.FILES.get(f'image_{product.id}')  
                if product_image:
                    product.image = product_image
                    product.save()

            variant_data = []
            for product in products:
                for variant in product.get('variants', []):
                    variant['product'] = product.id
                    variant_data.append(variant)
            
            variant_serializer = ProductVariantSerializer(data=variant_data, many=True)
            if variant_serializer.is_valid():
                variant_serializer.save()
                return Response({'message': 'Products and variants inserted successfully'}, status=status.HTTP_201_CREATED)
            else:
                Product.objects.filter(id__in=[product.id for product in products]).delete()
                return Response(variant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
