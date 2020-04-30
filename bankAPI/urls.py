from django.urls import path, include
from .views import approveReject, ApprovalView, cxcontact
from rest_framework import routers



router = routers.DefaultRouter()
router.register('alldata', ApprovalView)
urlpatterns = [
    path('', include(router.urls)),
    path('predict/', approveReject),
    path('form/', cxcontact, name="cxform"),

]
