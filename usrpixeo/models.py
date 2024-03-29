from django.db import models
from uuid import uuid4
from PIL import Image
import rembg

class Images(models.Model):
    img_id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    optimized = models.BooleanField(default=False)
    remove_bg = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.optimized:
            img = Image.open(self.image.path)

            if img.mode in ("RGBA", "P"): 
                img = img.convert("RGB")
                
            img.save(self.image.path, 'JPEG', quality=85)
        if self.remove_bg:
            img = Image.open(self.image.path)
            output_img = rembg.remove(img)
            output_img.save(self.image.path, 'PNG')

