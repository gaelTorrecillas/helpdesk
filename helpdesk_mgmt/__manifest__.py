# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Helpdesk Management",
    "summary": """
        Helpdesk""",
<<<<<<< HEAD
    "version": "16.0.2.7.0",
=======
    "version": "16.0.2.6.1",
>>>>>>> bd6f564a ([IMP]helpdesk_mgmt: Add internal notes)
    "license": "AGPL-3",
    "category": "After-Sales",
    "author": "AdaptiveCity, "
    "Tecnativa, "
    "ForgeFlow, "
    "C2i Change 2 Improve, "
    "Domatix, "
    "Factor Libre, "
    "SDi Soluciones, "
    "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/helpdesk",
    "depends": ["mail", "portal"],
    "data": [
        "data/helpdesk_data.xml",
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/res_config_settings_views.xml",
<<<<<<< HEAD
        "views/helpdesk_ticket_templates.xml",
=======
>>>>>>> bd6f564a ([IMP]helpdesk_mgmt: Add internal notes)
        "views/helpdesk_ticket_menu.xml",
        "views/helpdesk_ticket_team_views.xml",
        "views/helpdesk_ticket_stage_views.xml",
        "views/helpdesk_ticket_category_views.xml",
        "views/helpdesk_ticket_channel_views.xml",
        "views/helpdesk_ticket_tag_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_dashboard_views.xml",
<<<<<<< HEAD
=======
        "templates/helpdesk_ticket_templates.xml",
>>>>>>> bd6f564a ([IMP]helpdesk_mgmt: Add internal notes)
    ],
    "demo": ["demo/helpdesk_demo.xml"],
    "assets": {
        "web.assets_frontend": [
            "helpdesk_mgmt/static/src/js/new_ticket.js",
        ],
    },
    "development_status": "Beta",
    "application": True,
    "installable": True,
}
