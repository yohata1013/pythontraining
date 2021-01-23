from django.contrib import admin

from .models import Question,Choice


#admin.site.register(Question)
#admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('日付情報',{'fields':['pub_date']})
    ]

    inlines = (ChoiceInline,)

admin.site.register(Question,QuestionAdmin)
