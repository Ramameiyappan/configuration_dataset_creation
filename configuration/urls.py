from django.urls import path
from .views import FileUploadAPIView, GetColumnsAPIView, ProcessAPIView

urlpatterns = [
    path('upload/', FileUploadAPIView.as_view()),
    path('columns/<int:file_id>/', GetColumnsAPIView.as_view()),
    path('process/', ProcessAPIView.as_view()),
]
