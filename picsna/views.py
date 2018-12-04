from django.shortcuts import render, redirect
from django.core.files.uploadedfile import SimpleUploadedFile
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
		'user': request.user
	}
	return render(request, 'picsna/play.html', context)

def addImg(request):

	if request.method == 'POST':

		form = AddImg(request.POST, request.FILES) 
        # form = super(AddImg, self).save(commit=False)
        # form.author = request.user

		if form.is_valid():
			form.save()			
		else:
			print("Invalid Form")	

		return redirect('picsna-play')
			
	else:
		form = AddImg();

	return render(request, 'picsna/addImg.html', {'form' : form })