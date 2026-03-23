from django.urls import path
from .api_views.auth_view import CustomTokenView
from .api_views.user_view import RegisterUserAspView
from .api_views.registration_view import CompleteRegistrationView
from .api_views.application_view import (
    AcceptRejectApplicationView,
    ApplicationDetailView,
    ApprovedApplicationView,
    CorrectionApplicationView,
    UpdateApplicantApplicationView,
    ListApplicationsView
)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('auth/login/', CustomTokenView.as_view()),
    path('user/register/', RegisterUserAspView.as_view()),
    path('applications/', ListApplicationsView.as_view()),
    path('applications/<uuid:id>/approved/', ApprovedApplicationView.as_view()),
    path('applications/<uuid:id>/correction/', CorrectionApplicationView.as_view()),
    path('applications/<uuid:id>/resolve/', AcceptRejectApplicationView.as_view()),
    path('applications/<uuid:id>/update/', UpdateApplicantApplicationView.as_view()),
    path('applications/<uuid:id>/complete/', CompleteRegistrationView.as_view()),
    path('applications/<uuid:id>/', ApplicationDetailView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)