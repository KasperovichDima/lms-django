from django.contrib import admin

from groups.models import Group

from students.models import Student


class StudentsInlineTable(admin.TabularInline):
    extra = 5
    model = Student
    fields = [
        'first_name',
        'last_name',
        'birthday',
        'phone_number',
        'group',
    ]
    readonly_fields = fields
    show_change_link = True


class GroupAdmin(admin.ModelAdmin):
    list_display = ['group_name', 'start_date', 'headman']
    fields = ['group_name', 'start_date', 'headman', 'teachers']
    inlines = [StudentsInlineTable]


admin.site.register(Group, GroupAdmin)
