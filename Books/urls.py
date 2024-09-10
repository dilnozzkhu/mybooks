from django.urls import path
from . import views

app_name = 'Books'

urlpatterns = [
    path('', views.book_list, name='list'),
    path('book/<int:pk>', views.book_detail, name='detail')
]