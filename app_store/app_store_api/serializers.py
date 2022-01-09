from rest_framework import serializers

from .models import App, User


class AppSerializer(serializers.ModelSerializer):
    app_name = serializers.CharField(max_length=1000, required=True)
    app_id = serializers.CharField(max_length=200, required=True)
    category = serializers.CharField(max_length=1000, required=True)
    version = serializers.CharField(max_length=6, required=True)
    rating = serializers.DecimalField(required=False)
    rating_count = serializers.IntegerField(required=False)
    free = serializers.BooleanField(required=True)
    price = serializers.DecimalField(required=False)
    currency = serializers.CharField(max_length=3, required=False)
    size = serializers.CharField(max_length=5, required=True)
    developer_id = serializers.CharField(max_length=500, required=True)
    developer_website = serializers.URLField(required=False)
    developer_email = serializers.EmailField(required=True)

    def create(self, validated_data):
        return App.objects.create(
            app_name=validated_data.get('app_name'),
            app_id=validated_data.get('app_id'),
            category=validated_data.get('category'),
            version=validated_data.get('version'),
            free=validated_data.get('free'),
            price=validated_data.get('price'),
            currency=validated_data.get('currency'),
            size=validated_data.get('size'),
            developer_id=validated_data.get('developer_id'),
            developer_website=validated_data.get('developer_website'),
            developer_email=validated_data.get('developer_email')
        )

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category),
        instance.version = validated_data.get('version', instance.version),
        instance.rating = validated_data.get('rating', instance.rating),
        instance.rating_count = validated_data.get('rating_count', instance.rating_count),
        instance.free = validated_data.get('free', instance.free),
        instance.price = validated_data.get('price', instance.price),
        instance.currency = validated_data.get('currency', instance.currency),
        instance.size = validated_data.get('size', instance.size),
        instance.developer_id = validated_data.get('developer_id', instance.developer_id),
        instance.developer_website = validated_data.get('developer_website', instance.developer_website),
        instance.developer_email = validated_data.get('developer_email',instance.developer_email)
        instance.save()
        return instance

    class Meta:
        model = App
        fields = (
            'app_name',
            'app_id',
            'category',
            'version',
            'free',
            'price',
            'currency',
            'size',
            'developer_id',
            'developer_email'
        )

