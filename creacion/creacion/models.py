from django.db import models
from django.utils import timezone

# Modelo Usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

# Modelo Proyecto
class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField(null=True, blank=True)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='proyectos_creados')  # Relación con Usuario (Creador)
    colaboradores = models.ManyToManyField(Usuario, related_name='proyectos_asignados')  # Relación con Usuarios (Colaboradores)

    def __str__(self):
        return self.nombre

# Modelo Etiqueta
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

# Modelo Tarea
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
    
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas_creadas')  # Relación con Usuario (Creador)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')  # Relación con Proyecto
    etiquetas = models.ManyToManyField(Etiqueta, related_name='tareas_asociadas', blank=True)  # Relación con Etiquetas

    def __str__(self):
        return self.titulo

# Modelo Asignación de Tarea (relación intermedia entre Tarea y Usuario)
class AsignacionTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='asignaciones')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='asignaciones')
    observaciones = models.TextField()
    fecha_asignacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.tarea.titulo} asignada a {self.usuario.nombre}'

# Modelo Comentario
class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)
    
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')  # Relación con Usuario (Autor)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='comentarios')  # Relación con Tarea

    def __str__(self):
        return f'Comentario de {self.autor.nombre} en {self.tarea.titulo}'

