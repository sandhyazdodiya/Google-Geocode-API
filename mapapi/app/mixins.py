from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class CSRFExemptMixin(object):
    """
    A mixin to by pass csrf token validation.
    We do not do this in production.
    This is just to understand requests.
    
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)