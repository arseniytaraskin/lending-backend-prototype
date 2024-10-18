from django.db import models

# Create your models here.

class ContentBlock(models.Model):
    BLOCK_TYPES = (
        ('text','Text'),
        ('image','Image'),
    )

    block_type = models.CharField(max_length=100, choices=BLOCK_TYPES)
    content = models.TextField(blank=True, null=True)
    order = models.IntegerField() #Для управления порядком блоков

    def __str__(self):
        return f"{self.block_type} - {self.order}"
