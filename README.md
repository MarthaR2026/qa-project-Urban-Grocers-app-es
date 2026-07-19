
# QA Project - Urban Grocers API Automation

## Descripción del proyecto

Este proyecto contiene pruebas automatizadas para validar el funcionamiento de la API de **Urban Grocers**, específicamente el endpoint encargado de la creación de kits asociados a usuarios.

El objetivo principal es verificar que el campo `name` del cuerpo de la solicitud cumpla con las reglas de validación definidas en los requisitos del proyecto, comprobando diferentes escenarios positivos y negativos.

Las pruebas automatizadas validan:

* Creación de kits con nombres válidos.
* Límites de longitud permitidos para el campo `name`.
* Uso de caracteres especiales.
* Uso de espacios.
* Uso de números.
* Envío de solicitudes sin el parámetro requerido.
* Envío de valores con tipos de datos incorrectos.

## Tecnologías utilizadas

* **Python** como lenguaje de programación.
* **Pytest** como framework para ejecución de pruebas automatizadas.
* **Requests** para realizar peticiones HTTP a la API.
* **PyCharm** como entorno de desarrollo.

## Estructura del proyecto

```
qa-project-Urban-Grocers-app-es/
│
├── create_kit_name_kit_test.py    # Casos de prueba automatizados
├── sender_stand_request.py        # Funciones para enviar solicitudes a la API
├── configuration.py               # Configuración de URL y endpoints
├── data.py                        # Datos de prueba y cuerpos de solicitud
└── README.md                      # Documentación del proyecto
```

## Configuración del proyecto

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
```

### 2. Crear y activar un entorno virtual

Crear entorno virtual:

```bash
python -m venv .venv
```

Activar entorno virtual:

**Windows**

```bash
.venv\Scripts\activate
```

### 3. Instalar dependencias

Instalar las librerías necesarias:

```bash
pip install requests
pip install pytest
```

## Ejecución de pruebas

Para ejecutar todos los casos de prueba:

```bash
pytest
```

Para ejecutar un archivo específico:

```bash
pytest create_kit_name_kit_test.py
```

Para obtener información detallada de la ejecución:

```bash
pytest -v
```

## Descripción de los casos de prueba

El archivo `create_kit_name_kit_test.py` contiene pruebas para validar el comportamiento del endpoint de creación de kits:

| Caso | Validación                                                                      |
| ---- | ------------------------------------------------------------------------------- |
| 1    | Creación de kit con un carácter en el nombre                                    |
| 2    | Creación de kit con longitud máxima permitida (511 caracteres)                  |
| 3    | Validación de nombre vacío                                                      |
| 4    | Validación de nombre con longitud superior al límite permitido (512 caracteres) |
| 5    | Uso de caracteres especiales                                                    |
| 6    | Uso de espacios en el nombre                                                    |
| 7    | Uso de números en el nombre                                                     |
| 8    | Solicitud sin el parámetro `name`                                               |
| 9    | Solicitud con tipo de dato incorrecto en `name`                                 |

## Manejo de autenticación

Antes de crear un kit, el proyecto genera un nuevo usuario mediante el endpoint correspondiente y obtiene un token de autenticación.

Este token se utiliza en las solicitudes posteriores mediante el encabezado:

```
Authorization: Bearer <auth_token>
```

## Resultados esperados

Los casos positivos verifican:

* Código de respuesta HTTP `201`.
* Coincidencia entre el nombre enviado y el nombre recibido en la respuesta.

Los casos negativos verifican:

* Código de respuesta HTTP `400` cuando los datos enviados no cumplen con las reglas de validación.

## Notas

Durante la ejecución de las pruebas se verificó el comportamiento real de la API mediante automatización y pruebas manuales en Postman. Algunos escenarios pueden presentar diferencias entre el comportamiento actual del servicio y los códigos de respuesta definidos en los requisitos, por lo que dichos casos deben ser considerados como posibles incidencias del backend.

## Incidencias encontradas durante las pruebas

Durante la ejecución de las pruebas automatizadas se identificaron algunos comportamientos que no coinciden con los resultados esperados definidos en los requisitos del proyecto.

| Caso | Escenario | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|
| 3 | Envío de `name` vacío: `{"name": ""}` | Código 400 | Código 201 | Fallo de validación de API |
| 4 | Envío de `name` con 512 caracteres | Código 400 | Código 201 | Fallo de validación de API |
| 8 | Solicitud sin parámetro `name`: `{}` | Código 400 | Código 500 | Error interno del servidor |
| 9 | Envío de `name` con tipo de dato incorrecto: `{"name": 123}` | Código 400 | Código 201 | Fallo de validación de API |

### Observaciones

- Los casos positivos fueron ejecutados correctamente:
  - Nombre con 1 carácter.
  - Nombre con 511 caracteres.
  - Caracteres especiales.
  - Espacios.
  - Valores numéricos como texto.

- Los casos negativos mostraron diferencias entre el comportamiento esperado y la respuesta real del servicio.

- Las pruebas fueron verificadas tanto mediante automatización con **Pytest** como mediante solicitudes manuales utilizando **Postman**, obteniendo los mismos resultados.

Estos resultados deben considerarse posibles incidencias del backend, ya que la respuesta actual de la API no coincide con los códigos de estado definidos en los requisitos.

## Autor

Martha Ruiz Grupo 74
Proyecto de automatización QA desarrollado como práctica de pruebas API utilizando Python y Pytest. TRIPLETEN
