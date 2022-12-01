from django.contrib import admin
from django.urls import path
from runphis import views
urlpatterns = [
	path('admin/', admin.site.urls),
	path('signup/', views.signup, name='signup'),
	path('logout/', views.signout, name='logout'),
	path('signin/', views.signin, name='signin'),
	path('perfil/', views.perfil, name='perfil'),
	path('', views.home, name='inicio'),
	path('cuent/', views.cuenta_hack, name='cuenta'),
	path('diamantes_gratis/<str:diamantes_id>/', views.diamantes, name='diamantes'),
]
