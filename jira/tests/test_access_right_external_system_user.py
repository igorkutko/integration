from odoo.exceptions import AccessError
from odoo.tests import tagged
from odoo.tests.common import new_test_user, TransactionCase


@tagged('post_install', '-at_install', 'exchange_log', 'access_right')
class TestAccessRightExternalSystemUser(TransactionCase):

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

    def create_external_system_user(self, user, **values):
        return self.env[
            'integration.external_system_user'
        ].with_user(user).create({
            'name': 'test external system user',
            **values
        })

    def test_check_access_user(self):
        test_system1 = self.create_system(self.test_admin)
        # test_external_system_user_this = self.create_external_system_user(
        #     self.test_admin,
        #     system_id=test_system1.id,
        #     user_id=self.test_user.id,
        #     login='test_user',
        #     password='1'
        # )
        test_external_system_user_other = self.create_external_system_user(
            self.test_admin,
            system_id=test_system1.id,
            user_id=self.test_admin.id,
            login='test_admin',
            password='0'
        )
        # with self.assertRaises(
        #         AccessError,
        #         msg='User should not able to modify another user!'):
        #     test_external_system_user_this.with_user(self.test_user).write({
        #       'name': 'changed by user'
        #      })
        with self.assertRaises(
                AccessError,
                msg='User should be able to modify himself!'):
            test_external_system_user_other.with_user(self.test_user).write({
                'name': 'changed by user'
            })
