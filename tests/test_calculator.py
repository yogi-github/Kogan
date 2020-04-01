import unittest
from unittest.mock import patch, Mock

from calculator import CalculateCategoryWeight
from config import AIR_CONDITIONERS, PRODUCTS
from custom_exception import CalculatorException


class MockAPIResponse():

    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


class CalculateCategoryWeightTest(unittest.TestCase):

    def setUp(self):

        mock_get = patch('requests.get')
        self.mock_get = mock_get.start()
        self.addCleanup(mock_get.stop)

    def test_get_avg_weight_calculates_weight(self):

        data = {
            'objects': [
                {
                    "category": 'Air Conditioners',
                    "size": {
                        "length": 12.0,
                        "width": 10.0,
                        "height": 20.0
                    }
                },
                {
                    "category": 'Air Conditioners',
                    "size": {
                        "length": 43.0,
                        "width": 45.0,
                        "height": 53.6
                    }
                },
                {
                    "category": 'Washing Machine',
                    "size": {
                        "length": 43.0,
                        "width": 45.0,
                        "height": 53.6
                    }
                }
            ],
            'next': None
        }
        self.mock_get.return_value = MockAPIResponse(data, 200)
        obj = CalculateCategoryWeight()
        obj.category = PRODUCTS[AIR_CONDITIONERS]

        self.assertEqual(obj.get_avg_weight(), 13.2645)

    def test_get_avg_weight_returns_error(self):

        self.mock_get.return_value = MockAPIResponse({}, 400)
        obj = CalculateCategoryWeight()
        obj.category = PRODUCTS[AIR_CONDITIONERS]

        self.assertRaises(CalculatorException, obj.get_avg_weight)

    def test_get_avg_weight_invalid_data(self):

        data = {
            'objects': [
                {
                    "category": 'Air Conditioners',
                    "size": {
                        "width": 10.0,
                        "height": 20.0
                    }
                },
                {
                    "category": 'Air Conditioners',
                    "size": {
                        "length": 43.0,
                        "width": 45.0,
                    }
                },
                {
                    "category": 'Washing Machine',
                    "size": {
                        "length": 43.0,
                        "width": 45.0,
                        "height": 53.6
                    }
                }
            ],
            'next': None
        }
        self.mock_get.return_value = MockAPIResponse(data, 200)
        obj = CalculateCategoryWeight()
        obj.category = PRODUCTS[AIR_CONDITIONERS]

        self.assertEqual(obj.get_avg_weight(), 0)

    def test_get_avg_weight_partial_invalid_data(self):

        data = {
            'objects': [
                {
                    "category": 'Air Conditioners',
                    "size": {
                        "width": 10.0,
                        "height": 20.0
                    }
                },
                {
                    "category": 'Air Conditioners',
                    "size": {
                        "length": 43.0,
                        "width": 45.0,
                        "height": 50.2
                    }
                },
                {
                    "category": 'Washing Machine',
                    "size": {
                        "length": 43.0,
                        "width": 45.0,
                        "height": 53.6
                    }
                }
            ],
            'next': None
        }
        self.mock_get.return_value = MockAPIResponse(data, 200)
        obj = CalculateCategoryWeight()
        obj.category = PRODUCTS[AIR_CONDITIONERS]

        self.assertEqual(obj.get_avg_weight(), 24.28425)

    def test_get_avg_weight_with_one_dataset(self):

        data = {
            'objects': [
                {
                    "category": 'Air Conditioners',
                    "size": {
                        "length": 43.0,
                        "width": 45.0,
                        "height": 50.2
                    }
                },
                {
                    "category": 'Washing Machine',
                    "size": {
                        "length": 43.0,
                        "width": 45.0,
                        "height": 53.6
                    }
                }
            ],
            'next': None
        }
        self.mock_get.return_value = MockAPIResponse(data, 200)
        obj = CalculateCategoryWeight()
        obj.category = PRODUCTS[AIR_CONDITIONERS]

        self.assertEqual(obj.get_avg_weight(), 24.28425)

    def test_get_avg_weight_with_no_dataset(self):

        data = {
            'objects': [
                {
                    "category": 'Washing Machine',
                    "size": {
                        "length": 43.0,
                        "width": 45.0,
                        "height": 53.6
                    }
                }
            ],
            'next': None
        }
        self.mock_get.return_value = MockAPIResponse(data, 200)
        obj = CalculateCategoryWeight()
        obj.category = PRODUCTS[AIR_CONDITIONERS]

        self.assertEqual(obj.get_avg_weight(), 0)

    def test_get_avg_weight_with_empty_data(self):

        data = {
            'objects': [],
            'next': None
        }
        self.mock_get.return_value = MockAPIResponse(data, 200)
        obj = CalculateCategoryWeight()
        obj.category = PRODUCTS[AIR_CONDITIONERS]

        self.assertEqual(obj.get_avg_weight(), 0)