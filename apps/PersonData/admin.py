from django.contrib import admin

from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date','text']
    inlines = [ChoiceInLine]
    
admin.site.register(Question, QuestionAdmin)