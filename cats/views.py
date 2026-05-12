# from rest_framework import viewsets
# from .models import Cat
# from .serializers import CatSerializer

# # ModelViewSet provides default GET, POST, PUT, and DELETE actions.
# class CatViewSet(viewsets.ModelViewSet):
#     queryset = Cat.objects.all()
#     serializer_with = CatSerializer
#     serializer_class = CatSerializer


from rest_framework import viewsets
from .models import Cat
from .serializers import CatSerializer

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer