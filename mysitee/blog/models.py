from django.db import models

# Create your models here.

class Post(models.Model):
	title=models.CharField(max_length=200)
	text=models.TextField()
	posttime=models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True, related_name='allpost')

	def __str__(self):
	    return self.title

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
