from django.urls import path
from . import views

urlpatterns = [
    # URL para el modelo Usuario
    path('usuarios/', views.UsuarioList.as_view(), name='usuario_list'),  # Listar usuarios
    path('usuarios/nuevo/', views.UsuarioCreate.as_view(), name='usuario_create'),  # Crear usuario

    # URL para el modelo Proyecto
    path('proyectos/', views.ProyectoList.as_view(), name='proyecto_list'),  # Listar proyectos
    path('proyectos/nuevo/', views.ProyectoCreate.as_view(), name='proyecto_create'),  # Crear proyecto

    # URL para el modelo Tarea
    path('tareas/', views.TareaList.as_view(), name='tarea_list'),  # Listar tareas
    path('tareas/nuevo/', views.TareaCreate.as_view(), name='tarea_create'),  # Crear tarea

    # URL para el modelo Etiqueta
    path('etiquetas/', views.EtiquetaList.as_view(), name='etiqueta_list'),  # Listar etiquetas
    path('etiquetas/nuevo/', views.EtiquetaCreate.as_view(), name='etiqueta_create'),  # Crear etiqueta

    # URL para el modelo Asignación de Tarea
    path('asignaciones/', views.AsignacionTareaList.as_view(), name='asignacion_list'),  # Listar asignaciones
    path('asignaciones/nuevo/', views.AsignacionTareaCreate.as_view(), name='asignacion_create'),  # Crear asignación

    # URL para el modelo Comentario
    path('comentarios/', views.ComentarioList.as_view(), name='comentario_list'),  # Listar comentarios
    path('comentarios/nuevo/', views.ComentarioCreate.as_view(), name='comentario_create'),  # Crear comentario
]