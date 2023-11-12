"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eventos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('eventos/', views.eventos, name='eventos'),
    path('eventos_completados/', views.eventos_completados, name='eventos_completados'),
    path('eventos/create/', views.create_evento, name='create_eventos'),
    path('eventos/<int:evento_id>/', views.evento_detail, name='evento_detail'),
    path('eventos/<int:evento_id>/complete', views.evento_completado, name='evento_completado'),
    path('eventos/<int:evento_id>/delete', views.evento_eliminado, name='evento_eliminado'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),       
]