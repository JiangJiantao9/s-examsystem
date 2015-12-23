#-*- coding: utf-8 -*- 
from django import forms
from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

from .models import *
from django.contrib.auth.models import Group

#QuestionForm
class ChoiceQuestionForm(forms.Form):
    point = forms.ModelChoiceField(label='point',queryset=Point.objects.all())
    question = forms.CharField(label='question', max_length=100,widget=forms.Textarea(attrs={'cols':'110','rows':'5'}))
    choiceA = forms.CharField(label='A', max_length=100)
    choiceB = forms.CharField(label='B', max_length=100)
    choiceC = forms.CharField(label='C', max_length=100)
    choiceD = forms.CharField(label='D', max_length=100)
    CHOICES = ( ('A','A'),
				('B','B'),
				('C','C'),
				('D','D'),
			  )
    ans = forms.ChoiceField(label = 'ans',choices = CHOICES)
    DIFFCULTYS= (('ez','easy'),
				 ('nm','normal'),
				 ('hd','hard'),
				)
    diffculty = forms.ChoiceField(label = 'diffculty',choices = DIFFCULTYS)

class FillQuestionForm(forms.Form):
	point = forms.ModelChoiceField(label='point',queryset=Point.objects.all())
	question = forms.CharField(label='question', max_length=100,widget=forms.Textarea(attrs={'cols':'110','rows':'5'}))
	ans =  forms.CharField(label='ans', max_length=100)
	DIFFCULTYS= (('ez','easy'),
			 ('nm','normal'),
			 ('hd','hard'),
			)
	diffculty = forms.ChoiceField(label = 'diffculty',choices = DIFFCULTYS)

class TfQuestionForm(ModelForm):
	point = forms.ModelChoiceField(label='point',queryset=Point.objects.all())
	class Meta:
		model = TfQuestion
		fields = ['question_text','ans','diffculty']
		widgets = {
         	'question_text':forms.Textarea(attrs={'cols':'110','rows':'5'})
        		}
class SAQuestionForm(ModelForm):
	point = forms.ModelChoiceField(label='point',queryset=Point.objects.all())
	class Meta:
		model = SAQuestion
		fields = ['question_text','ans','diffculty']
		widgets = {
         	'question_text':forms.Textarea(attrs={'cols':'110','rows':'5'})
        		}

class SearchQuestionForm(forms.Form):
	point = forms.ModelChoiceField(label='point',queryset=Point.objects.all(),required = False)
	STYLE = (('select','select'),('fill','fill'),('tf','tf'),('sa','sa'))
	style = forms.ChoiceField(label = 'style',choices = STYLE)
	question_keyword = forms.CharField(label = 'question_keyword',max_length = 100,required=False)

#exam
class AddExamForm(ModelForm):
	count = forms.IntegerField(label='count')
	class Meta:
		model = Exam
		fields = ['name','subject','diffculty']
		'''widgets = {
            'fillquestions': CheckboxSelectMultiple(),
            'choicequestions':CheckboxSelectMultiple(),
        		}'''

class SearchExamForm(forms.Form):
	name = forms.CharField(label = 'name',max_length = 20,required = False)
	subject = forms.ModelChoiceField(label = 'subject',queryset = Point.objects.all(),required =False)
	DIFFCULTYS= (('ez','easy'),
				 ('nm','normal'),
				 ('hd','hard'),
				 ('all','all')
				)
	diffculty = forms.ChoiceField(label = 'diffculty',choices = DIFFCULTYS)

class SearchAnswerForm(forms.Form):
	name = forms.CharField(label = 'name',max_length = 20,required = False)
	author = forms.CharField(label = 'author',max_length = 20,required = False)
#user
class StudentSignInForm(forms.Form):
	name = forms.CharField(label='name', max_length=10)
	num = forms.CharField(label='num', max_length=15)
	age = forms.IntegerField(label = 'age')
	SEX =(('m','男'),('f','女'),)
	sex = forms.ChoiceField(label = 'sex',choices = SEX)
	birth = forms.DateField(label ='birth',required=False)
	COLLEGE = (('计算机','计算机学院'),('软件','软件学院'),)
	college = forms.ChoiceField(label = 'college',choices = COLLEGE)
	tel = forms.CharField(label = 'tel',max_length = 15,required=False)
	email =forms.EmailField(label = 'email',required=False)

class TeacherSignInForm(forms.Form):
	name = forms.CharField(label='name', max_length=10)
	num = forms.CharField(label='num', max_length=15)
	age = forms.IntegerField(label = 'age')
	SEX =(('m','男'),('f','女'),)
	sex = forms.ChoiceField(label = 'sex',choices = SEX)
	birth = forms.DateField(label ='birth',required=False)
	COLLEGE = (('计算机','计算机学院'),('软件','软件学院'),)
	college = forms.ChoiceField(label = 'college',choices = COLLEGE)
	tel = forms.CharField(label = 'tel',max_length = 15,required=False)
	email =forms.EmailField(label = 'email',required=False)

class NewUserSignInForm(forms.Form):
	username = forms.CharField(label = 'username',max_length = 30)
	password = forms.CharField(label = 'password',max_length = 10)
	GROUPS = (('teacher','teacher'),('student','student'))
	group = forms.ModelChoiceField(label = 'group',queryset=Group.objects.all())

class NewUserLoginForm(forms.Form):
	username = forms.CharField(label = 'username',max_length = 30)
	password = forms.CharField(label = 'password',max_length = 10)