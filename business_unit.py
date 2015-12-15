from openerp.osv import osv, fields



class business_unit(osv.osv):
    _name = "business.unit"

    _description = "business unit"
    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'code': fields.char('Code', size=5),
        'active': fields.boolean('Active', help="If the active field is set to False, it will allow you to hide the payment term without removing it."),
    }

    _defaults = {
        'active': 1,
    }
    _order = 'code'


