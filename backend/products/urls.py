from django.urls import path
from . import views


urlpatterns = [
    # path('get', views.api_get, name='get_product'),
    # path('post', views.api_post, name='post_product'),
    path('<int:pk>/', views.ProductsDetailView.as_view())
]