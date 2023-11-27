from django.urls import path, include 
from . import views


urlpatterns = [

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