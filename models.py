from django.db import models
from django.contrib.auth.models import User

class DetailV(models.Model):
	picture 	= models.ImageField(upload_to='picsna/static/images/detail_view', blank=False)
	author 		= models.ForeignKey(User, on_delete = models.DO_NOTHING)
	title 		= models.CharField( max_length = 100 )
	link 		= models.CharField( max_length = 250 )
	date_added 	= models.DateTimeField('date added', auto_now_add=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	detail 		= models.ForeignKey(DetailV, on_delete=models.CASCADE, related_name='comments')
	author 		= models.ForeignKey(User, on_delete = models.DO_NOTHING)
	content 	= models.TextField()
	date_added 	= models.DateTimeField('date snaped', auto_now_add=True)
