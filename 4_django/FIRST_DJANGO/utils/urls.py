from django.urls import path
from . import views
urlpatterns = [
    path('', views.index), #utils/
    path('art/<str:keyword>/', views.art_text), #utils/art/<KEYWORD>
    path('stock', views.stock), #utils/stock
]