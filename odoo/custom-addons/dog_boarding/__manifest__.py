{
    'name': 'Dog Boarding',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Manage dog boarding services',
    'description': """
        Dog Boarding Management System
        ============================
        * Manage dogs and their owners
        * Track vaccinations
        * Record dog walks
        * Handle boarding bookings
        * Manage kennels
    """,
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/dog_views.xml',
        'views/res_partner_views.xml',
        'views/dog_walk_views.xml',
        'views/booking_views.xml',
        'views/kennel_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
