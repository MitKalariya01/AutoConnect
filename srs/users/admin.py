from django.contrib import admin
from users.models import Profile, Location

# Register a model for new user
class ProfileAdmin(admin.ModelAdmin):
    pass

# Register a model for new location
class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)

admin.site.register(Location, LocationAdmin)