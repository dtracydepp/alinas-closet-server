"""View module for handling requests about pieces"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from alinasclosetapi.models import Piece, category


class PieceView(ViewSet):

    def list(self, request):
        """Handle GET requests to pieces resource
        Returns:
            Response -- JSON serialized list of pieces
        """

        # Get the current authenticated user
        # Left is variable , Right is ORM statement and request from client
        pieces = Piece.objects.all()

        # Support filtering pieces
         # Support filtering pieces by category
        #    http://localhost:8000/pieces?category=1
        #
        # That URL will retrieve all pieces
        category = self.request.query_params.get('id', None)
        if category is not None:
                pieces = pieces.filter(categoryId=category) 

        serializer = PieceSerializer(
            pieces, many=True, context={'request': request})
        return Response(serializer.data) 

    
    def retrieve(self, request, pk=None):
        """Handle GET requests for single piece
        Returns:
            Response -- JSON serialized piece instance
        """

          # Left is variable , Right is ORM statement and request from client
        try:
            piece = Piece.objects.get(pk=pk)
            serializer = PieceSerializer(piece, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

# Serializers -- Specifies what fields on the Model should be converted to JSON in the response

class PieceSerializer(serializers.ModelSerializer):
        """JSON serializer for pieces
        Arguments:serializer type """
        class Meta:
            model = Piece
            fields = ('id', 'piece_name', 'size', 'imageurl','price','retailer','category')
            depth = 1    