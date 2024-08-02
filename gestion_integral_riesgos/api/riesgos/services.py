from gestion_integral_riesgos.api.riesgos.models import Riesgo

class MonitoreoService:
    def __init__(self, riesgo_repo):
        self.riesgo_repo = riesgo_repo

    def generar_informe(self) -> list:

        riesgos = self.riesgo_repo.obtener_todos()
        informe = []
        for idx, riesgo in enumerate(riesgos, 1):
            riesgo_info = {
                'indice': idx,
                'id': riesgo.id,
                'nombre': riesgo.nombre,
                'descripcion': riesgo.descripcion,
                'probabilidad': riesgo.probabilidad,
                'prioridad_alta': riesgo.prioridad_alta
            }
            informe.append(riesgo_info)
        
        return informe

    def identificar_mejora(self) -> None:
        pass
