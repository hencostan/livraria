from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Editora, Autor, Livro
from core.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer, LivroSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer