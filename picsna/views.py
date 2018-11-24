from django.shortcuts import render
from django.contrib.auth.models import User
from .models import CompleteV
from .models import DetailV
from .forms import AddImg
from .forms import Complete


def play(request):
	context = {
		'detailViews': DetailV.objects.all(),
		# 'detailImgPath': 
		# 	[ 
		# 	  DetailV.objects.first().picture.name.split('/')[3], 
		# 	  DetailV.objects.second().picture.name.split('/')[3],
		# 	  DetailV.objects.third().picture.name.split('/')[3],
		# 	  DetailV.objects.last().picture.name.split('/')[3]
		# 	 ],
		'completeView': CompleteV.objects.last(),
		'title': 'Play',
		'user': User
	}
	return render(request, 'picsna/play.html', context)

def addImg(request):
	
	if request.method == 'POST':
		form = AddImg(request.POST)
		
		if form.is_valid():
			form.save()
			title = form.cleaned_data.get('title')
			messages.success(request, f'Detail view created: {title}!')
			return redirect('picsna-play')
	else:
		form = AddImg();

	context = {
		'title': 'Add your part of the Story',
	}
	return render(request, 'picsna/addImg.html', {'form' : form})