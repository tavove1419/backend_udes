from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..services.application_service import (
    accept_reject,
    approved,
    correction,
    update_applicant,
    list_applications
)
from ..services.application_service import get_application_full
from ..serializers import ApplicationFullSerializer
from ..models import Application
from ..serializers import ApplicationListSerializer


class ApprovedApplicationView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, id):
        application = Application.objects.get(id=id)
        approved(
            application=application,
            user=request.user,
            observation=request.data.get('observation')
        )
        return Response({"message": "Aprobado correctamente"}, status.HTTP_201_CREATED)


class CorrectionApplicationView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, id):
        application = Application.objects.get(id=id)
        correction(
            application=application,
            user=request.user,
            observation=request.data.get('observation')
        )
        return Response({"message": "Actualización realizada correctamente"})


class AcceptRejectApplicationView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, id):

        application = Application.objects.get(id=id)
        accept_reject(
            application=application,
            user=request.user,
            status=request.data.get('status'),
            observation=request.data.get('observation')
        )

        return Response({"message": "Proceso finalizado"})
    

class UpdateApplicantApplicationView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, id):

        application = Application.objects.get(id=id)

        update_applicant(
            applicant=application,
            user=request.user,
            data=request.data
        )
        return Response({"message": "Actualización exitosa!"})

class ListApplicationsView(APIView):

    permission_classes = [IsAuthenticated]
    def get(self, request):
        filters = {"user_id": request.query_params.get("user_id")}
        applications = list_applications(filters)
        serializer = ApplicationListSerializer(applications, many=True)
        return Response(serializer.data)

class ApplicationDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        application = get_application_full(id)

        serializer = ApplicationFullSerializer(
            application,
            context={'request': request}
        )

        return Response(serializer.data, status=status.HTTP_200_OK)