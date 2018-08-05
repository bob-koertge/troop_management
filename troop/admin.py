from django.contrib import admin

from .models import User, Scout, Parent, Rank, Patrol, Position, Leader, MeritBadge, RankRequirement


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', 'email', 'is_scout',
                    'is_parent', 'is_leader', 'is_staff', 'is_superuser', 'is_active')


class PositionAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'name', 'is_youth_position')


class MeritBadgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_eagle_required', 'is_active')


class RankRequirementAdmin(admin.ModelAdmin):
    list_display = ('number', 'requirement_display',
                    'rank', 'revision', 'is_active', 'is_header')
    ordering = ("rank", "sort_order", )

    def requirement_display(self, obj):
        if obj.is_header:
            return obj.header
        else:
            return obj.short_desc


admin.site.register(User, UserAdmin)
admin.site.register(Scout)
admin.site.register(Parent)
admin.site.register(Rank)
admin.site.register(Patrol)
admin.site.register(Position, PositionAdmin)
admin.site.register(Leader)
admin.site.register(MeritBadge, MeritBadgeAdmin)
admin.site.register(RankRequirement, RankRequirementAdmin)
