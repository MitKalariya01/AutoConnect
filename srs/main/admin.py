from django.contrib import admin

from main.models import Listing
from main.models import Liked_View_Listing


class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )


class Liked_view_liting_Admin(admin.ModelAdmin):
    readonly_fields = ('id', )


admin.site.register(Listing, ListingAdmin)
admin.site.register(Liked_View_Listing, Liked_view_liting_Admin)