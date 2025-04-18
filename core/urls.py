from datetime import datetime, timedelta

from django.conf import settings
from django.conf.urls import include, url
from django.contrib.gis import admin

from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from users.views import (
    MyTokenObtainPairView
)

class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()

# Feedbacks app

from feedbacks.views import (
    ComplaintViewSet,
    SurveyQuestionViewSet,
    SurveyAnswerViewSet,
    FeedbackViewSet
)

complaints_router = router.register(
    'complaints', ComplaintViewSet
)
survey_questions_router = router.register(
    'survey-questions', SurveyQuestionViewSet
)
survey_answers_router = router.register(
    'survey-answers', SurveyAnswerViewSet
)
feedbacks_router = router.register(
    'feedbacks', FeedbackViewSet
)

# Organisations app

from organisations.views import (
    OrganisationViewSet
)

organisations_router = router.register(
    'organisations', OrganisationViewSet
)

# Tickets app

from tickets.views import (
    TicketViewSet,
    ActionViewSet
)

tickets_router = router.register(
    'tickets', TicketViewSet
)
actions_router = router.register(
    'actions', ActionViewSet
)

# Users app

from users.views import (
    CustomUserViewSet
)

users_router = router.register(
    'users', CustomUserViewSet
)

urlpatterns = [
    url(r'v1/', include(router.urls)),
    url(r'auth/', include('rest_auth.urls')),
    url(r'auth/registration/', include('rest_auth.registration.urls')),

    url('auth/obtain/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('auth/verify/', TokenVerifyView.as_view(), name='token_verify')
]