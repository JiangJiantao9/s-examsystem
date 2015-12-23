from django.contrib import admin

from .models import *
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class ChoiceQuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'date','diffculty','ans','user')
    list_filter = ['date']
    search_fields = ['question_text']

class FillQuestionAdmin(admin.ModelAdmin):
	"""docstring for FillQuestion"""
	list_display = ('question_text', 'date', 'diffculty','ans','user') 
	list_filter = ['date']
	search_fields = ['question_text']

class TfQuestionAdmin(admin.ModelAdmin):
    """docstring for FillQuestion"""
    list_display = ('question_text', 'date', 'diffculty','ans','user') 
    list_filter = ['date']
    search_fields = ['question_text']

class ChoiceQuestionInline(admin.TabularInline):
    model = ChoiceQuestionDetail
    extra = 3

class FillQuestionInline(admin.TabularInline):
    model = FillQuestionDetail
    extra = 3

class TfQuestionInline(admin.TabularInline):
    model = TfQuestionDetail
    extra = 3

class SAQuestionInline(admin.TabularInline):
    model = SAQuestionDetail
    extra = 3

class ExamAdmin(admin.ModelAdmin):
    inlines = [ChoiceQuestionInline,FillQuestionInline,TfQuestionInline,SAQuestionInline]
    list_display = ('name','date','diffculty')
    list_filter = ['date']
    search_fields = ['name']

class ChoiceQuestionAnsInline(admin.TabularInline):
    model = ChoiceQuestionAns
    extra = 3

class FillQuestionAnsInline(admin.TabularInline):
    model = FillQuestionAns
    extra = 3

class TfQuestionAnsInline(admin.TabularInline):
    model = TfQuestionAns
    extra = 3

class AnswerAdmin(admin.ModelAdmin):
    inlines = [ChoiceQuestionAnsInline,FillQuestionAnsInline,TfQuestionAnsInline]
    list_display = ('exam','date')
    list_filter = ['date']

admin.site.register(ChoiceQuestion, ChoiceQuestionAdmin)
admin.site.register(FillQuestion, FillQuestionAdmin)
admin.site.register(TfQuestion,TfQuestionAdmin)
admin.site.register(SAQuestion)
admin.site.register(Point)
admin.site.register(Exam,ExamAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Answer,AnswerAdmin)