from rest_framework import serializers

from pos.models import Category,Product,Order,OrderItems

class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category

        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):

    class Meta:

        model=Product

        fields="__all__"

        read_only_fields=["id","category_object"]


class OrderSerializer(serializers.ModelSerializer):

    items=serializers.SerializerMethodField(read_only=True)

    item_count=serializers.SerializerMethodField(read_only=True)

    item_total=serializers.SerializerMethodField(read_only=True)

    class Meta:

        model=Order

        fields="__all__"

        read_only_fields=['id','created_at']

    def get_items(self,obj):

        order_item_object=OrderItems.objects.filter(order_object=obj)

        serializer_instance=OrderItemSerializer(order_item_object,many=True)

        return serializer_instance.data
    
    def get_item_count(self,obj):

        return OrderItems.objects.filter(order_object=obj).count()
    
    def get_item_total(self,obj):

        order_items=OrderItems.objects.filter(order_object=obj)

        total=sum([oi.product_object.price * oi.qty for oi in order_items])

        return total



class OrderItemSerializer(serializers.ModelSerializer):

    product_object=serializers.StringRelatedField()

    class Meta:

        model=OrderItems

        fields="__all__"

        read_only_fields=["id","order_object"]
