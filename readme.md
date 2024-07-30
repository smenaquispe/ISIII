## Postman:

### Gestion Presupuestal
```json
{
	"info": {
		"_postman_id": "19771cc6-2552-4d63-8ccf-5465cbc6a32f",
		"name": "Gestion_Presupuestal",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "37302820",
		"_collection_link": "https://www.postman.com/tecla-industries/workspace/proyecto-sedapal-is3/collection/37308430-19771cc6-2552-4d63-8ccf-5465cbc6a32f?action=share&source=collection_link&creator=37302820"
	},
	"item": [
		{
			"name": "solicitar_presupuesto",
			"event": [
				{
					"listen": "test",
					"script": {
						"exec": [
							"pm.test(\"Status code is 201\", function () {\r",
							"    pm.response.to.have.status(201);\r",
							"});\r",
							"\r",
							"pm.test(\"Response has 'Presupuesto solicitado'\", function () {\r",
							"    var jsonData = pm.response.json();\r",
							"    pm.expect(jsonData.message).to.eql(\"Presupuesto solicitado\");\r",
							"});\r",
							"\r",
							"pm.test(\"Response contains ID\", function () {\r",
							"    var jsonData = pm.response.json();\r",
							"    pm.expect(jsonData).to.have.property(\"id\");\r",
							"});\r",
							""
						],
						"type": "text/javascript",
						"packages": {}
					}
				}
			],
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"nombre\": \"Presupuesto de Marketing\",\r\n    \"descripcion\": \"Presupuesto anual para el departamento de marketing\",\r\n    \"importe\": 50000.0\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/presupuesto/solicitar",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"presupuesto",
						"solicitar"
					]
				}
			},
			"response": []
		},
		{
			"name": "validar_presupuesto",
			"event": [
				{
					"listen": "test",
					"script": {
						"exec": [
							"pm.test(\"Status code is 200\", function () {\r",
							"    pm.response.to.have.status(200);\r",
							"});\r",
							"\r",
							"pm.test(\"Response has 'Presupuesto válido'\", function () {\r",
							"    var jsonData = pm.response.json();\r",
							"    pm.expect(jsonData.message).to.eql(\"Presupuesto válido\");\r",
							"});\r",
							"\r",
							"pm.test(\"Response contains complete property\", function () {\r",
							"    var jsonData = pm.response.json();\r",
							"    pm.expect(jsonData).to.have.property(\"completo\");\r",
							"});\r",
							""
						],
						"type": "text/javascript",
						"packages": {}
					}
				}
			],
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/presupuesto/validar/1",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"presupuesto",
						"validar",
						"1"
					]
				}
			},
			"response": []
		}
	]
}

```

### Planeamiento Estrategico

```json
{
    "info": {
        "_postman_id": "aef31937-b308-4266-b3c8-2e994db1bc4b",
        "name": "Planeamiento_Estrategico",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
        "_exporter_id": "37308775",
        "_collection_link": "https://www.postman.com/tecla-industries/workspace/proyecto-sedapal-is3/collection/37308775-aef31937-b308-4266-b3c8-2e994db1bc4b?action=share&source=collection_link&creator=37308775"
    },
    "item": [
        {
            "name": "Crear Estrategia",
            "request": {
                "method": "GET",
                "header": []
            },
            "response": []
        },
        {
            "name": "Corregir Estrategia",
            "request": {
                "method": "GET",
                "header": []
            },
            "response": []
        }
    ]
}
```
### Gestion de Proyectos

```json
{
	"info": {
		"_postman_id": "de420562-6c0d-43f4-a2f8-e8eaad410450",
		"name": "Gestion de Proyectos",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "37264479"
	},
	"item": [
		{
			"name": "crearProyecto",
			"event": [
				{
					"listen": "test",
					"script": {
						"exec": [
							"pm.test(\"Status code is 201\", function () {\r",
							"    pm.response.to.have.status(201);\r",
							"});\r",
							"\r",
							"pm.test(\"Proyecto creado'\", function () {\r",
							"    var jsonData = pm.response.json();\r",
							"    pm.expect(jsonData.message).to.eql(\"Proyecto creado\");\r",
							"});\r",
							"\r",
							"pm.test(\"Response time is less than 200ms\", function () {\r",
							"    pm.expect(pm.response.responseTime).to.be.below(200);\r",
							"});\r",
							"\r",
							"pm.test(\"Successful POST request\", function () {\r",
							"    pm.expect(pm.response.code).to.be.oneOf([201, 202]);\r",
							"});\r",
							"\r",
							"pm.test(\"Status code name has string\", function () {\r",
							"    pm.response.to.have.status(\"CREATED\");\r",
							"});\r",
							""
						],
						"type": "text/javascript",
						"packages": {}
					}
				}
			],
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"id\" : 1,\r\n    \"nombre\": \"Ampliacion de tuberias\",\r\n    \"descripcion\": \"Nueva obra en Arequipa\",\r\n    \"estado\": \"No Iniciado\",\r\n    \"tipo\": \"Construccion\",\r\n    \"presupuesto\": 150.0,\r\n    \"fecha_inicio\": \"07/05/2020\",\r\n    \"fecha_fin\":\"20/02/2021\",\r\n    \"responsable\":\"Empresa de Construccion\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/proyecto/crear",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"proyecto",
						"crear"
					]
				}
			},
			"response": []
		},
		{
			"name": "buscarProyectoExistente",
			"event": [
				{
					"listen": "test",
					"script": {
						"exec": [
							"//CASO: BUSQUEDA DE UN PROYECTO EXISTENTE\r",
							"pm.test(\"Status code is 200\", function () {\r",
							"    pm.response.to.have.status(200);\r",
							"});\r",
							"\r",
							"pm.test(\"Proyecto creado'\", function () {\r",
							"    var jsonData = pm.response.json();\r",
							"    pm.expect(jsonData.id).to.eql(\"1\");\r",
							"});\r",
							"\r",
							"pm.test(\"Response time is less than 200ms\", function () {\r",
							"    pm.expect(pm.response.responseTime).to.be.below(200);\r",
							"});\r",
							"\r",
							"pm.test(\"Status code name has string\", function () {\r",
							"    pm.response.to.have.status(\"OK\");\r",
							"});"
						],
						"type": "text/javascript",
						"packages": {}
					}
				}
			],
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/proyecto/buscar?id=1",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"proyecto",
						"buscar"
					],
					"query": [
						{
							"key": "id",
							"value": "1"
						}
					]
				}
			},
			"response": []
		},
		{
			"name": "buscarProyectoInexistente",
			"event": [
				{
					"listen": "test",
					"script": {
						"exec": [
							"//CASO: BUSQUEDA DE UN PROYECTO INEXISTENTE\r",
							"pm.test(\"Status code is 404\", function () {\r",
							"    pm.response.to.have.status(404);\r",
							"});\r",
							"\r",
							"pm.test(\"Proyecto creado'\", function () {\r",
							"    var jsonData = pm.response.json();\r",
							"    pm.expect(jsonData.error).to.eql(\"Proyecto no encontrado\");\r",
							"});\r",
							"\r",
							"\r",
							"pm.test(\"Status code name has string\", function () {\r",
							"    pm.response.to.have.status(\"NOT FOUND\");\r",
							"});"
						],
						"type": "text/javascript",
						"packages": {}
					}
				}
			],
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/proyecto/buscar?id=100",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"proyecto",
						"buscar"
					],
					"query": [
						{
							"key": "id",
							"value": "100"
						}
					]
				}
			},
			"response": []
		}
	]
}
```

![alt text](Main.png)
