from django.db import models

class BlogPost(models.Model):
    """."""

    title = models.CharField(max_length=200)
    #title = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    """
    def __str__(self):
        #Return string BlogPost#docstring
        if len(self.title) < 50:
            return self.title
        return f"{self.title[:50]}..."
    """
