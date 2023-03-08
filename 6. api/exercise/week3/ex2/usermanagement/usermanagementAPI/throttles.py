from rest_framework.throttling import  UserRateThrottle

# This code creates a new throttle policy with unnamed scope.
class TenCallsPerMinute(UserRateThrottle):
    scope = 'ten'