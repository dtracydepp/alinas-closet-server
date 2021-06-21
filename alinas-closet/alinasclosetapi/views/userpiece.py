from django.contrib.auth.models import User, Piece
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers


class UserPieceView(ViewSet):
   
 
    def list(self, request):
        """Handle GET requests to userpieces resource
        Returns:
        Response -- JSON serialized list of userpieces
        """
        # Get the current authenticated user
        user = User.objects.get(user=request.auth.user)
        pieces = Piece.objects.filter(user=user)    

         

        serializer = PieceSerializer(
            pieces, many=True, context={'request': request})
        return Response(serializer.data) 



class PieceSerializer(serializers.ModelSerializer):
        """JSON serializer for pieces
        Arguments:serializer type """
        class Meta:
            model = Piece
            fields = ('id', 'piece_name', 'size', 'imageurl','price','retailer','category')
            depth = 1   
