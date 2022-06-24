from django.db import models
from django.contrib.auth import get_user_model
#from django.conf import settings

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length = 200)
    Text = models.TextField
    Author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, null=True)
    Created_on = models.DateTimeField(auto_now_add=True)
    Published_on = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        #return self.Title, self.Text,self.Author,self.Created_on,self.Published_on
        return (f'Post Title is "{self.Title}" written by {self.Author} created on {self.Created_on} and publlished on {self.Published_on}.')