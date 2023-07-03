from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """."""

    title = models.CharField(max_length=200)
    #title = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    """
    Ve bu?
    def __str__(self):
        #Return string BlogPost#docstring
        if len(self.text) < 50:
            return self.text
        return f"{self.text[:50]}..."
    """

"""
Bunlar ne ayak
class Meta:
    #verbose_name_plural = 'posts'
    
    def __str__(self):
        #Return string BlogPost#docstring
        if len(self.text) < 50:
            return self.text
        return f"{self.text[:50]}..."
"""