from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('test/', include('myapp.urls')),
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls', namespace='todo')),
]

# action = "/vypocitej/"
# todo:index -> /todo/
# todo:detail -> /todo/273287/
