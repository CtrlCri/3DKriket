# Archivo principal de urls

from django.urls import include, path
from rest_framework import routers

from printmodels import views

router = routers.DefaultRouter()
router.register(r'print-models', views.PrintModelViewSet, basename='print-model')
router.register(r'sample-images', views.SampleImageViewSet, basename='sample-image')
router.register(r'downloadable-files', views.DownloadableFileViewSet, basename='downloadable-file')
router.register(r'tags', views.TagViewSet, basename='tag')
router.register(r'print-model-tags', views.PrintModelTagViewSet, basename='print-model-tag')
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'orders', views.OrderViewSet, basename='order')
router.register(r'reviews', views.ReviewViewSet, basename='review')
router.register(r'payments', views.PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]
