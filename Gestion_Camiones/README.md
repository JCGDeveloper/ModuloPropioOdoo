# Módulo Paquetería y Gestión de Flota

## Nombre del Módulo
**paqueteria_gestion**

## Autor
Joaquin Carrasco

## Versión
1.0

## Descripción
Este módulo permite gestionar:

- **Paquetes**: con información de remitente, destinatario y dirección de entrega.  
- **Seguimiento**: registro de cada paquete con estado, fecha y notas adicionales.  
- **Camiones**: gestión de la flota, conductores actuales y anteriores, paquetes transportados y mantenimiento.  

Está diseñado para **Odoo 15+** y es compatible con la interfaz web estándar de Odoo.

---

## Modelos

### 1. `paqueteria.paquete`
Representa un paquete que se va a enviar.

**Campos principales:**

| Campo              | Tipo                          | Descripción                                |
|-------------------|-------------------------------|--------------------------------------------|
| tracking_number    | Char                          | Número de seguimiento único del paquete    |
| remitente_id       | Many2one(res.partner)         | Cliente remitente                          |
| destinatario_id    | Many2one(res.partner)         | Cliente destinatario                        |
| pais_id            | Many2one(res.country)         | País de entrega                             |
| region_id          | Many2one(res.country.state)   | Región/Provincia de entrega                |
| municipio          | Char                          | Municipio de entrega                        |
| calle              | Char                          | Calle de entrega                            |
| numero             | Char                          | Número de la dirección                      |
| info_adicional     | Text                          | Información adicional de la dirección      |
| camion_id          | Many2one(paqueteria.camion)   | Camión que transporta el paquete           |
| actualizaciones_ids| One2many(paqueteria.seguimiento)| Lista de actualizaciones del paquete    |
| last_update        | Datetime (compute)            | Última actualización registrada            |

---

### 2. `paqueteria.seguimiento`
Registro de actualizaciones de un paquete.

**Campos principales:**

| Campo       | Tipo        | Descripción                                   |
|------------|------------|-----------------------------------------------|
| paquete_id  | Many2one(paqueteria.paquete) | Paquete asociado        |
| fecha       | Date       | Fecha de la actualización                      |
| estado      | Selection  | Estado del paquete (`en_transito`, `en_reparto`, `entregado`, `incidencia`) |
| notas       | Text       | Notas adicionales                              |

---

### 3. `paqueteria.camion`
Representa un camión de la flota de transporte.

**Campos principales:**

| Campo                   | Tipo                     | Descripción                               |
|------------------------|--------------------------|-------------------------------------------|
| matricula               | Char                     | Matrícula del camión (única)             |
| conductor_actual_id     | Many2one(hr.employee)    | Conductor actual                          |
| conductores_antiguos_ids| Many2many(hr.employee)   | Conductores anteriores                    |
| fecha_itv               | Date                     | Fecha de la última ITV                     |
| notas_mantenimiento     | Text                     | Notas de mantenimiento                     |
| paquetes_ids            | One2many(paqueteria.paquete) | Paquetes transportados                 |

---

## Vistas
El módulo incluye vistas tipo **form** y **list** para cada modelo:

- `paquete_views.xml`
- `seguimiento_views.xml`
- `camion_views.xml`

Y un menú principal y submenús en:

- `menus_views.xml`

---

## Seguridad
El módulo incluye un archivo `ir.model.access.csv` para controlar permisos básicos de lectura, creación, edición y borrado para:

- `paqueteria.paquete`
- `paqueteria.seguimiento`
- `paqueteria.camion`

Se recomienda revisar y ajustar permisos según los roles de los usuarios.

---

## Instalación
1. Copia la carpeta del módulo dentro de tu directorio de addons.  
2. Reinicia el servidor de Odoo.  
3. Actualiza la lista de módulos.  
4. Instala **Paquetería - Gestión de paquetes y flota**.

---

## Uso
1. Accede al menú **Paquetería** en la barra lateral.  
2. Selecciona **Paquetes**, **Seguimiento** o **Camiones**.  
3. Crea, edita o elimina registros según tu necesidad.  
4. Los paquetes pueden vincularse a camiones y registrar actualizaciones de seguimiento.  
5. Los camiones muestran los paquetes que transportan y sus conductores.

---

## Notas Técnicas
- El campo `last_update` en `paqueteria.paquete` se calcula automáticamente a partir de las actualizaciones.  
- La relación entre paquetes y camiones se realiza mediante un `Many2one` y un `One2many`.  
- Las listas de antiguos conductores se guardan en un `Many2many`.
