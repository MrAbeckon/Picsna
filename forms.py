# from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms import ModelForm
from .models import Comment
from .models import DetailV

class AddImg(ModelForm):
	class Meta:
		model = DetailV
		fields = ['picture','title', 'link', 'author']

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['detail', 'author', 'content']
		