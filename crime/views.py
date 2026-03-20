from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from crime.models import Crime
from crime.serializers import CrimeSerializer   # fixed spelling

# GET all crimes
@api_view(['GET'])
def get_crimes(request):
    crimes = Crime.objects.all()
    serializer = CrimeSerializer(crimes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# POST new crime
@api_view(['POST'])
def add_crime(request):
    serializer = CrimeSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)