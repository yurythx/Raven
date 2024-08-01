from django.urls import path
from blog import views

urlpatterns = [

    path('', views.PostIndex.as_view(), name='blog_index'),
    path('categoria/<str:categoria>', views.PostCategoria.as_view(), name='post_categoria'),
    path('busca/', views.PostBusca.as_view(), name='post_busca'),
    path('novo/', views.PostCreate.as_view(), name='novo-post'),
    path('update/<int:pk>', views.PostUpdateView.as_view(), name='update-post'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name='delete-post'),
    path('post/<int:pk>', views.PostDetalhes.as_view(), name='post_detalhes'),
    

]