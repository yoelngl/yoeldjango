from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import Hajime
from .forms import PostForm
from django.views.generic.base import TemplateView,RedirectView,View
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
	introduce = Hajime.objects.all()
	error = ''
	form = PostForm(request.POST)
	paginator = Paginator(introduce, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)


	if request.method == 'POST':
		HajimeForm = Hajime(request.POST)

		# Hajime.objects.create(
		# 		name = request.POST.get('name'),
		# 		description = request.POST.get('description'),
		# )
		# if HajimeForm.is_valid():
		# 	post = HajimeForm.save()

		# 	post.save()
		# 	return redirect('adminview:index')
	if request.method == 'POST':

		if form.is_valid():
			form.save()

			return redirect('adminView:index')

		else:
			error = form.errors


	context = {
		'perkenalan': introduce,
		'form' : PostForm,
		'error':error,
		'page_obj':page_obj
	}

	return render(request, 'adminViews/index.html', context)


# class DashboardCreateView(CreateView):
# 	form_class = PostForm
# 	template_name = 'adminViews/index.html'



# def delete(request,id):
# 	Hajime.objects.filter(id=id).delete()
# 	return redirect('adminView:index')

# def update(request,id):
# 	introduce = Hajime.objects.all()
# 	data_db = Hajime.objects.get(id=id)
# 	data = {
# 		'name': data_db.name,
# 		'description': data_db.description,
# 		'majors': data_db.majors
# 	}
# 	error = ''
# 	form = PostForm(request.POST or None, initial=data, instance=data_db)

# 	if request.method == 'POST':
# 		if form.is_valid():
# 			form.save()

# 			return redirect('adminView:index')
			

# 		else: 
# 			error = form.errors


# 	context = {
# 		'perkenalan': introduce,
# 		'forms' : form,
# 		'error':error,
# 	}


# 	return render(request, 'adminViews/index.html', context)

# class IndexViewClass(View):
# 	introduce = Hajime.objects.all()
# 	form = PostForm()
# 	template_name = 'adminViews/index.html'

# 	def get(self,request):
# 		context = {
# 			'perkenalan': self.introduce,
# 			'forms': self.form
# 		}
# 		return render(request, 'adminViews/index.html', context)

# 	def post(self,request):
# 		form = PostForm(request.POST or None)

# 		if request.method == 'POST':
# 			if form.is_valid():
# 				form.save()
				
# 				return redirect('adminView:index')


# 		context = {
# 			'perkenalan': self.introduce,
# 			'form': form
# 		}
# 		return render(request, self.template_name, context)

# class DashboardView(ListView):
# 	template_name = 'adminViews/index.html'
# 	model = Hajime
# 	extra_context = {
# 		'forms': PostForm(),
# 	}
# 	paginate_by = 5
# 	def get_context_data(self, *args, **kwargs):
# 		self.kwargs.update(self.extra_context)
# 		kwargs = self.kwargs
# 		return super().get_context_data()
	# template_name = 'adminViews/index.html'
	# context = {}
	# form = None
	# introduce = Hajime.objects.all()

	# def get(self, *args, **kwargs):
	# 	self.context = {
	# 		'forms': PostForm(),
	# 		'perkenalan': self.introduce
	# 	}
	# 	return render(self.request, self.template_name, self.context)

	# def post(self, *args, **kwargs):
	# 	self.form = PostForm(self.request.POST or None)
	# 	print(self.request.POST)	

	# 	if self.form.is_valid():
	# 		self.form.save()
	# 		return redirect('adminView:index')


class DashboardDeleteView(RedirectView):
	pattern_name = 'adminView:index'

	def get_redirect_url(self, *args, **kwargs):
		id = kwargs['pk']
		print(id)
		Hajime.objects.filter(id=id).delete()
		return super().get_redirect_url()

# class DashboardCreateAndUpdateView(View):
# 	content = None
# 	form = PostForm()
# 	introduce = Hajime.objects.all()
# 	template_name = 'adminViews/index.html'
# 	context = {}
# 	content = None
# 	paginator = None
# 	page_number = None
# 	page_obj = None

# 	def get(self, *args, **kwargs):
# 		if self.content == 'update':
# 			id = kwargs['id']
# 			formDB = Hajime.objects.get(id=id)
# 			data = formDB.__dict__
# 			self.form = PostForm(initial=data, instance=formDB)
# 			self.paginator = Paginator(self.introduce, 5)
# 			self.page_number = self.request.GET.get('page')
# 			self.page_obj = self.paginator.get_page(self.page_number)

# 		self.context = {
# 			'forms' : self.form,
# 			'page_obj': self.page_obj
# 		}
# 		return render(self.request, self.template_name, self.context)

# 	def post(self, *args, **kwargs):
# 		if kwargs.__contains__('id'):
# 			id = kwargs['id']
# 			formDB = Hajime.objects.get(id=id)
# 			self.form = PostForm(self.request.POST, instance=formDB)
# 		else:
# 			self.form = PostForm(self.request.POST)

# 		if self.form.is_valid():
# 			self.form.save()


# 		return redirect('adminView:index')

class DashboardUpdateView(UpdateView):
	form_class = PostForm
	model = Hajime
	introduce = Hajime.objects.all()
	template_name = 'adminViews/index.html'
	paginator = None
	page_number = None
	page_obj = None

	def get_context_data(self, *args, **kwargs):
		self.paginator = Paginator(self.introduce, 5)
		self.page_number = self.request.GET.get('page')
		self.page_obj = self.paginator.get_page(self.page_number)

		context = super().get_context_data()
		context['page_obj'] = self.page_obj
		return context

	
# class DashboardDeleteView(DeleteView):
# 	model = Hajime
# 	template_name = 'adminViews/index.html'
# 	success_url = reverse_lazy('adminView:index')


class DashboardDetailView(DetailView):
	template_name = 'adminViews/detail_index.html'
	model = Hajime



