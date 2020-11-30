from django.urls import path

from mainapp import views
from mainapp.views import buy, detail, results, vote

urlpatterns = [
    path ('buy/', buy),
    #path('', views.index, name='index'),

    path('<int:question_id>/', detail, name='detail'),

    path('<int:question_id>/results/', results, name='results'),

    path('<int:question_id>/vote/', vote, name='vote'),
]