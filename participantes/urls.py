from django.urls import path, include 
from . import views

urlpatterns = [
    path('participantes/create/', views.create_participante, name="create_participante"),
    path('participantes/lparticipantes', views.lparticipantes, name='lparticipantes'),
    path('participantes/<int:participante_id>/', views.form_detail, name='form_detail'),
    path('participantes/<int:participante_id>/delete', views.participante_eliminado, name='participante_eliminado'),
]