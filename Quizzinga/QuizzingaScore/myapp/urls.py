from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'/ajax_change_score/', views.ajax_change_score, name = 'ajax_change_score'),

    path('', views.index, name='index'),

    path('<int:quiz_id>/', views.detail, name = 'detail'),

    path('<int:quiz_id>/teams/<int:team_id>', views.results, name = 'results'),
]