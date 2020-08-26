from django.urls import path,re_path

from .views import(DashboardDeleteView,index,login, DashboardUpdateView, DashboardDetailView)
# from .views import IndexViewClass

urlpatterns = [
	path('delete/<int:pk>', DashboardDeleteView.as_view(), name='index_delete'),
	path('update/<int:pk>', DashboardUpdateView.as_view(), name='index_update'),
	path('', index, name='index'),
	# path('create/', DashboardCreateView, name='index_create'),

	path('detail/<int:pk>', DashboardDetailView.as_view(), name='index_detail')
	# path('create', DashboardCreateAndUpdateView.as_view(), name='index_create'),
	# path('', index,name='index'),
]