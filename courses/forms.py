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


class MultipleChoiceQuestionForm(QuestionForm):
    """ The form for a multiple choice question """
    
    class Meta:
        model = models.MultipleChoiceQuestion
        fields = [
            'order',
            'prompt',
            'shuffle_answers'
        ]


class AnswerForm(forms.ModelForm):
    """ The form for a question """
    
    class Meta:
        model = models.Answer
        fields = [
            'order',
            'text',
            'correct'
        ]
AnswerFormSet = forms.modelformset_factory(
    models.Answer,
    form=AnswerForm,
    extra=2,
)

