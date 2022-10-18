from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin
from radius.models import Estudiante

# Register your models here.

@admin.register(Estudiante)
class EstudiantesAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin):
    search_fields = ["cedula",
                     "usuario",
                     "nombres",
                     "apellidos", ]
    list_display = ["cedula",
                    "usuario",
                    "correo",
                    "nombres",
                    "apellidos",
                    "carrera",
                    "_estado"]
    exclude = ["fecha","attribute","op"]
    list_per_page = 20

    list_filter= ["carrera"]


    @admin.display(boolean=True)
    def _estado(self, obj):
        return obj.estado
