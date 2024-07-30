from .models import Riesgo, db_riesgos

class RiesgosRepository:
    #def __init__(self):
        #self.riesgos = []

    def adicionar(self, riesgo: Riesgo) -> None:
        #self.riesgos.append(riesgo)
        db_riesgos.session.add(riesgo)
        db_riesgos.session.commit()

    def eliminar(self, id:str) -> None:
        #self.riesgos = [r for r in self.riesgos if r.id != id]
        riesgo = self.buscar(id)
        if riesgo:
            db_riesgos.session.delete(riesgo)
            db_riesgos.session.commit()

    def actualizar(self, riesgo: Riesgo) -> None:
        #for i, r in enumerate(self.riesgos):
            #if r.id == riesgo.id:
                #self.riesgos[i] = riesgo
        db_riesgos.session.merge(riesgo)
        db_riesgos.session.commit()

    def buscar(self, id) -> Riesgo:
        #for r in self.riesgos:
            #if r.id == id:
                #return r
        return db_riesgos.session.query(Riesgo).filter_by(id=id).first()

    def obtener_todos(self) -> list:
        return Riesgo.query.all()
