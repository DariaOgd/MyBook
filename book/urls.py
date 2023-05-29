from django.urls import path,include

from . import views
app_name ='book'
urlpatterns = [
    
    path('<int:pk>/', views.detail, name='detail'),
    
    # path('<int:pk>/delete/', views.delete, name = 'delete' ),
    
]

