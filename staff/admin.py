from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Position)


@admin.register(models.Employer)
class StaffMemberAdmin(admin.ModelAdmin):
    actions = ['reset_total_salary_paid',]

    list_display = ('full_name', 'position', 'boss', 'salary_amount', 'total_salary_paid', 'date_joined')
    list_display_links = ('full_name', 'boss')
    list_filter = ('position', 'level')

    fields = ('username',
              'password',
              'first_name',
              'second_name',
              'last_name',
              'email',
              'position',
              'boss',
              'salary_amount',
              'is_staff',
              'is_active',
              'is_superuser',
              'groups',
              'user_permissions')

    def reset_total_salary_paid(self, request, queryset):
        queryset.update(total_salary_paid=0.0)


@admin.register(models.TeamLeader)
class TeamLeaderAdmin(StaffMemberAdmin):
    pass


@admin.register(models.DepartmentLeader)
class DepartmentLeaderAdmin(StaffMemberAdmin):
    pass


@admin.register(models.VicePresident)
class VicePresidentAdmin(StaffMemberAdmin):
    pass


@admin.register(models.President)
class PresidentAdmin(StaffMemberAdmin):
    list_display = ('full_name', 'position', 'salary_amount', 'total_salary_paid')
    list_display_links = ('full_name',)
    fields = ('username',
              'password',
              'first_name',
              'second_name',
              'last_name',
              'email',
              'position',
              'salary_amount',
              'is_staff',
              'is_active',
              'is_superuser',
              'groups',
              'user_permissions')
