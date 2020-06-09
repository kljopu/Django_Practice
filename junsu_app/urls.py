from django.conf.urls import url
from junsu_app import views
from django.urls import path, include

app_name = 'junsu_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('', include('signup.urls')),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]