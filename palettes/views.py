from rest_framework import generics
from .models import Palette
from .serializers import PaletteSerializer

class PaletteListCreate(generics.ListCreateAPIView):
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer

class PaletteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer
