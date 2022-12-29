from rest_framework.routers import DefaultRouter
from .views import ( 
    PrintModelViewSet, SampleImageViewSet, 
    DownloadableFileViewSet, TagViewSet, 
    PrintModelTagViewSet, PrintModelViewSet, 
    CategoryViewSet, OrderViewSet, 
    ReviewViewSet, PaymentViewSet
)
router = DefaultRouter()

router.register(r'print-models', PrintModelViewSet)
router.register(r'sample-images', SampleImageViewSet)
router.register(r'downloadable-files', DownloadableFileViewSet)
router.register(r'tags', TagViewSet)
router.register(r'print-model-tags', PrintModelTagViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'payments', PaymentViewSet)