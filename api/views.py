from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializers
from base.models import Item

@api_view(['GET'])
def getData(request):

    

    items = Item.objects.all()
    serializer = ItemSerializers(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

