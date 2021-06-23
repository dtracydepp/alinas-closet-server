from alinasclosetapi.models.user_piece import UserPiece
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from django.http import HttpResponse
from django.core.exceptions import ValidationError
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


    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized piece instance
        """

        # Uses the token passed in the `Authorization` header
        userpiece = UserPiece()

        # Create a new Python instance of the Piece class
        # and set its properties from what was sent in the
        # body of the request from the client.
        userpiece.piece = Piece.objects.get(pk=request.data["piece"])
        userpiece.user = request.auth.user
        userpiece.note = request.data.get("note", None)
        userpiece.is_favorite = request.data["is_favorite"]
        userpiece.look_id = request.data.get("look",None)
        userpiece.shopping_list_id = request.data.get("shopping_list", None)
        
        

        # Try to save the new piece to the database, then
        # serialize the look instance as JSON, and send the
        # JSON as a response to the client request
        try:
            userpiece.save()
            serializer = PieceSerializer(userpiece, context={'request': request})
            return Response(serializer.data)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


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


    def update(self, request, pk=None):
        """Handle PUT requests for a userpiece
        Returns:
            Response -- Empty body with 204 status code
        """
        userpiece = UserPiece.objects.get(pk=pk)
        
        userpiece.piece = Piece.objects.get(pk=request.data["piece"])
        userpiece.user = request.auth.user
        userpiece.note = request.data.get("note", None)
        userpiece.is_favorite = request.data["is_favorite"]
        userpiece.look_id = request.data.get("look",None)
        userpiece.shopping_list_id = request.data.get("shopping_list", None)
        

        try:
            userpiece.save()
        except ValidationError as ex:
            return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)

        return Response({}, status=status.HTTP_204_NO_CONTENT)        



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
            fields = ('id', 'note', 'is_favorite', 'piece', 'user','look','shopping_list')
            depth = 1 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'id']