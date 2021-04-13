from django.urls import path, include
from . import views
from .views import ListProducts, ProductDetailedView, ProductViewSet
from .views import ListProducts, ProductDetailedView, ProductViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter


router = SimpleRouter()
router.register(
    'productviewset', ProductViewSet, basename='product'
)


urlpatterns = [
    path('productlist/', views.listproducts, name='ListProduct'),
    path('messagelist/', views.listmessages, name='message'),
    path('classproductlist/',
         ListProducts.as_view(), name='listproducts'),
    path('classdetailedproduct/<int:pid>/',
         ProductDetailedView.as_view(), name='detailedproduct'),
    path('mixinpath/', views.ListProductsMixins.as_view(), name='mp'),
    path('product-mixin/<int:pk>/',
         views.DetailedProductMixins.as_view(), name='mdp'),
    path('productgenericlist/',
         views.ListProductsGenerics.as_view(), name='lpg'),
    path('productgenericdetail/<int:pk>',
         views.DetailedProductsGenerics.as_view(), name='dpg'),
    path('special/<int:pk>',
         views.SpecilaProductsGenerics.as_view(), name='spg'),
]+router.urls
