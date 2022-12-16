{
    'name': 'ata_integration_jira',
    'summary': """
Integration: Jira
    """,

    'author': 'Igor Kutko',
    'website': 'https://www.it-artel.ua',
    'category': 'project',
    'version': '15.0.1.0.0',

    'depends': [
        'base',
        'project',
        'hr_timesheet',
    ],

    'data': [
        'security/integration_groups.xml',
        'security/integration_exchange_log_security.xml',
        'security/ir.model.access.csv',
        'views/integration_menus.xml',
        'views/external_system_views.xml',
        'views/external_system_user_views.xml',
        'views/external_service_views.xml',
        'views/external_service_parameter_views.xml',
        'views/exchange_log_views.xml',
        'views/project_project_views.xml',
        'views/project_task_views.xml',
        'wizard/external_request_views.xml',
        'wizard/jira_issue_views.xml',
        'wizard/jira_worklog_views.xml',
        'wizard/jira_comment_views.xml',
        'wizard/exchange_views.xml',
        'report/planned_workload_report_templates.xml',
        'report/planned_workload_report_views.xml',
        'report/task_report_views.xml',
    ],

    'demo': [
        'data/external_system_demo.xml',
        'data/external_service_demo.xml',
        'data/external_service_parameter_demo.xml',
    ],
    'license': 'LGPL-3',

}
