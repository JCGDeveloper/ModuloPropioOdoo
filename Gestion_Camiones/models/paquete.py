from odoo import models, fields, api

class Paquete(models.Model):
    _name = 'paqueteria.paquete'
    _description = 'Paquete'
    _rec_name = 'tracking_number'

    tracking_number = fields.Char(string='N.º de seguimiento', required=True)

    remitente_id = fields.Many2one('res.partner', string='Remitente')
    destinatario_id = fields.Many2one('res.partner', string='Destinatario')
    pais_id = fields.Many2one('res.country', string='País')
    region_id = fields.Many2one('res.country.state', string='Región/Provincia')

    municipio = fields.Char(string='Municipio')
    calle = fields.Char(string='Calle')
    numero = fields.Char(string='Número')
    info_adicional = fields.Text(string='Información adicional')

    camion_id = fields.Many2one('paqueteria.camion', string='Camión')

    actualizaciones_ids = fields.One2many(
        'paqueteria.seguimiento',
        'paquete_id',
        string='Seguimiento'
    )

    last_update = fields.Datetime(string='Última actualización', compute='_compute_last_update', store=True)

    @api.depends('actualizaciones_ids.fecha')
    def _compute_last_update(self):
        for record in self:
            record.last_update = max(record.actualizaciones_ids.mapped('fecha')) if record.actualizaciones_ids else False
