# ModuloPropioOdoo

## Instalación del Módulo en Odoo

Este directorio contiene módulos personalizados de Odoo que están configurados para ser detectados automáticamente por la instancia de Odoo en Docker.

### Estructura

```
ModuloPropioOdoo/
└── mi_modulo/
    ├── __init__.py
    └── __manifest__.py
```

### Pasos para instalar el módulo

1. **Iniciar los contenedores de Odoo:**
   ```bash
   cd /home/joaquin/odoo
   docker compose up -d
   ```
   
   **Nota:** Si usas una versión antigua de Docker, usa `docker-compose` (con guión). Las versiones modernas usan `docker compose` (sin guión).

2. **Acceder a Odoo:**
   - Abre tu navegador en: `http://localhost:8069`
   - Completa la configuración inicial si es la primera vez

3. **Activar el modo desarrollador:**
   - Ve a: **Configuración** → **Activar el modo de desarrollador**
   - O añade `?debug=1` a la URL

4. **Instalar el módulo:**
   - Ve a: **Aplicaciones** (Apps)
   - Busca "Mi Módulo" `__manifest__.py`
   - Haz clic en **Instalar**

El modulo de PC_Inventory :

Lo que hace es poder crear componentes con su precio para luego en ordenadores , poder meter componentes y lo que hace es el dinero de cada componente sumar el total
