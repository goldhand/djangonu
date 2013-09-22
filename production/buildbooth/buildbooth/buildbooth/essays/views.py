from django.forms.models import inlineformset_factory
from django.shortcuts import render

from rest_framework import permissions, viewsets

from users.models import User

from .permissions import IsOwnerOrReadOnly

from .models import Intro, Body, Conclusion, Essay
from .serializers import IntroSerializer, BodySerializer, ConclusionSerializer, EssaySerializer, UserSerializer
from .forms import IntroForm, BodyForm, ConclusionForm, EssayForm, SummaryForm


class IntroViewSet(viewsets.ModelViewSet):
    queryset = Intro.objects.all()
    serializer_class = IntroSerializer


class BodyViewSet(viewsets.ModelViewSet):
    queryset = Body.objects.all()
    serializer_class = BodySerializer


class ConclusionViewSet(viewsets.ModelViewSet):
    queryset = Conclusion.objects.all()
    serializer_class = ConclusionSerializer


class EssayViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def angular_view(request):

    return render(request, 'essays/angular/index.html')


def angular_view_essay_list(request):
    return render(request, 'essays/angular/partials/essay-list.html')


def angular_view_essay_detail(request):
    return render(request, 'essays/angular/partials/essay-detail.html')


def angular_view_essay_document(request):
    context = {
        #'thesis_part_form': ThesisPartForm(),
        'intro_form': IntroForm(),
        'body_form': BodyForm(),
        'conclusion_form': ConclusionForm(),
        'essay_form': EssayForm(),
        'summary_form': SummaryForm(),
        }
    return render(request, 'essays/angular/partials/essay-document.html', context)




