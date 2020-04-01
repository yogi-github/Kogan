import io
import unittest
from unittest.mock import patch
import start
from custom_exception import CalculatorException


class StartScriptTest(unittest.TestCase):

    def setUp(self):

        mock_ac = patch('air_conditioners.CalculateAirconditionerWeight.get_avg_weight')
        self.mock_ac = mock_ac.start()
        self.addCleanup(mock_ac.stop)

        mock_input = patch('start.input')
        self.mock_input = mock_input.start()
        self.addCleanup(mock_input.stop)

        mock_print = patch('sys.stdout', new_callable=io.StringIO)
        self.mock_print = mock_print.start()
        self.addCleanup(mock_print.stop)

    def test_get_started(self):

        self.mock_input.side_effect = [1]
        self.mock_ac.return_value = 2
        start.get_started()
        self.assertIn('2 Kg', self.mock_print.getvalue())

    def test_get_started_invalid_input(self):

        self.mock_input.side_effect = ['a']
        self.mock_ac.return_value = 2
        start.get_started()
        self.assertIn('Invalid choice', self.mock_print.getvalue())

    def test_get_started_invalid_choice(self):

        self.mock_input.side_effect = [0]
        self.mock_ac.return_value = 2
        start.get_started()
        self.assertIn('Category implementation does not exist', self.mock_print.getvalue())

    def test_get_started_invalid_data(self):

        self.mock_input.side_effect = [1]
        self.mock_ac.return_value = 0
        start.get_started()
        self.assertIn('Improper data', self.mock_print.getvalue())

    def test_get_started_calculator_exception(self):

        self.mock_input.side_effect = [1]
        self.mock_ac.side_effect = CalculatorException('Invalid data')
        start.get_started()
        self.assertIn('Invalid data', self.mock_print.getvalue())

    def test_get_started_handle_exception(self):

        self.mock_input.side_effect = [1]
        self.mock_ac.side_effect = Exception('Invalid data')
        start.get_started()
        self.assertIn('Invalid data', self.mock_print.getvalue())
