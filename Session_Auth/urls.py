
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Permissions import views


router= DefaultRouter()
router.register('studentapi',views.StudentModelViewApi,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # auth used for login and logout
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))

]
