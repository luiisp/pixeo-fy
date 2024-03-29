from django.db import models
from uuid import uuid4

class Images(models.Model):
    img_id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    optimized = models.BooleanField(default=True)
    remove_bg = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
