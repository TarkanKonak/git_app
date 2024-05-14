from django.shortcuts import render
from myCV.models import GeneralSetting, ImageSetting


# Create your views here.
def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    # -----------------------------------------------------------------------------------
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameter
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameter
    # -----------------------------------------------------------------------------------
    skill_description_name = GeneralSetting.objects.get(name='skill_description_name').parameter
    # -----------------------------------------------------------------------------------
    skill_per_one = GeneralSetting.objects.get(name='skill_per_one').parameter
    skill_per_two = GeneralSetting.objects.get(name='skill_per_two').parameter
    skill_per_three = GeneralSetting.objects.get(name='skill_per_three').parameter
    skill_per_four = GeneralSetting.objects.get(name='skill_per_four').parameter
    skill_per_five = GeneralSetting.objects.get(name='skill_per_five').parameter
    skill_per_six = GeneralSetting.objects.get(name='skill_per_six').parameter
    # -----------------------------------------------------------------------------------
    skill_name_one = GeneralSetting.objects.get(name='skill_name_one').parameter
    skill_name_two = GeneralSetting.objects.get(name='skill_name_two').parameter
    skill_name_three = GeneralSetting.objects.get(name='skill_name_three').parameter
    skill_name_four = GeneralSetting.objects.get(name='skill_name_four').parameter
    skill_name_five = GeneralSetting.objects.get(name='skill_name_five').parameter
    skill_name_six = GeneralSetting.objects.get(name='skill_name_six').parameter
    # -----------------------------------------------------------------------------------
    #images
    header_logo = ImageSetting.objects.get(name='header_logo').file
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file
    site_favicon = ImageSetting.objects.get(name='site_favicon').file


    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'skill_description_name': skill_description_name,
        # -----------------------------------------------------------------------------------
        'skill_per_one': skill_per_one,
        'skill_per_two': skill_per_two,
        'skill_per_three': skill_per_three,
        'skill_per_four': skill_per_four,
        'skill_per_five': skill_per_five,
        'skill_per_six': skill_per_six,
        # -----------------------------------------------------------------------------------
        'skill_name_one': skill_name_one,
        'skill_name_two': skill_name_two,
        'skill_name_three': skill_name_three,
        'skill_name_four': skill_name_four,
        'skill_name_five': skill_name_five,
        'skill_name_six': skill_name_six,
        # -----------------------------------------------------------------------------------
        'header_logo': header_logo,
        'home_banner_image': home_banner_image,
        'site_favicon': site_favicon,
    }
    return render(request, 'index.html', context=context)
