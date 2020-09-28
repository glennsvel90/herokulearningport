from django import forms

from . import models


class QuizForm(forms.ModelForm):
    """ The form for a quiz """

class QuestionForm(forms.ModelForm):
    """ The form for a question """
    
class TrueFalseQuestionForm(QuestionForm):
    """ The form for a true/false question """
    

AnswerFormSet = forms.modelformset_factory(
    models.Answer,
    form=AnswerForm,
    extra=2,
)

