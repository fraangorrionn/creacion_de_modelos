from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Usuario, Proyecto, Tarea, Etiqueta, AsignacionTarea, Comentario

# Vista para listar Usuarios
class UsuarioList(ListView):
    model = Usuario
    template_name = 'biblioteca/usuario_list.html'  # Cambia según tu estructura de plantillas
    context_object_name = 'usuarios'

# Vista para crear Usuarios
class UsuarioCreate(CreateView):
    model = Usuario
    template_name = 'biblioteca/usuario_form.html'  # Cambia según tu estructura de plantillas
    fields = ['nombre', 'correo_electronico', 'contraseña']  # Cambia según los campos de tu modelo
    success_url = reverse_lazy('usuario_list')

# Vista para listar Proyectos
class ProyectoList(ListView):
    model = Proyecto
    template_name = 'biblioteca/proyecto_list.html'
    context_object_name = 'proyectos'

# Vista para crear Proyectos
class ProyectoCreate(CreateView):
    model = Proyecto
    template_name = 'biblioteca/proyecto_form.html'
    fields = ['nombre', 'descripcion', 'duracion_estimada', 'fecha_inicio', 'fecha_finalizacion']
    success_url = reverse_lazy('proyecto_list')

# Vista para listar Tareas
class TareaList(ListView):
    model = Tarea
    template_name = 'biblioteca/tarea_list.html'
    context_object_name = 'tareas'

# Vista para crear Tareas
class TareaCreate(CreateView):
    model = Tarea
    template_name = 'biblioteca/tarea_form.html'
    fields = ['titulo', 'descripcion', 'prioridad', 'estado', 'completada', 'fecha_creacion', 'hora_vencimiento']
    success_url = reverse_lazy('tarea_list')

# Vista para listar Etiquetas
class EtiquetaList(ListView):
    model = Etiqueta
    template_name = 'biblioteca/etiqueta_list.html'
    context_object_name = 'etiquetas'

# Vista para crear Etiquetas
class EtiquetaCreate(CreateView):
    model = Etiqueta
    template_name = 'biblioteca/etiqueta_form.html'
    fields = ['nombre']
    success_url = reverse_lazy('etiqueta_list')

# Vista para listar Asignaciones de Tarea
class AsignacionTareaList(ListView):
    model = AsignacionTarea
    template_name = 'biblioteca/asignacion_list.html'
    context_object_name = 'asignaciones'

# Vista para crear Asignaciones de Tarea
class AsignacionTareaCreate(CreateView):
    model = AsignacionTarea
    template_name = 'biblioteca/asignacion_form.html'
    fields = ['observaciones', 'fecha_asignacion']
    success_url = reverse_lazy('asignacion_list')

# Vista para listar Comentarios
class ComentarioList(ListView):
    model = Comentario
    template_name = 'biblioteca/comentario_list.html'
    context_object_name = 'comentarios'

# Vista para crear Comentarios
class ComentarioCreate(CreateView):
    model = Comentario
    template_name = 'biblioteca/comentario_form.html'
    fields = ['contenido']
    success_url = reverse_lazy('comentario_list')