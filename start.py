from air_conditioners import CalculateAirconditionerWeight
from config import PRODUCTS, AIR_CONDITIONERS
from custom_exception import CalculatorException

# Can be extended to support N categories
CATEGORY_FUNCTION = {
        AIR_CONDITIONERS: CalculateAirconditionerWeight,
    }


def get_started():

    print('Select any product to find average cubic weight')
    counter = 0
    for product in PRODUCTS:
        counter += 1
        print('{}. {}'.format(counter, product))

    try:
        option = int(input('Enter product number [strictly numeric]\n'))

        func = CATEGORY_FUNCTION.get(option-1)
        if not func:
            raise CalculatorException('Category implementation does not exist')

        weight = func().get_avg_weight()
        if weight == 0:
            raise CalculatorException('Improper data')

        print('Average Cubic Weight: {} Kg'.format(weight))
        print('Rounded Average Cubic Weight: {} Kg'.format(round(weight, 2)))

    except ValueError as ex:
        print('Sorry, Invalid choice')

    except CalculatorException as ex:
        print('Application error: {}'.format(str(ex)))

    except Exception as ex:
        print('Application error: {}'.format(str(ex)))


if __name__ == '__main__':
    get_started()