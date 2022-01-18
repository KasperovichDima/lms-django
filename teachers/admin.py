from teachers.models import Teacher

from django.contrib import admin


class TeacherAdmin(admin.ModelAdmin):
    fields = [
        ('first_name', 'last_name'),
        ('birthday', 'age'),
        ('specialization', 'work_experience'),
        'phone_number',
        'salary',
    ]
    readonly_fields = ['age']
    list_display = ['first_name',
                    'last_name',
                    'birthday',
                    'specialization',
                    'work_experience',
                    ]
    list_display_links = list_display
    list_per_page = 20
    search_fields = ['first_name', 'last_name', 'specialization']
    list_filter = (
        'specialization',
        'work_experience'
    )


admin.site.register(Teacher, TeacherAdmin)