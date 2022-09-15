from django.urls import path
from AppTwo import views

#template Tagging
app_name = 'basic_app'

urlpatterns = [
	#url(r'^$', views.help, name='help'),
	path('users/', views.user, name='users'),
	path('help/',views.help,name='help'),
	path('addbooks/',views.addbook_form,name='addbook_form'),
	path('displaybooks/',views.displaybook,name='displaybook'),
	path('deletebooks/',views.deletebook,name='deletebook'),
	path('register/',views.register,name='register'),
	path('user_login/',views.user_login,name='user_login'),
]
