from alinasclosetapi.models.shopping_list import ShoppingList
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from django.http import HttpResponse



class ListView(ViewSet):
   
 
    def list(self, request):
        """Handle GET requests to shopping lists resource
        Returns:
        Response -- JSON serialized list of userpieces
        """
        list = ShoppingList.objects.all()

         
        serializer = ListSerializer(
            list, many=True, context={'request': request})
        return Response(serializer.data) 




    def retrieve(self, request, pk=None):
        """Handle GET requests for single list
        Returns:
            Response -- JSON serialized list instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/lists/2
            #
            # The `2` at the end of the route becomes `pk`
            list = ShoppingList.objects.get(pk=pk)
            serializer = ListSerializer(list, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)



    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized list instance
        """

        # Uses the token passed in the `Authorization` header
        user = User.objects.get(user=request.auth.user)  

        # Create a new Python instance of the Look class
        # and set its properties from what was sent in the
        # body of the request from the client.
        list = ShoppingList()
        list.list_name = request.data["list_name"]
       
        

        # Try to save the new list to the database, then
        # serialize the look instance as JSON, and send the
        # JSON as a response to the client request
        try:
            list.save()
            serializer = ListSerializer(list, context={'request': request})
            return Response(serializer.data)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single list
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            list = ShoppingList.objects.get(pk=pk)
            list.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ShoppingList.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        """Handle PUT requests for a list
        Returns:
            Response -- Empty body with 204 status code
        """
        list = ShoppingList.objects.get(pk=pk)
        
        list.list_name = request.data["list_name"]

        try:
            list.save()
        except ValidationError as ex:
            return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)

        return Response({}, status=status.HTTP_204_NO_CONTENT)     






class ListSerializer(serializers.ModelSerializer):
        """JSON serializer for looks
        Arguments:serializer type """
        class Meta:
            model = ShoppingList
            fields = ('id', 'list_name', 'note', 'is_favorite')
            depth = 1    