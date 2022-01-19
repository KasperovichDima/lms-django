from django.contrib import admin

from groups.models import Group

from students.models import Student
# from teachers.models import Teacher


class StudentsInlineTable(admin.TabularInline):
    extra = 2
    model = Student
    fields = [
        'first_name',
        'last_name',
        'birthday',
        'phone_number',
        'group',
    ]
    readonly_fields = []
    show_change_link = False


class TeachersInlineTable(admin.TabularInline):
    model = Group.teachers.through
    extra = 0
    # fields = [
    #     'first_name',
    #     'last_name',
    #     'birthday',
    #     'specialization',
    #     'work_experience',
    # ]


class GroupAdmin(admin.ModelAdmin):
    list_display = ['group_name', 'start_date', 'headman', ]
    fields = ['group_name',
              'start_date',
              'headman',
              'teachers'
              ]
    inlines = [TeachersInlineTable, StudentsInlineTable]
    filter_horizontal = ['teachers']


admin.site.register(Group, GroupAdmin)
