"""View module for handling requests about categories"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from alinasclosetapi.models import Category, category


class CategoryView(ViewSet):

    def retrieve(self, request, pk=None):
        """Handle GET requests for single category
        Returns:
            Response -- JSON serialized category instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/pieces?category=1
            # The `1` at the end of the route becomes `pk`
                category = Category.objects.get(pk=pk)
                serializer = CategorySerializer(category, context={'request': request})
                return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    

    def list(self, request):
        """Handle GET requests to categories resource
        Returns:
            Response -- JSON serialized list of categories
        """
        categories = Category.objects.all()

        # Support filtering categories
        category = self.request.query_params.get('categoryId', None)
        if category is not None:
            categories = categories.filter(category__id=category)    

        serializer = CategorySerializer(
            categories, many=True, context={'request': request})
        return Response(serializer.data)


class CategorySerializer(serializers.ModelSerializer):
        """JSON serializer for categories
        Arguments:serializer type """
        class Meta:
            model = Category
            fields = ('id', 'category_name')
            depth = 1    