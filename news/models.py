from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class News(models.Model):
    sarlavha = models.CharField(max_length=250)
    taglavha = models.CharField(max_length=550)
    asosoiy_matn = models.TextField()
    rasm = models.ImageField(upload_to="media/")
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.sarlavha)
        return super().save(*args, **kwargs)
