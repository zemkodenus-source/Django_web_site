from django.urls import path
from . import views

urlpatterns = [
    path('create_link/', views.create_link, name='create_link'),
    path('my_links/', views.my_links, name='my_links'),
    path('detail_link/<int:pk>/', views.LinkDetailView.as_view(), name='detail_link'),
    path('update_link/<int:pk>/', views.LinkUpdateView.as_view(), name='update_link'),
    path('delete_link/<int:pk>/', views.LinkDeleteView.as_view(), name='delete_link'),
    path('users_links/', views.LinksListView.as_view(), name='users_links'),
]