from rest_framework.throttling import SimpleRateThrottle

class AnonymousUserThrottle(SimpleRateThrottle):
    rate = '1/day'

    def get_cache_key(self, request, view):
        return self.get_ident(request)