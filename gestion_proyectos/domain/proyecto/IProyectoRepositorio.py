# Ejemplo de datos de proyectos
proyectos = [
    {
        "id": "1",
        "nombre": "Proyecto de mejora de redes",
        "descripcion": "Optimización de la red de distribución de agua en el distrito central.",
        "estado": "En progreso",
        "tipo": "Infraestructura",
        "presupuesto": 5000000,
        "fecha_inicio": "2024-01-15",
        "fecha_fin": "2024-12-31",
        "responsable": "Juan Perez"
    },
    {
        "id": "2",
        "nombre": "Implementación de sistemas de monitoreo",
        "descripcion": "Instalación de sensores de presión y caudal en puntos estratégicos de la red.",
        "estado": "Planificación",
        "tipo": "Tecnología",
        "presupuesto": 1200000,
        "fecha_inicio": "2024-09-01",
        "fecha_fin": "2025-03-01",
        "responsable": "Ana Gomez"
    },
    {
        "id": "3",
        "nombre": "Campaña de sensibilización sobre el uso del agua",
        "descripcion": "Iniciativa para educar a la población sobre el uso eficiente del agua.",
        "estado": "Completado",
        "tipo": "Educación",
        "presupuesto": 300000,
        "fecha_inicio": "2023-06-01",
        "fecha_fin": "2023-12-31",
        "responsable": "Carlos Fernandez"
    }
]

class IProyectoRepositorio:
    def adicionar(self, proyecto):
        pass

    def actualizar(self, proyecto):
        pass

    def eliminar(self, proyecto):
        pass

    def buscar(self, id):
        # Buscar el proyecto por id
        proyecto = next((p for p in proyectos if p["id"] == id), None)
        return proyecto
        
