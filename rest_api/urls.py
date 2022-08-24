from rest_framework.routers import DefaultRouter

from .views import BookingViewSet, ContactViewSet, NewsletterViewSet, TaxiViewSet

router = DefaultRouter()

router.register('taxi', TaxiViewSet)
router.register('booking', BookingViewSet)
router.register('contact', ContactViewSet)
router.register('newsletter', NewsletterViewSet)

urlpatterns = router.urls
