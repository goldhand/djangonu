from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from .views import IntroViewSet, BodyViewSet, ConclusionViewSet, EssayViewSet, UserViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'intro', IntroViewSet)
router.register(r'body', BodyViewSet)
router.register(r'conclusion', ConclusionViewSet)
router.register(r'essay', EssayViewSet)
router.register(r'users', UserViewSet)

urlpatterns = patterns('essays.views',
                       url(r'^', include(router.urls)),
                       url(r'^angular/partials/essay-list/', 'angular_view_essay_list'),
                       url(r'^angular/partials/essay-detail/', 'angular_view_essay_detail'),
                       url(r'^angular/partials/essay-document/', 'angular_view_essay_document'),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

