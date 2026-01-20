# -*- coding: utf-8 -*-

from odoo import models, fields


class PCComputerTag(models.Model):
    _name = 'pc.computer.tag'
    _description = 'Etiqueta de Sistema Operativo'

    name = fields.Char(string='Sistema Operativo', required=True)


