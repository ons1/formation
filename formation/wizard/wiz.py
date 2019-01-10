from openerp import models, fields, api
from openerp.exceptions import Warning, AccessError, ValidationError
import time
from datetime import date, datetime
from openerp.tools.translate import _




class wiz_calc_age(models.TransientModel):
    _name = 'calc.age.wiz'
    
    from_date = fields.Date("From Date", required=True)
    
    @api.multi
    def calc_age(self):
        hr_obj = self.env['res.partner']
        for rec in self:
            student_ids = hr_obj.search([('birthday','<=',rec.from_date)])
            for student in  student_ids:
                birthday = student.birthday      
                if birthday :
                    student.age = (datetime.now() - datetime.strptime(birthday, '%Y-%m-%d')).days / 365
        return True