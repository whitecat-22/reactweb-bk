from django.contrib import admin
from django_boost.admin import LogicalDeletionModelAdmin

from .models import User, Customer, Project

@admin.register(User)
class UserAdmin(LogicalDeletionModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(LogicalDeletionModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(LogicalDeletionModelAdmin):
    pass
