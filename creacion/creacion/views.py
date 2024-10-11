from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Usuario, Proyecto, Tarea, Etiqueta, AsignacionTarea, Comentario

class UsuarioList(ListView):
    model = Usuario
    template_name = 'creacion/usuario_list.html'  # Cambia según tu estructura de plantillas
    context_object_name = 'usuarios'

class UsuarioCreate(CreateView):
    model = Usuario
    template_name = 'creacion/usuario_form.html'  # Cambia según tu estructura de plantillas
    fields = ['nombre', 'correo_electronico', 'contraseña']  # Cambia según los campos de tu modelo
    success_url = reverse_lazy('usuario_list')

class ProyectoList(ListView):
    model = Proyecto
    template_name = 'creacion/proyecto_list.html'
    context_object_name = 'proyectos'

class ProyectoCreate(CreateView):
    model = Proyecto
    template_name = 'creacion/proyecto_form.html'
    fields = ['nombre', 'descripcion', 'duracion_estimada', 'fecha_inicio', 'fecha_finalizacion']
    success_url = reverse_lazy('proyecto_list')

class TareaList(ListView):
    model = Tarea
    template_name = 'creacion/tarea_list.html'
    context_object_name = 'tareas'

class TareaCreate(CreateView):
    model = Tarea
    template_name = 'creacion/tarea_form.html'
    fields = ['titulo', 'descripcion', 'prioridad', 'estado', 'completada', 'fecha_creacion', 'hora_vencimiento']
    success_url = reverse_lazy('tarea_list')

class EtiquetaList(ListView):
    model = Etiqueta
    template_name = 'creacion/etiqueta_list.html'
    context_object_name = 'etiquetas'

class EtiquetaCreate(CreateView):
    model = Etiqueta
    template_name = 'creacion/etiqueta_form.html'
    fields = ['nombre']
    success_url = reverse_lazy('etiqueta_list')

class AsignacionTareaList(ListView):
    model = AsignacionTarea
    template_name = 'creacion/asignacion_list.html'
    context_object_name = 'asignaciones'

class AsignacionTareaCreate(CreateView):
    model = AsignacionTarea
    template_name = 'creacion/asignacion_form.html'
    fields = ['observaciones', 'fecha_asignacion']
    success_url = reverse_lazy('asignacion_list')

class ComentarioList(ListView):
    model = Comentario
    template_name = 'creacion/comentario_list.html'
    context_object_name = 'comentarios'

class ComentarioCreate(CreateView):
    model = Comentario
    template_name = 'creacion/comentario_form.html'
    fields = ['contenido']
    success_url = reverse_lazy('comentario_list')