from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .logic import find_category
from .models import Category, Keyword
from .serializers import (
    CategorySerializer,
    KeywordSerializer,
    TriageRequestSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class TriageView(APIView):
    def post(self, request):
        serializer = TriageRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data["text"]

        category = find_category(text)

        if category is None:
            return Response({
                "category": None,
                "message": "We couldn't match your question to a topic.",
            })

        return Response({
            "category": category.name,
            "explanation": category.explanation,
            "next_steps": category.next_steps,
        })