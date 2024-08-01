import unittest
from app import app, db
from models import Estrategia
from repositories import EstrategiaRepository

class EstrategiaTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_estrategia(self):
        response = self.app.post('/estrategias', json={
            'nombre': 'Estrategia Test',
            'descripcion': 'Descripción Test'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Estrategia creada', response.get_data(as_text=True))

    def test_read_estrategia(self):
        with app.app_context():
            estrategia = Estrategia(nombre='Estrategia Test', descripcion='Descripción Test')
            db.session.add(estrategia)
            db.session.commit()

            estrategia_id = estrategia.id

        response = self.app.get(f'/estrategias/{estrategia_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Estrategia Test', response.get_data(as_text=True))

    def test_update_estrategia(self):
        with app.app_context():
            estrategia = Estrategia(nombre='Estrategia Test', descripcion='Descripción Test')
            db.session.add(estrategia)
            db.session.commit()

            estrategia_id = estrategia.id

        response = self.app.put(f'/estrategias/{estrategia_id}', json={
            'nombre': 'Estrategia Actualizada',
            'descripcion': 'Descripción Actualizada'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Estrategia actualizada', response.get_data(as_text=True))

    def test_delete_estrategia(self):
        with app.app_context():
            estrategia = Estrategia(nombre='Estrategia Test', descripcion='Descripción Test')
            db.session.add(estrategia)
            db.session.commit()

            estrategia_id = estrategia.id

        response = self.app.delete(f'/estrategias/{estrategia_id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
