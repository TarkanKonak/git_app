from django.contrib import admin
from myCV.models import *
# Register your models here.

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description', 'parameter', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']
    class Meta:
        model = GeneralSetting

@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description', 'file', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'file']
    list_editable = ['description', 'file']
    class Meta:
        model = ImageSetting
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id','order', 'name', 'percentage', 'updated_date', 'created_date']
    search_fields = ['name']
    list_editable = ['order', 'name', 'percentage']
    class Meta:
        model = Skill


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id','company_name', 'job_title', 'start_date', 'end_date', 'updated_date', 'created_date']
    search_fields = ['company_name', 'job_title']
    list_editable = ['company_name', 'job_title', 'start_date', 'end_date']
    class Meta:
        model = Experience




@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id','order', 'link', 'icon',  'updated_date', 'created_date']
    search_fields = ['link', 'icon']
    list_editable = ['order', 'link', 'icon']
    class Meta:
        model = SocialMedia




