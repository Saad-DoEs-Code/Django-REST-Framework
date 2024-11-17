from django.urls import path
from . import views


urlpatterns = [
    # path('get', views.api_get, name='get_product'),
    # path('post', views.api_post, name='post_product'),
    path('',views.ProductCreateAPIView.as_view(),),
    path('<int:pk>/', views.ProductsDetailView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateView.as_view()),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view()),
    path('list/', views.ProductsListCreateView.as_view()),
    # """MADE FOR FUNCTION VIEWS"""
    # path('',views.get_or_post_product),
    # path('<int:pk>/', views.get_or_post_product),
    # path('list/', views.get_or_post_product),
]