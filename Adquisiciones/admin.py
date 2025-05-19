from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Acquisition

@admin.register(Acquisition)
class AcquisitionAdmin(VersionAdmin):
    list_display = (
        'id',
        'tipo_bien_servicio',
        'proveedor',
        'cantidad',
        'valor_unitario',
        'valor_total',
        'fecha_adquisicion',
        'unidad',
        'activa',
    )
    list_filter = ('unidad', 'proveedor', 'fecha_adquisicion', 'activa')
    search_fields = ('tipo_bien_servicio', 'proveedor', 'unidad')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    fieldsets = (
        (None, {
            'fields': (
                'presupuesto',
                'unidad',
                'tipo_bien_servicio',
                'cantidad',
                'valor_unitario',
                'valor_total',
                'fecha_adquisicion',
                'proveedor',
                'documentacion',
                'activa',
                'fecha_creacion',
                'fecha_actualizacion',
            )
        }),
    )
