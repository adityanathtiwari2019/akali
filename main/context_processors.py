from main.models import sitesocial

def social_processor(request):
    links = sitesocial.objects.all()
    return {'social_links':links}