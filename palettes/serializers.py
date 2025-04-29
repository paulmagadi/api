from rest_framework import serializers
from .models import Palette

class PaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields = ['id', 'name', 'colors']
    
    def validate_name(self, value):
        """Handle name conflicts by appending suffixes"""
        original_name = value
        counter = 1
        
        while Palette.objects.filter(name=value).exists():
            value = f"{original_name}-{counter}"
            counter += 1
            
        return value