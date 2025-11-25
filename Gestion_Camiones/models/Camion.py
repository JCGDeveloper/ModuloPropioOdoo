
from odoo import models, fields


class Camion(models.Model):
    _name = "paqueteria_camion"
    _description = "Camión de la Flota"

    matricula = fields.Char(
        string="Número de matrícula",
        required=True
    )

    conductor_actual_id = fields.Many2one(
        "hr.employee",
        string="Conductor actual"
    )

    conductores_antiguos_ids = fields.Many2many(
        "hr.employee",
        string="Antiguos conductores"
    )

    fecha_itv = fields.Date(
        string="Fecha de la última ITV"
    )

    notas_mantenimiento = fields.Text(
        string="Notas de mantenimiento"
    )

    paquetes_ids = fields.One2many(
        "paqueteria_paquete",
        "camion_id",
        string="Paquetes transportados"
    )

    _sql_constraints = [
        (
            'matricula_unique',
            'unique(matricula)',
            'La matrícula del camión debe ser única.'
        )
    ]
