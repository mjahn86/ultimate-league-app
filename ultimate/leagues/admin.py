from django.contrib import admin
from ultimate.leagues.models import *


class LeagueAdmin(admin.ModelAdmin):
	list_display = ('year', 'season', 'night', 'gender', 'state',)
	list_display_links = ('year', 'season', 'night', 'gender', 'state',)
	save_as = True
	save_on_top = True


class ScheduleAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'score_report',)
	list_select_related = True


admin.site.register(Field)
admin.site.register(League, LeagueAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Game)