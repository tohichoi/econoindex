from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from econoindex.serializers.importexport import ImportExportListView, ImportExportDetailView

urlpatterns = [
    path('importexport/', ImportExportListView.as_view()),
    path('importexport/<int:pk>/', ImportExportDetailView.as_view()),
    # path('', ImportExportListView.as_view(), name='import-export-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
