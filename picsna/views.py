from django.shortcuts import render, redirect
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Comment
from .models import DetailV
from .forms import AddImg
from .forms import CommentForm
from PIL import Image

# is_checked = IntVar()

def play(request):
	context = {
		'detailViews': DetailV.objects.all(),
		'title': 'Play',
		'user': request.user,
	}
	
	return render(request, 'picsna/play.html', context)

def addImg(request):

	if request.method == 'POST':
		form = AddImg(request.POST, request.FILES) 
		if form.is_valid():
			form.save()			
		else:
			print("Invalid Form")	

		return redirect('picsna-play')		
	else:
		form = AddImg();

	return render(request, 'picsna/addImg.html', {'form' : form })

def detail(request, detail_id):

	# FORM MANIPULATION FOR COMMENT
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save()			
		else:
			print("Invalid Form")	
	
	form = CommentForm(initial={'detail': DetailV.objects.get(id=detail_id)})

	context = {
		'title': 'Detail',
		'detail': DetailV.objects.get(id=detail_id),
		'comments': Comment.objects.filter(detail=detail_id),
		'user': request.user,
		'form': form,
	}

	return render(request, 'picsna/detail.html', context)