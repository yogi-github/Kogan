import requests
from config import ROOT_API, FIRST_PAGE
from custom_exception import CalculatorException
from http import HTTPStatus

class CalculateCategoryWeight(object):

    def __init__(self):

        self.results = list()
        self.loop_api = None

    def read_data(self, response):

        if response.status_code != HTTPStatus.OK:
            raise CalculatorException('API to fetch data failed with status_code: {}'.format(response.status_code))

        data = response.json()
        objects = data.get('objects')
        self.loop_api = data.get('next')

        if objects:
            for product in objects:
                if product.get('category') == self.category:
                    self.results.append(product.get('size'))

    def calculate(self):

        sum = 0
        count = 0
        for size in self.results:
            if size:
                try:
                    sum += size['length'] * size['width'] * size['height']
                    count += 1
                except KeyError:
                    continue

        if count == 0 or sum == 0:
            return 0

        avg = sum / count
        cum_wt = (avg / 1000000) * 250
        return cum_wt

    def get_avg_weight(self):

        response = requests.get(ROOT_API + FIRST_PAGE)
        self.read_data(response)

        while self.loop_api is not None:
            response = requests.get(ROOT_API + self.loop_api)
            self.read_data(response)

        return self.calculate()
