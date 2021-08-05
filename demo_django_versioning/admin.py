from django.contrib import admin
from django.contrib.auth import get_user_model

from simple_history.admin import SimpleHistoryAdmin

from demo_django_versioning.models import Question, Choice


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), SimpleHistoryAdmin)
admin.site.register(Question, SimpleHistoryAdmin)
admin.site.register(Choice, SimpleHistoryAdmin)
