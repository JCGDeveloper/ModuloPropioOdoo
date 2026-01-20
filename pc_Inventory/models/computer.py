# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PCComputer(models.Model):
    _name = 'pc.computer'
    _description = 'Ordenador de la Empresa'

    name = fields.Char(string='Número de equipo', required=True)
    user_id = fields.Many2one('res.users', string='Usuario')
    component_ids = fields.Many2many('pc.component', string='Componentes')
    last_update = fields.Date(string='Última modificación')
    total_price = fields.Monetary(
        string='Precio total',
        currency_field='currency_id',
        compute='_compute_total_price',
        store=True
    )
    incident = fields.Text(string='Incidencias')
    tag_ids = fields.Many2many('pc.computer.tag', string='Sistemas Operativos')

    currency_id = fields.Many2one(
        'res.currency',
        string='Moneda',
        default=lambda self: self.env.company.currency_id.id
    )

    @api.depends('component_ids.price')
    def _compute_total_price(self):
        for record in self:
            record.total_price = sum(record.component_ids.mapped('price'))

    @api.constrains('last_update')
    def _check_last_update(self):
        for record in self:
            if record.last_update and record.last_update > fields.Date.today():
                raise ValidationError("La fecha no puede ser futura")


