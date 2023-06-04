from .models import SocialMediaLinks
def add_variable_to_context(request):
    try:
        links = SocialMediaLinks.objects.get(id = 1)

        return{
            'facebook':links.facebook,
            'github': links.github,
            'twitter': links.twitter,
            'instagram': links.instagram,
            'github': links.github,
            'linkedin': links.linkedin,
            'youtube': links.youtube
        }

    except:
        return dict()