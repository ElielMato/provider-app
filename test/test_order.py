import unittest
from flask import current_app
from app import create_app
import os
from app import db
from app.models import Order
from app.services import OrderService
order_service = OrderService()

class ProductTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_order(self):
        order = self.__new_order()
        self.assertIsNotNone(order)
        self.assertEqual(order.id_client, 1)
        self.assertEqual(len(order.products), 2)
        self.assertEqual(order.total, 100.0)

    def test_save(self):
        order = self.__new_order()
        order_save = order_service.save(order)
        self.assertIsNotNone(order_save)
        self.assertIsNotNone(order_save.id)
        self.assertGreater(order_save.id, 0)
        self.assertEqual(order_save.id_client, order.id_client)
        self.assertEqual(order_save.products, order.products)
        self.assertEqual(order_save.total, order.total)
        self.assertIsNotNone(order_save.order_date)

    def test_delete(self):
        order = self.__new_order()
        order_save = order_service.save(order)
        self.assertIsNotNone(order_save)
        self.assertIsNotNone(order_save.id)
        self.assertGreater(order_save.id, 0)

        order_service.delete(order_save)

        deleted_order = order_service.find(order_save.id)
        self.assertIsNone(deleted_order)

    def test_find(self):
        order = self.__new_order()
        order_save = order_service.save(order)
        self.assertIsNotNone(order_save)
        self.assertIsNotNone(order_save.id)
        self.assertGreater(order_save.id, 0)

        order_find = order_service.find(order_save.id)
        self.assertIsNotNone(order_find)
        self.assertEqual(order_find.id, order_save.id)
        self.assertEqual(order_find.id_client, order_save.id_client)
        self.assertEqual(order_find.products, order_save.products)
        self.assertEqual(order_find.total, order_save.total)
        self.assertEqual(order_find.order_date, order_save.order_date)

    def test_find_all(self):
        order1 = self.__new_order()
        order2 = self.__new_order()
        order2.id_client = 2
        order2.total = 150.0

        order_service.save(order1)
        order_service.save(order2)

        orders = order_service.find_all()
        self.assertIsNotNone(orders)
        self.assertEqual(len(orders), 2)
        self.assertIn(order1, orders)
        self.assertIn(order2, orders)

    def test_find_by(self):
        order = self.__new_order()
        order_save = order_service.save(order)
        self.assertIsNotNone(order_save)
        self.assertIsNotNone(order_save.id)
        self.assertGreater(order_save.id, 0)

        order_find = order_service.find_by(id_client=1)
        self.assertIsNotNone(order_find)
        self.assertEqual(len(order_find), 1)
        self.assertEqual(order_find[0].id, order_save.id)
        self.assertEqual(order_find[0].id_client, order_save.id_client)

    def test_update(self):
        order = self.__new_order()
        order_save = order_service.save(order)
        
        order_save.total = 200.0
        order_save.products = [{"id": 3, "quantity": 4}]
        
        updated_order = order_service.save(order_save)
        
        self.assertEqual(updated_order.total, 200.0)
        self.assertEqual(updated_order.products, [{"id": 3, "quantity": 4}])
        self.assertEqual(order_save.id, updated_order.id)
        self.assertEqual(order_save.id_client, updated_order.id_client)

    def __new_order(self):
        order = Order()
        order.id_client = 1
        order.products = [
            {"id": 1, "quantity": 2},
            {"id": 2, "quantity": 1}
        ]
        order.total = 100.0
        return order