from django.shortcuts import render
from .models import CompleteV
from .models import DetailV


def register(request):
	context = {
		'title': 'Register'
	}
	return render(request, 'picsna/register.html', context)

def login(request):
	context = {
		'title': 'Login'
	}
	return render(request, 'picsna/login.html', context)


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
		'title': 'Play'
	}
	return render(request, 'picsna/play.html', context)
