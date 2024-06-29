from django.db import models

# Create your models here.
class Blog(models.Model):
    
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField()
    
    class Meta:
        db_table = 'blogs'
    
    def __str__(self):
        self.title