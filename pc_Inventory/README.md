# PC Inventory - Gestión de Ordenadores y Componentes

## Descripción del Módulo

Este módulo permite gestionar el inventario de ordenadores de una empresa, incluyendo sus componentes, asignación de usuarios, mantenimiento y sistemas operativos instalados.

## Funcionalidades

### 1. Modelo Componente (`pc.component`)

Gestiona los componentes de hardware que pueden formar parte de los ordenadores.

**Campos:**
- **Nombre técnico** (Char, requerido): Nombre del componente (ej: "Intel i7-9700K", "16GB RAM DDR4")
- **Especificaciones** (Text): Descripción detallada del componente
- **Precio** (Monetary): Precio del componente en la moneda de la empresa

**Uso:**
- Crear componentes reutilizables que pueden ser asignados a múltiples ordenadores
- Los componentes se pueden usar en varios ordenadores (relación Many2many)

### 2. Modelo Ordenador (`pc.computer`)

Gestiona los ordenadores de la empresa con toda su información.

**Campos:**
- **Número de equipo** (Char, requerido): Identificador único del ordenador
- **Usuario** (Many2one): Usuario asignado al ordenador (relación con `res.users`)
- **Componentes** (Many2many): Lista de componentes que tiene el ordenador
- **Última modificación** (Date): Fecha de última actualización del equipo
- **Precio total** (Monetary, calculado): Suma automática del precio de todos los componentes
- **Incidencias** (Text): Registro de problemas o mantenimientos del equipo
- **Sistemas Operativos** (Many2many con tags): SO instalados (BONUS - widget tags)

**Funcionalidades especiales:**

#### Cálculo automático del precio total
El campo `precio_total` se calcula automáticamente sumando el precio de todos los componentes asignados al ordenador. Se actualiza cada vez que se modifican los componentes.

```python
@api.depends('component_ids.price')
def _compute_total_price(self):
    for record in self:
        record.total_price = sum(record.component_ids.mapped('price'))
```

#### Validación de fecha
El campo `last_update` tiene una restricción que impide introducir fechas futuras:

```python
@api.constrains('last_update')
def _check_last_update(self):
    for record in self:
        if record.last_update and record.last_update > fields.Date.today():
            raise ValidationError("La fecha no puede ser futura")
```

### 3. Modelo Etiqueta de SO (`pc.computer.tag`) - BONUS

Gestiona los sistemas operativos que pueden estar instalados en los ordenadores.

**Campos:**
- **Sistema Operativo** (Char, requerido): Nombre del SO (ej: "Windows 11", "Ubuntu 22.04", "macOS")

**Uso:**
- Se muestra como tags en el formulario del ordenador
- Permite asignar múltiples sistemas operativos a un mismo ordenador

## Relaciones entre Modelos

### Many2one: Ordenador → Usuario
- Un ordenador puede tener **un solo usuario** asignado
- Un usuario puede tener **múltiples ordenadores**
- Campo: `user_id = fields.Many2one('res.users', string='Usuario')`

### Many2many: Ordenador ↔ Componente
- Un ordenador puede tener **múltiples componentes**
- Un componente puede estar en **múltiples ordenadores**
- Campo: `component_ids = fields.Many2many('pc.component', string='Componentes')`

### Many2many: Ordenador ↔ Etiquetas SO
- Un ordenador puede tener **múltiples sistemas operativos**
- Un SO puede estar en **múltiples ordenadores**
- Campo: `tag_ids = fields.Many2many('pc.computer.tag', string='Sistemas Operativos')`
- Widget: `many2many_tags` para mostrar como etiquetas visuales

## Vistas

### Vista de Lista (Componentes)
- Muestra: Nombre técnico, Precio
- Permite crear, editar y eliminar componentes

### Vista de Formulario (Componentes)
- Campos principales: Nombre, Precio
- Campo de texto para especificaciones

### Vista de Lista (Ordenadores)
- Muestra: Número de equipo, Usuario, Precio total, Última modificación
- Permite ver todos los ordenadores de la empresa

### Vista de Formulario (Ordenadores)
- **Grupo 1**: Información básica (Número, Usuario, Fecha)
- **Grupo 2**: Precio total (solo lectura, calculado automáticamente)
- **Grupo 3**: Sistemas Operativos (widget tags)
- **Grupo 4**: Componentes (widget tags)
- **Pestaña Incidencias**: Campo de texto para registrar problemas

## Instalación

1. Copia el módulo a la carpeta de addons de Odoo
2. Actualiza la lista de aplicaciones en Odoo
3. Busca "PC Inventory" en Aplicaciones
4. Haz clic en "Instalar"

## Uso del Módulo

### Crear un Componente
1. Ve a **Inventario PC** → **Componentes**
2. Haz clic en **Crear**
3. Introduce el nombre técnico, precio y especificaciones
4. Guarda

### Crear un Ordenador
1. Ve a **Inventario PC** → **Ordenadores**
2. Haz clic en **Crear**
3. Introduce el número de equipo
4. Selecciona el usuario asignado
5. Añade componentes (se calculará el precio total automáticamente)
6. Añade sistemas operativos usando las etiquetas
7. Registra incidencias en la pestaña correspondiente
8. Guarda

### Asignar Componentes a un Ordenador
- En el formulario del ordenador, haz clic en el campo "Componentes"
- Selecciona los componentes que tiene el ordenador
- El precio total se actualizará automáticamente

### Añadir Sistemas Operativos (BONUS)
- En el formulario del ordenador, haz clic en el campo "Sistemas Operativos"
- Escribe el nombre del SO y presiona Enter (se creará automáticamente)
- O selecciona uno existente de la lista
- Se mostrarán como etiquetas visuales

## Seguridad

El módulo tiene permisos configurados para que todos los usuarios internos (`base.group_user`) puedan:
- Leer componentes y ordenadores
- Crear nuevos registros
- Editar registros existentes
- Eliminar registros

## Estructura del Código

```
pc_Inventory/
├── __init__.py                 # Inicialización del módulo
├── __manifest__.py             # Configuración y metadatos
├── models/
│   ├── __init__.py            # Importa los modelos
│   ├── component.py           # Modelo Componente
│   ├── computer.py            # Modelo Ordenador
│   └── computer_tag.py        # Modelo Etiqueta SO (BONUS)
├── security/
│   └── ir.model.access.csv    # Permisos de acceso
├── views/
│   ├── component_views.xml    # Vistas de Componentes
│   └── computer_views.xml     # Vistas de Ordenadores
└── README.md                  # Esta documentación
```

## Explicación del Código

### Decorador @api.depends
Se usa para indicar que un campo calculado depende de otros campos. Cuando estos cambian, se recalcula automáticamente:

```python
@api.depends('component_ids.price')
def _compute_total_price(self):
```

### Decorador @api.constrains
Se usa para validar datos antes de guardarlos. Si la validación falla, lanza un error:

```python
@api.constrains('last_update')
def _check_last_update(self):
```

### Widget many2many_tags
Permite mostrar relaciones Many2many como etiquetas visuales en lugar de una lista desplegable. Es más intuitivo para el usuario:

```xml
<field name="tag_ids" widget="many2many_tags"/>
```

## Requisitos

- Odoo 18.0 o superior
- Módulo base de Odoo

## Autor

Joaquin

## Licencia

LGPL-3


