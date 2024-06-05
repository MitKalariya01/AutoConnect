from django.conf import settings
from django.urls import path
from main.views import main_view, home_view, list_view, listing_view, edit_view
from main.views import liked_listing_view, inquire_listing_using_email

urlpatterns = [
    path('', main_view, name='main'), # default view page
    path('home/', home_view, name='home'), # home page
    path('list/', list_view, name='list'), # list page
    path('listing/<str:id>/', listing_view, name='listing'), # listing page
    path('listing/<str:id>/edit/', edit_view, name='edit'), # edit page
    path('listing/<str:id>/like/', liked_listing_view, name='liked_listing'), # liked listing page
    path('listing/<str:id>/inquire/', inquire_listing_using_email, name='inquire_listing'), # inquire mail listing
]
