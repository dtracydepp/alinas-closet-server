from alinasclosetapi.models.user_piece import UserPiece
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from alinasclosetapi.models import Piece


class UserPieceView(ViewSet):
   
 
    def list(self, request):
        """Handle GET requests to userpieces resource
        Returns:
        Response -- JSON serialized list of userpieces
        """
        # Get the current authenticated user
        user = request.auth.user
        userpiece = UserPiece.objects.filter(user=user)   
        # piece = Piece.objects.filter() 

         

        serializer = UserPieceSerializer(
            userpiece, many=True, context={'request': request})
        return Response(serializer.data) 



class PieceSerializer(serializers.ModelSerializer):
        """JSON serializer for pieces
        Arguments:serializer type """
        class Meta:
            model = Piece
            fields = ('id', 'piece_name', 'size', 'imageurl','price','retailer','category')
            depth = 1   

class UserPieceSerializer(serializers.ModelSerializer):
        """JSON serializer for pieces
        Arguments:serializer type """
        class Meta:
            model = UserPiece
            fields = ('id', 'note', 'is_favorite', 'piece','user','look','shopping_list')
            depth = 1 
