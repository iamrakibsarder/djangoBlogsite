from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    content = RichTextUploadingField ()
    featured_img = models.ImageField(upload_to='uploads/', null=True, blank=True)
    tags = TaggableManager(blank=True)
    popular = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True)
    mod_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)