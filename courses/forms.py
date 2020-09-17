from django import forms

from . import models


class QuizForm(forms.ModelForm):
    """ The form for a quiz """

class QuestionForm(forms.ModelForm):
    """ The form for a question """
    
    class Media:
        css = {'all':('course/css/order.css',)}
        js = (
            'courses/js/vendor/jquery.fn.sortable.min.js',
            'courses/js/order.js'
        )


class TrueFalseQuestionForm(QuestionForm):
    """ The form for a true/false question """
    
    class Meta:
        model = models.TrueFalseQuestion
        fields = ['order', 'prompt']


AnswerFormSet = forms.modelformset_factory(
    models.Answer,
    form=AnswerForm,
    extra=2,
)

