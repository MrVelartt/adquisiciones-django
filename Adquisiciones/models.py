from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import date

class Acquisition(models.Model):
    presupuesto = models.DecimalField("Presupuesto", max_digits=15, decimal_places=2, validators=[MinValueValidator(0)])
    unidad = models.CharField("Unidad administrativa", max_length=255)
    tipo_bien_servicio = models.CharField("Tipo de bien o servicio", max_length=255)
    cantidad = models.PositiveIntegerField("Cantidad", validators=[MinValueValidator(1)])
    valor_unitario = models.DecimalField("Valor unitario", max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    valor_total = models.DecimalField("Valor total", max_digits=15, decimal_places=2, validators=[MinValueValidator(0)])
    fecha_adquisicion = models.DateField("Fecha de adquisición")
    proveedor = models.CharField("Proveedor", max_length=255)
    documentacion = models.TextField("Documentación")
    activa = models.BooleanField("Activa", default=True)
    fecha_creacion = models.DateTimeField("Fecha de creación", auto_now_add=True)
    fecha_actualizacion = models.DateTimeField("Última actualización", auto_now=True)

    def clean(self):
        # Validar que la fecha no sea futura
        if self.fecha_adquisicion > date.today():
            raise ValidationError({'fecha_adquisicion': "La fecha de adquisición no puede ser futura."})
        
        # Validar que valor_total sea consistente (opcional si no quieres permitir edición directa)
        expected_total = self.cantidad * self.valor_unitario
        if self.valor_total != expected_total:
            raise ValidationError({
                'valor_total': f"El valor total debe ser igual a cantidad × valor unitario ({expected_total})."
            })

    def __str__(self):
        return f"{self.tipo_bien_servicio} - {self.proveedor} - {self.fecha_adquisicion}"
