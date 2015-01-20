from account.models import Campaign, ClickTracking
from django.contrib import admin


class CampaignAdmin(admin.ModelAdmin):
    list_display = ['name', 'campaign_id', 'expired', 'created']
    search_fields = ['name']


class ClickTrackingAdmin(admin.ModelAdmin):
    list_display = ['campaign', 'link', 'count']
    search_fields = ['link']


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(ClickTracking, ClickTrackingAdmin)
