# tests/test_account.py
import json
from pathlib import Path
from unittest import TestCase
from models import db, app
from models.account import Account

ACCOUNT_DATA = []

class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """Connect and load data needed by tests"""
        # PORNEȘTE application context
        cls.ctx = app.app_context()
        cls.ctx.push()

        db.create_all()

        fixtures = Path(__file__).parent / "fixtures" / "account_data.json"
        with fixtures.open(encoding="utf-8") as f:
            global ACCOUNT_DATA
            ACCOUNT_DATA = json.load(f)

    @classmethod
    def tearDownClass(cls):
        """Disconnect from database"""
        db.session.remove()
        db.drop_all()
        cls.ctx.pop()   # ÎNCHIDE application context

    def setUp(self):
        db.session.query(Account).delete()
        db.session.commit()

    def tearDown(self):
        db.session.remove()

    # ----------------- TESTS -----------------
    def test_create_an_account(self):
        data = ACCOUNT_DATA[0]
        account = Account(**data)
        account.create()
        self.assertEqual(len(Account.all()), 1)

    def test_create_all_accounts(self):
        for data in ACCOUNT_DATA:
            Account(**data).create()
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))
