from datetime import datetime, timedelta
from odoo.tests import tagged
from odoo.tests.common import new_test_user, TransactionCase


@tagged('post_install', '-at_install', 'exchange_log', 'access_right')
class TestAccessRightExchangeLog(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_admin = cls.env.ref('base.user_admin')
        cls.test_user = new_test_user(
            cls.env,
            login='test_user',
            groups='jira.integration_group_user'
        )

    def create_system(self, user, **values):
        return self.env['integration.external_system'].with_user(user).create({
            'name': 'test_system',
            **values
        })

    def create_service(self, user, **values):
        return self.env['integration.external_service'].with_user(user).create({
            'name': 'test_service',
            **values
        })

    def create_exchange_log(self, user, **values):
        one_hour = timedelta(hours=1)
        return self.env['integration.exchange_log'].with_user(user).create({
            'name': 'test_exchange_log',
            'start_date': datetime.now(),
            'finish_date': datetime.now() + one_hour,
            **values

        })

    def test_check_access_user(self):
        test_system1 = self.create_system(self.test_admin)
        test_service1 = self.create_service(self.test_admin,
                                            system_id=test_system1)
        one_hour = timedelta(hours=1)
        one_day = timedelta(days=1)

        start_date = datetime.now() - one_day
        finish_date = start_date + one_hour
        test_exchange_log_old = self.create_exchange_log(
            self.test_admin,
            service_id=test_service1.id,
            start_date=start_date,
            finish_date=finish_date,
        )

        start_date = datetime.now()
        finish_date = start_date + one_hour
        test_exchange_log_now = self.create_exchange_log(
            self.test_admin,
            service_id=test_service1.id,
            start_date=start_date,
            finish_date=finish_date,
        )

        exchange_log_manager = self.env['integration.exchange_log']
        exchange_log_ids = exchange_log_manager.with_user(self.test_user).browse()

        self.assertInNot(
            member=test_exchange_log_old.id,
            container=exchange_log_ids,
            msg='User should not have access to the old logs')

        self.assertIn(
            member=test_exchange_log_now.id,
            container=exchange_log_ids,
            msg='User must have access to logs of today')
