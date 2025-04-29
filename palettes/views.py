from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Palette
from .serializers import PaletteSerializer
from .auth import CsrfExemptSessionAuthentication  # import the custom class
from rest_framework.authentication import BasicAuthentication

class PaletteListCreate(generics.ListCreateAPIView):
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

class PaletteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]





# from rest_framework import generics
# from .models import Palette
# from .serializers import PaletteSerializer

# class PaletteListCreate(generics.ListCreateAPIView):
#     queryset = Palette.objects.all()
#     serializer_class = PaletteSerializer

# class PaletteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Palette.objects.all()
#     serializer_class = PaletteSerializer
