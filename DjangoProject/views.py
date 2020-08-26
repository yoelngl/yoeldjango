from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

def loginView(request):
	user = None
	if request.method == "POST":
		username_login = request.POST['username']
		password_login = request.POST['password']
		user = authenticate(request, username=username_login, password=password_login)

		if user is not None:
			login(request, user)
			return redirect('adminView:index')
		else:
			return redirect('login')

	if request.method == "GET":
		print(request.user.is_authenticated)
		if request.user.is_authenticated:
			return redirect('adminView:index')
		else:
			return render(request, 'adminViews/login.html')

def logoutView(request):
	if request.method == "POST":
		logout(request)
		return redirect('login')

	return render(request, 'adminViews/logout.html')
