from django.contrib import admin

from callsource.models import CallSource, HistoryCallSource

admin.site.register(CallSource)
admin.site.register(HistoryCallSource)
