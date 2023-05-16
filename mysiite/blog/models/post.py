from django.db import models
from django.contrib.auth.models import User
STATUS =(
    (0,'Draft')
    (1,'Publish'),
)




class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog-posts')
    updated_on = models.DateTimeFiedld(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeFiedld(auto_now_Add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def _str_(self):
        return self.title
