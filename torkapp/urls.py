from django.conf.urls import url

from torkapp import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^csvupload/', views.csvupload, name="csvupload"),
]