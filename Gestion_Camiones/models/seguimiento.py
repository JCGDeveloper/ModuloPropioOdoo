from odoo import models, fields

class Seguimiento(models.Model):
    _name = "paqueteria.seguimiento"
    _description = "Actualización de Envío"

    paquete_id = fields.Many2one(
        "paqueteria.paquete",
        string="Paquete",
        required=True
    )

    fecha = fields.Date(
        string="Fecha de actualización",
        required=True,
        default=fields.Date.today
    )

    estado = fields.Selection(
        [
            ('en_transito', 'En tránsito'),
            ('en_reparto', 'En reparto'),
            ('entregado', 'Entregado'),
            ('incidencia', 'Incidencia'),
        ],
        string="Estado",
        required=True
    )

    notas = fields.Text(string="Notas adicionales")
