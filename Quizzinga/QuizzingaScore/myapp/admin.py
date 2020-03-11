from django.contrib import admin

from .models import Team, Question, Member, Quiz, Score

admin.site.register(Question)
admin.site.register(Team)
admin.site.register(Member)
admin.site.register(Quiz)
admin.site.register(Score)
# Register your models here.
