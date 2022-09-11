from rest_framework import mixins
from rest_framework import generics
from rest_framework.request import Request

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)