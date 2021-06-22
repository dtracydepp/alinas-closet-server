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


    def retrieve(self, request, pk=None):
        """Handle GET requests for single userpiece
        Returns:
            Response -- JSON serialized userpiece instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/userpieces/2
            #
            # The `2` at the end of the route becomes `pk`
            userpiece = UserPiece.objects.get(pk=pk)
            serializer = UserPieceSerializer(userpiece, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single userpiece
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            userpiece = UserPiece.objects.get(pk=pk)
            userpiece.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except UserPiece.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



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
