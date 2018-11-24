from django.forms import ModelForm
from .models import CompleteV
from .models import DetailV

class AddImg(ModelForm):
	class Meta:
		model = DetailV
		fields = ['picture', 'title', 'link']

class Complete(ModelForm):
	class Meta:
		model = CompleteV
		fields = ['picture', 'title', 'link', 'description']
		