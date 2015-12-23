#-*- coding: utf-8 -*- 
from django.conf.urls import url

from . import views

urlpatterns = [
    #common
    url(r'^welcome/$',views.welcome,name = 'welcome'),
    url(r'^HomePage/$',views.HomePage,name = 'HomePage'),
    url(r'^RegesteSuccess/$',views.RegesteSuccess,name = 'RegesteSuccess'),
    #user
    url(r'^StudentUpdate/$', views.StudentUpdate, name='StudentUpdate'),
    url(r'^TeacherUpdate/$', views.TeacherUpdate, name='TeacherUpdate'),
    url(r'^NewUser/$',views.NewUser,name = 'NewUser'),
    url(r'^Login/$',views.Login,name = 'Login'),
    #url(r'^UserDetail/$',views.UserDetail,name = 'UserDetail'),
    url(r'^UserDetail/(?P<pk>[^/]+)/$',views.UserDetail,name = 'UserDetail'),
    url(r'^Logout/$',views.Logout,name = 'Logout'),
    #questions
    url(r'^choiceQ/$', views.get_choicequestion, name='get_choicequestion'),
    url(r'^fillQ/$', views.get_fillquestion, name='get_fillquestion'),
    url(r'^tfQ/$', views.get_tfquestion, name='get_tfquestion'),
    url(r'^saQ/$', views.get_saquestion, name='get_saquestion'),
    url(r'^Questionlist/$', views.Questionlist, name='Questionlist'),
    #url(r'^Questionlist/(?P<point>[^/]+)/(?P<style>[a-z]+)/$', views.Questionlist, name='Questionlist'),
   
    #exam   
    url(r'^AddExam/$',views.AddExam,name = 'AddExam'),
    url(r'^AddExam/(?P<pk>[^/]+)/Questionlist/$',views.SelectQuestion,name = 'SelectQuestion'),
    url(r'^AddExam/(?P<pk>[^/]+)/Questionlist/(?P<point>[^/]+)/(?P<style>[a-z]+)/$', views.SelectQuestion, name='SelectQuestion'),
    url(r'^SetMark/(?P<pk>[^/]+)/SetMark$',views.SetMark,name = 'SetMark'),
    url(r'^ExamList/$',views.ExamList,name = 'ExamList'),
    url(r'^ExamDetail/(?P<pk>[0-9]+)/$',views.ExamDetail,name = 'ExamDetail'),

    #answer
    url(r'^AnswerExam/(?P<pk>[0-9]+)/$',views.AnswerExam,name = 'AnswerExam'),
    url(r'^verifyAnswer/(?P<pk>[0-9]+)/$',views.verify_Answer,name = 'verify_Answer'),
    url(r'^ExamResult/(?P<pk>[0-9]+)/$',views.ExamResult,name = 'ExamResult'),
    url(r'^ResultDetail/(?P<pk>[0-9]+)/$',views.ResultDetail,name = 'ResultDetail'),
    url(r'^JudgeAnswer/(?P<pk>[0-9]+)/$',views.JudgeAnswer,name = 'JudgeAnswer'),
    url(r'^ResultList/$',views.ResultList,name = 'ResultList'),
    ]

    #url(r'^SearchQuestion/$', views.SearchQuestion, name='search_question'),
    #url(r'^SearchQuestion/(?P<point>[^/]+)/(?P<style>[a-z]+)/(?P<pagenum>[0-9]+)/$', views.SearchQuestion, name='search_question'),