from django.urls import path, include
from .views import approveReject, ApprovalView, cxcontact
from rest_framework import routers



router = routers.DefaultRouter()
router.register('alldata', ApprovalView)
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/predict/', approveReject),
    path('', cxcontact, name="cxform"),

]
