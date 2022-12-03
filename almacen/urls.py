from .views import CategoriasView
from django.urls import path


urlpatterns = [
  path('categorias', CategoriasView.as_view()),
]