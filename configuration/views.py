import os
import pandas as pd
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UploadedFile
from .services import process_excel
from django.conf import settings
from .models import UploadedFile


class FileUploadAPIView(APIView):
    def post(self, request):
        if 'file' not in request.FILES:
            return Response(
                {"error": "No file received"},
                status=400
            )
        uploaded_file = request.FILES['file']
        obj = UploadedFile.objects.create(file=uploaded_file)

        return Response({
            "message": "File uploaded",
            "file_id": obj.id,
            "saved_path": obj.file.path
        })


class GetColumnsAPIView(APIView):
    def get(self, request, file_id):
        try:
            file_obj = UploadedFile.objects.get(id=file_id)
        except UploadedFile.DoesNotExist:
            return Response(
                {"error": "File not found"},
                status=404
            )

        if not os.path.exists(file_obj.file.path):
            return Response(
                {"error": "File missing on disk"},
                status=404
            )

        df = pd.read_excel(file_obj.file.path)
        return Response({
            "columns": list(df.columns)
        })

class ProcessAPIView(APIView):
    def post(self, request):
        file_id = request.data.get("file_id")
        config = request.data.get("config")

        if not file_id:
            return Response(
                {"error": "file_id is required"},
                status=400
            )

        if not config:
            return Response(
                {"error": "config is required"},
                status=400
            )

        try:
            file_obj = UploadedFile.objects.get(id=file_id)
        except UploadedFile.DoesNotExist:
            return Response(
                {"error": "File not found"},
                status=404
            )

        if not os.path.exists(file_obj.file.path):
            return Response(
                {"error": "File missing on disk"},
                status=404
            )

        df = process_excel(file_obj.file.path, config)
        output_path = os.path.join(settings.MEDIA_ROOT, f"output_{file_id}.xlsx")
        df.to_excel(output_path, index=False)

        return FileResponse(
            open(output_path, "rb"),
            as_attachment=True,
            filename="result.xlsx"
        )