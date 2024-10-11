from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField(null=True, blank=True)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='proyectos_creados')
    colaboradores = models.ManyToManyField(Usuario, related_name='proyectos_asignados')

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    ESTADO_OPCIONES = [
        ('Pendiente', 'Pendiente'),
        ('Progreso', 'Progreso'),
        ('Completada', 'Completada'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    estado = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='Pendiente')
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateField(default=timezone.now)
    hora_vencimiento = models.TimeField()
    
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas_creadas') 
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    etiquetas = models.ManyToManyField(Etiqueta, related_name='tareas_asociadas', blank=True)

    def __str__(self):
        return self.titulo

class AsignacionTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='asignaciones')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='asignaciones')
    observaciones = models.TextField()
    fecha_asignacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.tarea.titulo} asignada a {self.usuario.nombre}'

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)
    
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self):
        return f'Comentario de {self.autor.nombre} en {self.tarea.titulo}'

