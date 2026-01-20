# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    dni = fields.Char(string="DNI", help="Documento Nacional de Identidad (8 números + Letra)")
    nss = fields.Char(string="NSS", help="Número de la Seguridad Social (12 dígitos)")

    @api.constrains('dni')
    def _check_dni(self):
        for record in self:
            if record.dni:
                if not re.match(r'^\d{8}[A-Z]$', record.dni):
                    raise ValidationError("El DNI debe tener 8 dígitos y una letra mayúscula (ej: 12345678Z).")
                
                numeros = int(record.dni[:8])
                letra = record.dni[8]
                letras_validas = "TRWAGMYFPDXBNJZSQVHLCKE"
                
                if letras_validas[numeros % 23] != letra:
                    raise ValidationError(f"La letra del DNI es incorrecta. Debería ser {letras_validas[numeros % 23]}.")

    @api.constrains('nss')
    def _check_nss(self):
        for record in self:
            if record.nss:
                # Eliminar espacios o guiones si los hubiera, aunque asumimos entrada limpia o añadimos limpieza
                nss_clean = record.nss.replace(" ", "").replace("-", "")
                
                if not nss_clean.isdigit() or len(nss_clean) != 12:
                     raise ValidationError("El NSS debe tener exactamente 12 dígitos numéricos.")

                # Algoritmo: (2 dígitos provincia + 8 dígitos número) % 97 == 2 dígitos control
                base_number = int(nss_clean[:10])
                control_digit = int(nss_clean[10:])
                
                # Odoo a veces recomienda usar el algoritmo específico, pero el enunciado pide:
                # NSS tiene 12 caracteres... 
                # Vamos a usar la validación estándar A % 97 == B
                if base_number % 97 != control_digit:
                    raise ValidationError(f"NSS inválido. El dígito de control no coincide. Valor calculado: {base_number % 97:02d}")
