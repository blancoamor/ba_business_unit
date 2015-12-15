from openerp.osv import osv, fields



class product_template(osv.osv):

    _inherit = "product.template"
    _columns = {
        'business_unit_id': fields.many2one('business.unit', 'Business unit'),
    }

