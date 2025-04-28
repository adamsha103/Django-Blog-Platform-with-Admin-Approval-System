
from django.db import models

class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Published', 'Published'),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
