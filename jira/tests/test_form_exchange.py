from odoo.tests import tagged
from odoo.tests.common import Form, TransactionCase


@tagged('post_install', '-at_install', 'exchange', 'form')
class TestFormExchange(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_admin = cls.env.ref('base.user_admin')

    def test_form(self):
        default_service = self.env.ref(
            'jira.integration_external_service_issue_updated')
        default_worklog_service = self.env.ref(
            'jira.integration_external_service_worklog')

        project_key = "TEST";

        exchange_form = Form(self.env['integration.exchange'])
        exchange_form.project_key = project_key
        test_exchange1 = exchange_form.save()
        self.assertEqual(
            test_exchange1.service_id,
            default_service.id,
            msg=f"""Exchange service {test_exchange1.service_id.name} 
                is not equal default value {default_service.name}""")
        self.assertEqual(
            test_exchange1.worklog_service_id,
            default_worklog_service.id,
            msg=f"""Exchange worklog service {test_exchange1.worklog_service_id.name}
                is not equal default value {default_worklog_service.name}""")
        self.assertEqual(
            test_exchange1.project_key,
            project_key,
            msg=f"""Project key {test_exchange1.project_key}
                is not equal test value {project_key}"""
        )
