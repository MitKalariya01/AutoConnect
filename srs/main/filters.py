import django_filters

from main.models import Listing

class ListingFilter(django_filters.FilterSet):
    
    class Meta():
        model = Listing()
        fields = {'brand':{'exact'}, 'transmisson':{'exact'}, 'mileage':{'lt', 'gt'}, 'model':{'icontains'}}