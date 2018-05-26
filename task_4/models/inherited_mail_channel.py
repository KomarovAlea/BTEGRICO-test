# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from odoo import _, api, models


class Channel(models.Model):
    _inherit = 'mail.channel'

    @api.multi
    def get_new_followers(self):
        last_month = datetime.today() + timedelta(days=-30)
        query = """SELECT * 
            FROM mail_channel_partner AS fl
            WHERE fl.channel_id = %s
                AND fl.create_date >= %s;"""
        self.env.cr.execute(query, (self.id, last_month))
        followers = self.env.cr.dictfetchall()
        for fl in followers:
            pr = self.env['res.partner'].browse(fl['partner_id']).name_get()[0][1]
            print(pr, fl)
        print('Exit(%s)' % last_month)