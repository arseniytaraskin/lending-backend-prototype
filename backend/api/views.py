
from rest_framework import generics
from .models import ContentBlock
from .serializers import ContentBlockSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_content(request):
    data = {
        'message': 'Updated content from backend!'
    }
    return Response(data)

class ContentBlockList(generics.ListCreateAPIView):
    queryset = ContentBlock.objects.all().order_by('order')
    serializer_class = ContentBlockSerializer
