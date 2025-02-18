from django.contrib import admin
from .Models import Activities, Client, ChienDichData, ChienDich, NguonGoi, BlackList, Report, CallOutCome, CallStatus, Calls, HistoryCallVB, HistoryCall, Queue, ReportView, VBChienDich, VBSetup



# Register your models here.
admin.site.register(Activities)
admin.site.register(Client)
admin.site.register(ChienDichData)
admin.site.register(NguonGoi)
admin.site.register(BlackList)
admin.site.register(Report)
admin.site.register(CallOutCome)
admin.site.register(CallStatus)
admin.site.register(Calls)
admin.site.register(HistoryCallVB)
admin.site.register(HistoryCall)
admin.site.register(Queue)
admin.site.register(ReportView)
admin.site.register(VBChienDich)
admin.site.register(VBSetup)