from rest_framework import serializers

from .models import Category, Keyword


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ["id", "word", "category"]


class CategorySerializer(serializers.ModelSerializer):
    keywords = KeywordSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "explanation", "next_steps", "keywords"]

class TriageRequestSerializer(serializers.Serializer):
            text = serializers.CharField(max_length=1000)