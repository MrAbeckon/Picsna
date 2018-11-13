from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistration

def register(request):

	if request.method == 'POST':
		form = UserRegistration(request.POST)
		
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('login')
	else :
		form = UserRegistration()


	context = {
		'title': 'Register'
	}
	return render(request, 'users/register.html', {'form': form})

# CHANGED TO DJANGO.CONTRIB.AUTH.AUTH_VIEWS
def login(request):
	context = {
		'title': 'Login'
	}
	form = UserRegistration()
	return render(request, 'users/login.html', {'form': form})


