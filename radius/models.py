from datetime import datetime
from django.db import models

# Create your models here.


class Estudiante(models.Model):

    cedula = models.CharField(
        max_length=10, db_column="identity", verbose_name="Cédula")
    usuario = models.CharField(
        max_length=15, db_column="username", verbose_name="Usuario")
    correo = models.CharField(
        max_length=30, db_column="email", verbose_name="Correo")
    nombres = models.CharField(
        max_length=20, db_column="name", verbose_name="Nombres")
    apellidos = models.CharField(
        max_length=20, db_column="last_name", verbose_name="Apellidos")
    contrasena = models.CharField(
        max_length=10, db_column="value", verbose_name="Contraseña")
    estado = models.CharField(db_column="status", verbose_name="Estado", choices=[
                              ("0", "INACTIVO"), ("1", "ACTIVO")], default=1, max_length=1)
    carrera = models.CharField(
        verbose_name="Carrera", db_column="career-unit", max_length=50)
    fecha = models.DateField(db_column="date", default=datetime.now())
    attribute = models.CharField(max_length=25, default="Cleartext-Password")
    op = models.CharField(default=":=", max_length=2)

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"

    class Meta:

        db_table = "radcheck"
