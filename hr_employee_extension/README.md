# Tarea 13: Extensión de Módulos (El Hackeo a RRHH 🚀)

¡Buenas! A ver, aquí dejo lo que hay que hacer para la Tarea 13, explicado en cristiano para que no nos liemos. Básicamente vamos a "tunear" el módulo de empleados para que Odoo se trague los DNI y los números de la Seguridad Social de España bien validados.

## ¿Qué hay que hacer? 📝

Hay que crear un módulo nuevo (yo lo he llamado `hr_employee_extension`) que herede del de empleados (`hr.employee`). Nada de tocar el código base de Odoo que luego se rompe todo en las actualizaciones, ¿eh? Usamos la herencia como buenos ciudadanos.

### 1. El Módulo 📦
Creamos la carpeta del módulo con su `__manifest__.py` y el `__init__.py`. En el manifiesto poner que dependemos de `hr` porque sin empleados no hay paraíso.

### 2. Los Campos Nuevos (Python) 🐍
En `models/hr_employee.py` extendemos la clase `hr.employee`:
- **DNI**: Un campo Char. Ojo, tiene validación.
  - La letra tiene que cuadrar. Dividimos el número entre 23 y el resto nos dice la letra (buscad la tabla esa de `TRWAGMY...`). Si no cuadra, `ValidationError` al canto.
- **NSS (Seguridad Social)**: Otro Char.
  - Formato: 2 dígitos provincia + 8 número + 2 control.
  - El truco: `(Provincia + Número) % 97` tiene que coincidir con los dígitos de control. Si no, ¡error!

### 3. La Vista (XML) 👁️
En `views/hr_employee_views.xml` heredamos la vista `hr.view_employee_form`.
Usamos **XPath** (esa cosa rara) para meter nuestros campos `dni` y `nss` donde queden bonitos. Por ejemplo, después del email o el teléfono.

```xml
<xpath expr="//field[@name='mobile_phone']" position="after">
    <field name="dni"/>
    <field name="nss"/>
</xpath>
```

### 4. Seguridad 🔒
No os olvidéis del `ir.model.access.csv` aunque sea heredado, a veces da guerra si añadimos modelos nuevos, pero aquí como heredamos igual nos libramos, pero mejor revisar si hace falta dar permisos. (En este caso al solo extender campos en modelo existente, los permisos del modelo base suelen valer, pero lo revisamos).

## Resumen para vagos
1. Crear módulo.
2. `_inherit = 'hr.employee'`.
3. Meter campos `dni` y `nss`.
4. Meter funciones `@api.constrains` para validar matemáticas.
5. XML con XPath para que se vean.
6. Instalar y probar que si metes un DNI falso te grite.

¡Ale, a currar! 💪
