from django.db.models import fields
from .models import Product
from rest_framework import serializers
from .models import Product

#! model based one


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        #fields = ['product_id', 'name']


#! simple
class MessageSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
