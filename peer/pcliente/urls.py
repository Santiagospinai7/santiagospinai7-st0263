from django.urls import path
from .views import login, logout, send_index, query

urlpatterns = [
  path('login/', login, name='login'),
  path('logout/', logout, name='logout'),
  path('send_index/', send_index, name='send_index'),
  path('query/', query, name='query'),
]
