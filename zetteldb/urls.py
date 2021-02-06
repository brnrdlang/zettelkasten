from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<str:fid>/', views.zettel_thread, name='zettel_thread'),
  path('<str:fid>/<int:zid>/', views.zettel, name='zettel'),
  ]
