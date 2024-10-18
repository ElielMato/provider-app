import unittest
from flask import current_app
from app import create_app
import os
from app import db
from app.models import Product
from app.repositories import ProductRepository
from app.services import ProductService
service = ProductService()

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
    
    def test_product(self):
        product = self.__new_product()
        self.assertIsNotNone(product)
        self.assertEqual(product.name, "Producto")
        self.assertEqual(product.description, "Un Producto")

    def test_save(self):
        product = self.__new_product()
        product_save = service.save(product)
        self.assertIsNotNone(product_save)
        self.assertIsNotNone(product_save.id)
        self.assertGreater(product_save.id, 0)

    def test_delete(self):
        product = self.__new_product()
        product_save = service.save(product)
        self.assertIsNotNone(product_save)
        self.assertIsNotNone(product_save.id)
        self.assertGreater(product_save.id, 0)
        product_delete = service.delete(product_save)
        self.assertIsNone(product_delete)

    def test_find(self):
        product = self.__new_product()
        product_save = service.save(product)
        self.assertIsNotNone(product_save)
        self.assertIsNotNone(product_save.id)
        self.assertGreater(product_save.id, 0)
        product_find = service.find(1)
        self.assertIsNotNone(product_find)
        self.assertIsNotNone(product_save.id)
        self.assertGreater(product_save.id, 0)

    def test_find_all(self):
        product = self.__new_product()
        product1 = self.__new_product()
        product1.name = "Producto2"
        product1.description = "Un Producto2"
        product_save = service.save(product)
        service.save(product1)
        self.assertIsNotNone(product_save)
        self.assertIsNotNone(product_save.id)
        self.assertGreater(product_save.id, 0)
        products = service.find_all()
        self.assertIsNotNone(products)
        self.assertGreater(len(products), 1)

    def test_find_by(self):
        product = self.__new_product()
        product_save = service.save(product)
        self.assertIsNotNone(product_save)
        self.assertIsNotNone(product_save.id)
        self.assertGreater(product_save.id, 0)
        product_find = service.find_by(id = 1)
        self.assertIsNotNone(product_find)

    def test_update(self):
        product = self.__new_product()
        product_save = service.save(product)
        product_save.name = "Producto Nuevo"
        product_save_update = service.save(product)
        self.assertEqual(product_save_update.name, "Producto Nuevo")
        self.assertEqual(product_save.name, product_save_update.name)
        self.assertEqual(product.name, product_save_update.name)

    def test_stock_buy(self):
        product = self.__new_product()
        product_buy = service.buy(product, 2)
        self.assertEqual(product_buy.stock, 302)
        
    def test_stock_sell(self):
        product = self.__new_product()
        product_sell = service.sell(product, 2)
        self.assertEqual(product_sell.stock, 298)

    def __new_product(self):
        product = Product()
        product.name = "Producto"
        product.description = "Un Producto"
        product.stock = 300
        product.price = 20
        return product