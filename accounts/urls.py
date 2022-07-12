from rest_framework.routers import SimpleRouter

from accounts.views.authentication import UserAuthenticationViewSet
from accounts.views.user import CurrentUserViewSet
from accounts.views.user_sign_up import UserSignUpViewSet

router = SimpleRouter()
router.register('user', CurrentUserViewSet, basename='accounts')
router.register('', UserAuthenticationViewSet, basename='')
router.register('signup', UserSignUpViewSet, basename='sign-up')
urlpatterns = router.urls
