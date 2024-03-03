from django.urls import path
from .views import login, logout, sendIndex, query

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('sendIndex/', sendIndex, name='sendIndex'),
    path('query/', query, name='query'),
]
