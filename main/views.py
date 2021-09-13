from rest_framework.generics import *
from main.models import Publication
from main.serializers import PublicationsListSerializer, PublicationDetailSerializer


class PublicationsListCreateView(ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationsListSerializer


class PublicationDetailView(RetrieveAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationsListSerializer




