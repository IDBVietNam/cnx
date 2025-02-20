from django.contrib import admin

from .models import Customer, Campaign, CampaignData

# Register your models here.

admin.site.register(Customer)
admin.site.register(Campaign)
admin.site.register(CampaignData)
