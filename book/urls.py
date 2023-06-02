from django.urls import path,include

from . import views
app_name ='book'
urlpatterns = [
    
    path('<int:pk>/', views.detail, name='detail'),
    # path('<int:pk>/', views.delete, name='delete'),
    path('new/', views.new, name='new'),
    
    path('<int:pk>/delete/', views.delete, name = 'delete' ),
    path('<int:pk>/edit/', views.edit, name = 'edit' ),
    path('', views.books, name = 'books' ),
    
    
]

