from django.db import models

class Palette(models.Model):
    name = models.CharField(max_length=100)  
    colors = models.JSONField()
    
    class Meta:
        unique_together = ('name', 'colors')  
        
        
    def save(self, *args, **kwargs):
        if isinstance(self.colors, list):
            self.colors = [color.upper() for color in self.colors if isinstance(color, str)]
        elif isinstance(self.colors, dict):
            self.colors = {key: value.upper() if isinstance(value, str) else value for key, value in self.colors.items()}
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name