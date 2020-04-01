from calculator import CalculateCategoryWeight
from config import AIR_CONDITIONERS, PRODUCTS


class CalculateAirconditionerWeight(CalculateCategoryWeight):

	def __init__(self):
		super().__init__()
		self.category = PRODUCTS[AIR_CONDITIONERS]

