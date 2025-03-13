

from django.urls import path

from pos import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("category",views.CategoryViewSet,basename="category")

router.register("products",views.ProductViewSetView,basename="products")

urlpatterns=[

      path("category/<int:pk>/products/",views.ProductCreateView.as_view()),

      path("orders/",views.OrderSetUpView.as_view()),

      path("orders/<int:pk>/items/",views.OrderItemCreateView.as_view()),

      path("orders/<int:pk>/",views.OrderRetriveView.as_view()),

    
] + router.urls