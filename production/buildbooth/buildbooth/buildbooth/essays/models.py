from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Intro(models.Model):
    essay = models.ForeignKey('Essay', related_name='intro')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    intro = models.CharField(max_length=500, blank=True, verbose_name='Introduction Sentence')
    transition = models.CharField(max_length=500, blank=True, verbose_name='Transition to Thesis')
    thesis = models.TextField(blank=True)
    conclusion = models.CharField(max_length=500, blank=True, verbose_name='Transition to First Body Paragraph')

    class Meta:
        verbose_name = _('Introduction Paragraph')
        verbose_name_plural = _('Introduction Paragraphs')
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('intro-detail', kwargs={'pk': self.pk})

    def get_display_url(self):
        return '/#/intro/%d' % self.pk


class Body(models.Model):
    essay = models.ForeignKey('Essay', related_name='body')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    intro = models.CharField(max_length=500, blank=True, verbose_name='Introduction Sentence')
    transition = models.CharField(max_length=500, blank=True, verbose_name='Transition to Body')
    body = models.TextField(blank=True, verbose_name='Body Content')
    conclusion = models.CharField(max_length=500, blank=True, verbose_name='Transition to Next Body Paragraph')

    class Meta:
        verbose_name = _('Body Paragraph')
        verbose_name_plural = _('Body Paragraphs')
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('body-detail', kwargs={'pk': self.pk})

    def get_display_url(self):
        return '/#/body/%d' % self.pk


class Conclusion(models.Model):
    essay = models.ForeignKey('Essay', related_name='conclusion')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    intro = models.CharField(max_length=500, blank=True, verbose_name='Introduction Sentence')
    transition = models.CharField(max_length=500, blank=True, verbose_name='Transition to Thesis')
    thesis = models.TextField(blank=True, verbose_name='Restate Your Thesis')
    body = models.TextField(blank=True, verbose_name='Body Content')
    conclusion = models.CharField(max_length=500, blank=True, verbose_name='Concluding Sentance')

    class Meta:
        verbose_name = _('Conclusion Paragraph')
        verbose_name_plural = _('Conclusion Paragraphs')
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('conclusion-detail', kwargs={'pk': self.pk})

    def get_display_url(self):
        return '/#/conclusion/%d' % self.pk


class Essay(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('users.user', related_name='essays')
    title = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = _('Essay')
        verbose_name_plural = _('Essays')
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('essay-detail', kwargs={'pk': self.pk})

    def get_display_url(self):
        return '/#/essay/%d' % self.pk
