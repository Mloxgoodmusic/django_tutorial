from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    #ex: /polls/5/
    path('<int:question_id>/', views.details, name='details'),
    #ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='details'),
    #ex: /pollls/5/votes/
    path('<int:question_id>/votes/', views.vote, name='details')
]