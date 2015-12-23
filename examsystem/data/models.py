#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.
#question
class ChoiceQuestion(models.Model):
	"""docstring for Question_select"""
	question_text = models.CharField(max_length=200)
	CHOICES = ( ('A','A'),
				('B','B'),
				('C','C'),
				('D','D'),
			  )
	ans = models.CharField(max_length = 1,choices = CHOICES)
	DIFFCULTYS= (('ez','easy'),
				 ('nm','normal'),
				 ('hd','hard'),
				)
	diffculty = models.CharField(max_length = 2,choices = DIFFCULTYS)
	date = models.DateTimeField('date input',auto_now = True)
	user = models.ForeignKey(User,null = True)
	def __unicode__(self):
		return self.question_text

class Choice(models.Model):
	"""docstring for ClassName"""
	question = models.ForeignKey(ChoiceQuestion)
	choice_text = models.CharField(max_length = 200)
	CHOICES = ( ('A','A'),
				('B','B'),
				('C','C'),
				('D','D'),
			  )
	number = models.CharField(max_length = 1,choices = CHOICES)
	def __unicode__(self):
		return self.choice_text

class FillQuestion(models.Model):
	question_text = models.CharField(max_length=200)
	ans = models.CharField(max_length = 200)
	DIFFCULTYS= (('ez','easy'),
				 ('nm','normal'),
				 ('hd','hard'),
				)
	diffculty = models.CharField(max_length = 2,choices = DIFFCULTYS)
	date = models.DateTimeField('date input',auto_now = True)
	user = models.ForeignKey(User,null = True)
	def __unicode__(self):
		return self.question_text

class TfQuestion(models.Model):
	question_text = models.CharField(max_length=200)
	ans = models.BooleanField()
	DIFFCULTYS= (('ez','easy'),
				 ('nm','normal'),
				 ('hd','hard'),
				)
	diffculty = models.CharField(max_length = 2,choices = DIFFCULTYS)
	date = models.DateTimeField('date input',auto_now = True)
	user = models.ForeignKey(User,null = True)
	def __unicode__(self):
		return self.question_text

class SAQuestion(models.Model):
	question_text= models.CharField(max_length = 200)
	ans = models.CharField(max_length = 200)
	DIFFCULTYS= (('ez','easy'),
				 ('nm','normal'),
				 ('hd','hard'),
				)
	diffculty = models.CharField(max_length = 2,choices = DIFFCULTYS)
	date = models.DateTimeField('date input',auto_now = True)
	user = models.ForeignKey(User,null = True)
	def __unicode__(self):
		return self.question_text

#point&subject
class Point(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children")
    choicequestions= models.ManyToManyField(ChoiceQuestion,blank = True) 
    fillquestions = models.ManyToManyField(FillQuestion,blank = True) 
    tfquestions = models.ManyToManyField(TfQuestion,blank = True)
    saquestions = models.ManyToManyField(SAQuestion,blank = True)
    def __unicode__(self):
        return self.name

#exam
class Exam(models.Model):
	name = models.CharField(max_length=50)
	subject = models.ForeignKey(Point)
	DIFFCULTYS= (('ez','easy'),
				 ('nm','normal'),
				 ('hd','hard'),
				)
	diffculty = models.CharField(max_length = 2,choices = DIFFCULTYS)
	count = models.IntegerField(default = 100)
	choicequestions= models.ManyToManyField(ChoiceQuestion,through = 'ChoiceQuestionDetail',blank = True)
	fillquestions = models.ManyToManyField(FillQuestion,through = 'FillQuestionDetail',blank = True)
	tfquestions = models.ManyToManyField(TfQuestion,through = 'TfQuestionDetail',blank = True)
	saquestions = models.ManyToManyField(SAQuestion,through = 'SAQuestionDetail',blank = True)
	date = models.DateTimeField('date_input',auto_now = True)
	user = models.ForeignKey(User,null = True)
	def __unicode__(self):
		return self.name

class ChoiceQuestionDetail(models.Model):
	choicequestion = models.ForeignKey(ChoiceQuestion)
	exam = models.ForeignKey(Exam)
	mark = models.IntegerField()

class FillQuestionDetail(models.Model):
	choicequestion = models.ForeignKey(FillQuestion)
	exam = models.ForeignKey(Exam)
	mark = models.IntegerField()

class TfQuestionDetail(models.Model):
	tfquestion = models.ForeignKey(TfQuestion)
	exam = models.ForeignKey(Exam)
	mark = models.IntegerField()

class SAQuestionDetail(models.Model):
	saquestion = models.ForeignKey(SAQuestion)
	exam = models.ForeignKey(Exam)
	mark = models.IntegerField()
	
#answer
class Answer(models.Model):
	exam = models.ForeignKey(Exam)
	choicequestion = models.ManyToManyField(ChoiceQuestion,through = 'ChoiceQuestionAns')
	fillquestion = models.ManyToManyField(FillQuestion,through = 'FillQuestionAns')
	Tfquestion = models.ManyToManyField(TfQuestion,through = 'TfQuestionAns')
	saquestion = models.ManyToManyField(SAQuestion,through = 'SAQuestionAns')
	user = models.ForeignKey(User,null = True)
	select_score = models.IntegerField(null=True,default= None)
	fill_score= models.IntegerField(null = True,default = None)
	tf_score= models.IntegerField(null = True,default = None)
	sa_score= models.IntegerField(null = True,default = None)
	score = models.IntegerField(null = True,default = None)
	state = models.BooleanField(default = True)
	date = models.DateTimeField('date_input',auto_now = True)

class ChoiceQuestionAns(models.Model):
	choicequestion = models.ForeignKey(ChoiceQuestion)
	answer = models.ForeignKey(Answer)
	ans = models.CharField(max_length = 2,null = True)
	state = models.NullBooleanField(null = True,default =None)

class FillQuestionAns(models.Model):
	fillquestion = models.ForeignKey(FillQuestion)
	answer = models.ForeignKey(Answer)
	ans = models.CharField(max_length = 100,null= True)
	state = models.NullBooleanField(null = True,default = None)

class TfQuestionAns(models.Model):
	Tfquestion = models.ForeignKey(TfQuestion)
	answer = models.ForeignKey(Answer)
	ans = models.NullBooleanField()
	state = models.NullBooleanField(null = True,default = None)

class SAQuestionAns(models.Model):
	saquestion = models.ForeignKey(SAQuestion)
	answer = models.ForeignKey(Answer)
	ans = models.CharField(max_length = 200,null = True)
	mark = models.IntegerField(default = 10)
	score = models.IntegerField(null = True)
	state = models.NullBooleanField(null = True,default = None)

#user
class Student(models.Model):
	name = models.CharField(max_length=10,null = True)
	user = models.ForeignKey(User,null = True)
	num = models.CharField(max_length=15,null = True)
	age = models.IntegerField(null = True)
	SEX =(('m','男'),('f','女'),)
	sex = models.CharField(max_length = 1,choices = SEX,null = True)
	birth = models.DateField(blank = True,null = True)
	COLLEGE = (('计算机','计算机学院'),('软件','软件学院'),)
	college = models.CharField(max_length = 10,choices = COLLEGE,null = True)
	tel = models.CharField(max_length = 15,blank = True,null = True)
	email =models.EmailField(blank = True,null = True)
	def __unicode__(self):
		if self.name == None:
			return 'NULL'
		return self.name

class Teacher(models.Model):
	name = models.CharField(max_length=10,null = True)
	user = models.ForeignKey(User,null = True)
	num = models.CharField(max_length=15,null = True)
	age = models.IntegerField(null = True)
	SEX =(('m','男'),('f','女'),)
	sex = models.CharField(max_length = 1,choices = SEX,null = True)
	birth = models.DateField(blank = True,null = True)
	COLLEGE = (('sc','计算机学院'),('sw','软件学院'),)
	college = models.CharField(max_length = 20,choices = COLLEGE,blank = True,null = True)
	tel = models.CharField(max_length = 15,blank = True,null = True)
	email =models.EmailField(blank = True,null = True)
	def __unicode__(self):
		return self.name