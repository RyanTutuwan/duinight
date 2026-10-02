from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='tracker.index'),
    path('increment/<int:participant_id>/<str:field>/', views.increment, name='tracker.increment'),
    path('decrement/<int:participant_id>/<str:field>/', views.decrement, name='tracker.decrement'),
    path('remove/<int:participant_id>/', views.remove, name='tracker.remove'),
    path('removeAll/', views.removeAll, name='tracker.removeAll'),
    path('currentWinner/', views.currentWinner, name='tracker.currentWinner'),
    path('currentTicketer/', views.currentTicketer, name='tracker.currentTicketer'),
    path('currentPisser/', views.currentPisser, name='tracker.currentPisser'),
]