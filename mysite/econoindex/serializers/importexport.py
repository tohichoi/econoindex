from django.http import Http404
from rest_framework import serializers, status, viewsets, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from econoindex.models import ImportExport


class ImportExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportExport
        fields = ['id', 'timestamp', 'country', 'imp_count', 'imp_amount', 'exp_count', 'exp_amount', 'balance']

    # id = serializers.IntegerField(read_only=True)
    #
    # timestamp = serializers.IntegerField(read_only=True)
    # country = serializers.CharField(read_only=True)
    # # usd
    # imp_count = serializers.IntegerField(read_only=True)
    # imp_amount = serializers.IntegerField(read_only=True)
    # # usd
    # exp_count = serializers.IntegerField(read_only=True)
    # exp_amount = serializers.IntegerField(read_only=True)
    # # usd
    # balance = serializers.IntegerField(read_only=True)
    # note = serializers.CharField(style={'base_template': 'textarea.html'})

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return ImportExport.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instanceimportexport


class ImportExportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ImportExport.objects.all().order_by('-timestamp')
    serializer_class = ImportExportSerializer
    permission_classes = [permissions.IsAuthenticated]


class ImportExportListView(ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = ImportExport.objects.all()
    serializer_class = ImportExportSerializer

    # def get(self, request, format=None):
    #     snippets = ImportExport.objects.all()
    #     serializer = ImportExportSerializer(snippets, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = ImportExportSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImportExportDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    queryset = ImportExport.objects.all()
    serializer_class = ImportExportSerializer

    # def get_object(self, pk):
    #     try:
    #         return ImportExport.objects.get(pk=pk)
    #     except ImportExport.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk, format=None):
    #     obj = self.get_object(pk)
    #     serializer = ImportExportSerializer(obj)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk, format=None):
    #     obj = self.get_object(pk)
    #     serializer = ImportExportSerializer(obj, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     obj = self.get_object(pk)
    #     obj.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)