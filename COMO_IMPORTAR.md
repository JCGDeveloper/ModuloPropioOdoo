# 📦 Cómo importar el módulo desde la interfaz de Odoo

## Archivo ZIP creado:
**Ubicación:** `/home/joaquin/odoo/ModuloPropioOdoo/mi_modulo.zip`

## Pasos para importar:

### 1. Accede a Odoo
```
http://localhost:8069?debug=1
```
(El `?debug=1` activa el modo desarrollador)

### 2. Ve a Aplicaciones
- Menú principal → **"Aplicaciones"** o **"Apps"**

### 3. Importa el módulo
- Haz clic en el botón **"Importar módulo"** o **"Import Module"** (arriba a la derecha)
- O busca en el menú: **"Aplicaciones" → "Importar módulo"**

### 4. Selecciona el archivo ZIP
- Haz clic en **"Seleccionar archivo"** o **"Choose File"**
- Navega a: `/home/joaquin/odoo/ModuloPropioOdoo/mi_modulo.zip`
- O arrastra el archivo ZIP a la zona de carga

### 5. Instala el módulo
- Después de importar, busca **"Módulo Personalizado Joaquin"** en la lista
- Haz clic en **"Instalar"**

## ✅ Verificación

Una vez instalado, deberías ver:
- **Menú:** "Menú desplegable" → "Barra de navegación" → "Test action"
- **Vista de lista:** Con campos name, active, date_created
- **Vista de formulario:** Para crear/editar registros

## 🔄 Si necesitas actualizar el módulo

Si haces cambios y quieres actualizar:
1. Vuelve a crear el ZIP (o usa el comando de abajo)
2. En Odoo: **Aplicaciones** → Busca el módulo → **"Actualizar"**

## 📝 Comando para recrear el ZIP

Si necesitas recrear el ZIP después de hacer cambios:

```bash
cd /home/joaquin/odoo/ModuloPropioOdoo
rm mi_modulo.zip
zip -r mi_modulo.zip mi_modulo/ -x "*.pyc" -x "__pycache__/*"
```

