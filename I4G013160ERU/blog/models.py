from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(max_length=250)
    Author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

    def __init__(self) -> None:
        super().__init__()
        pass