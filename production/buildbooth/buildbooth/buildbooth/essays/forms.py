from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit, Button, Fieldset, HTML
from django import forms

from .models import Intro, Body, Conclusion, Essay


class IntroForm(forms.ModelForm):
    class Meta:
        model = Intro
        fields = [
            'intro', 'transition', 'thesis', 'conclusion',
            'essay',
        ]
        widgets = {
            'essay': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(IntroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Introduction Paragraph',
                'essay',
                Field("intro", css_class='form-control', ng_model='document.intro.intro',
                      data_content='<p><em>%s</em></p><p><strong>%s</strong></p><p>%s</p>' % (
                          'You should start with a broad statement that introduces the general subject of your paper.',
                          'Example',
                          'Langston Hughes short story Salvation is a brazen work which tells the story of the authors real-life refusal to fully embrace ideologies as a twelve year old boy.'
                      )),
                Field("transition", css_class='form-control', ng_model='document.intro.transition',
                      data_content='<p><em>%s</em></p><p><strong>%s</strong></p><p>%s</p>' % (
                          'Provide more context for the central argument of your essay, or thesis (note: this can come before or after the essay',
                          'Example',
                          'In telling this story of a rather pivotal night Hughes experienced as a youth, the author clearly unveils a theme of disillusionment with his religious institution as well as the extraordinary amount of pressure forced upon any children slightly skeptical towards the ideas or beliefs which that religion relies upon.'
                      )),
                Field("thesis", css_class='form-control', ng_model='document.intro.thesis',
                      data_content='<p><em>%s</em></p><p><strong>%s</strong></p><p>%s</p>' % (
                          'Now comes the thesis, or central argument of the essay.  A good litmus test for a thesis is asking yourself "so what?" Your thesis should not be too broad and will need to be backed up by evidence from the text as well as external sources (if needed).',
                          'Example',
                          'Hughes brings forth these themes via a precise and gripping point of view, strong imagery, a compellingly bittersweet tone, and a bit of irony and sarcasm sprinkled throughout the text.'
                      )),
                Field("conclusion", css_class="form-control", ng_model='document.intro.conclusion',
                      data_content='<p><em>%s</em></p><p><strong>%s</strong></p><p>%s</p>' % (
                          'Restate the thesis and first sentence, being sure to make a smooth transition into the next paragraph.',
                          'Example',
                          'All these elements combine to form the authors scathing indictment of unequivocal religious devotion.'
                      )),
            ),
        )


class BodyForm(forms.ModelForm):
    class Meta:
        model = Body
        fields = [
            'intro', 'transition', 'body', 'conclusion',
            'essay',
        ]
        widgets = {
            'essay': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(BodyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Body Paragraph',
                'essay',
                Field("intro", css_class='form-control', ng_model='bodyParagraph.intro',
                      data_content='<p><em>%s</em></p><p><strong>%s</strong></p><p>%s</p><p><strong>%s</strong></p><p>%s</p>' % (
                          'Instructions',
                          'Thesis',
                          '{[{ document.intro.thesis }]}',
                          'Example',
                          'Example Content'
                      )),
                Field("transition", css_class='form-control', ng_model='bodyParagraph.transition',
                      data_content='<p><em>%s</em></p><p><strong>%s</strong></p><p>%s</p>' % (
                          'Instruction Content',
                          'Example',
                          'Example Content'
                      )),
                Field("body", css_class="form-control", ng_model='bodyParagraph.body',
                      data_content='<p><em>%s</em></p><p><strong>%s</strong></p><p>%s</p>' % (
                          'Instruction Content',
                          'Example',
                          'Example Content'
                      )),
                Field("conclusion", css_class="form-control", ng_model='bodyParagraph.conclusion',
                      data_content='<p><em>%s</em></p><p><strong>%s</strong></p><p>%s</p>' % (
                          'Instruction Content',
                          'Example',
                          'Example Content'
                      )),
            ),
        )


class ConclusionForm(forms.ModelForm):
    class Meta:
        model = Conclusion
        fields = [
            'intro', 'transition', 'thesis', 'body', 'conclusion',
            'essay',
        ]
        widgets = {
            'essay': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ConclusionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Conclusion Paragraph',
                'essay',
                Field("intro", css_class='form-control', ng_model='document.conclusion.intro',
                      data_content='<p><em>%s</em></p><p><strong>%s</strong></p><p>%s</p>' % (
                          'Instruction Content',
                          'Example',
                          'Example Content'
                      )),
                Field("transition", css_class='form-control', ng_model='document.conclusion.transition',
                      data_content='<p><em>%s</em></p><p><strong>%s</strong></p><p>%s</p>' % (
                          'Instruction Content',
                          'Example',
                          'Example Content'
                      )),
                Field("thesis", css_class='form-control', ng_model='document.conclusion.thesis',
                      data_content='<p><em>%s</em></p><p><strong>%s</strong></p><p>%s</p><p><strong>%s</strong></p><p>%s</p>' % (
                          'Instruction Content',
                          'Thesis',
                          '{[{ document.intro.thesis }]}',
                          'Example',
                          'Example Content'
                      )),
                Field("body", css_class="form-control", ng_model='document.conclusion.body',
                      data_content='<p><em>%s</em></p><p><strong>%s</strong></p><p>%s</p>' % (
                          'Instruction Content',
                          'Example',
                          'Example Content'
                      )),
                Field("conclusion", css_class="form-control", ng_model='document.conclusion.conclusion',
                      data_content='<p><em>%s</em></p><p><strong>%s</strong></p><p>%s</p>' % (
                          'Instruction Content',
                          'Example',
                          'Example Content'
                      )),
            ),
        )


class EssayForm(forms.ModelForm):
    class Meta:
        model = Essay
        fields = [
            'title', 'owner',
        ]
        widgets = {
            'owner': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(EssayForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Essay',
                'owner',
                Field("title", css_class='form-control', ng_model='document.essay.title', ng_blur='saveEssay()',
                      data_content='<p><em>%s</em></p><p><strong>%s</strong></p><p>%s</p>' % (
                          'Allude to your subject and ideally hint to your thesis. Dont capitalize the words a, the, to, with, but, and, or the.',
                          'Example',
                          'BuildBooth: The Best Way to Build'
                      ))
            )
        )


class SummaryForm(forms.Form):
    document = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super(SummaryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_tag = False
        #self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Field("document", css_class="form-control", rows=20),
        )
