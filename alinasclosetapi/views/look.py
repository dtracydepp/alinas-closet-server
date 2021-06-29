from alinasclosetapi.models.look import Look
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers



class LookView(ViewSet):
   
 
    def list(self, request):
        """Handle GET requests to looks resource
        Returns:
        Response -- JSON serialized list of look
        """
        look = Look.objects.all()

         
        serializer = LookSerializer(
            look, many=True, context={'request': request})
        return Response(serializer.data) 




    def retrieve(self, request, pk=None):
        """Handle GET requests for single look
        Returns:
            Response -- JSON serialized look instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/looks/2
            #
            # The `2` at the end of the route becomes `pk`
            look = Look.objects.get(pk=pk)
            serializer = LookSerializer(look, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)



    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized look instance
        """

        # Uses the token passed in the `Authorization` header
        user = User.objects.get(user=request.auth.user)  

        # Create a new Python instance of the Look class
        # and set its properties from what was sent in the
        # body of the request from the client.
        look = Look()
        look.look_name = request.data["look_name"]
       
        

        # Try to save the new look to the database, then
        # serialize the look instance as JSON, and send the
        # JSON as a response to the client request
        try:
            look.save()
            serializer = LookSerializer(look, context={'request': request})
            return Response(serializer.data)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single look
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            look = Look.objects.get(pk=pk)
            look.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Look.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

   
    def update(self, request, pk=None):
        """Handle PUT requests for a look
        Returns:
            Response -- Empty body with 204 status code
        """
        look = Look.objects.get(pk=pk)
        
        look.look_name = request.data["look_name"]

        try:
            look.save()
        except ValidationError as ex:
            return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)

        return Response({}, status=status.HTTP_204_NO_CONTENT)     






class LookSerializer(serializers.ModelSerializer):
        """JSON serializer for looks
        Arguments:serializer type """
        class Meta:
            model = Look
            fields = ('id', 'look_name', 'note')
            depth = 1               
