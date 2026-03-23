from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..services.user_service import create_pre_registration

class RegisterUserAspView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        try:
            result = create_pre_registration(request.data)

            return Response({
                "message": "Pre-inscripción realizada exitosamente!",
                "application_id": result["application"].id
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