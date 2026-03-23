from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from ..services.registration_service import create_complete_registration

class CompleteRegistrationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        try:
            registration = create_complete_registration(
                application_id=id,
                data=request.data
            )

            return Response({
                "message": "Inscripción completada exitosamente",
                "registration_id": str(registration.id)
            }, status=status.HTTP_201_CREATED)

        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            return Response(
                {
                    "error": "Error interno del servidor",
                    "msg_error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )