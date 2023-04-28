import pytest

# import the function you want to test
from main import calculate_total_charge


def test_calculate_total_charge():
    # Test 1 - Empty list
    assert calculate_total_charge('PA', []) == 0.0

    # Test 2 - No tax
    records = [{'name': 'Apples', 'price': 1.99, 'type': 'Wic Eligible food'}]
    assert calculate_total_charge('PA', records) == 2.11

    # Test 3 - PA clothing
    records = [{'name': 'T-shirt', 'price': 19.99, 'type': 'Clothing'}]
    assert calculate_total_charge('PA', records) == 21.19

    # Test 4 - NJ clothing, non-fur
    records = [{'name': 'T-shirt', 'price': 19.99, 'type': 'Clothing'}]
    assert calculate_total_charge('NJ', records) == 21.31

    # Test 5 - NJ clothing, fur
    records = [{'name': 'Fur coat', 'price': 199.99, 'type': 'Clothing'}]
    assert calculate_total_charge('NJ', records) == 213.19

    # Test 6 - DE clothing
    records = [{'name': 'T-shirt', 'price': 19.99, 'type': 'Clothing'}]
    assert calculate_total_charge('DE', records) == 19.99 * 1.0

    # Test 7 - NJ electronics
    records = [{'name': 'Headphones', 'price': 39.99, 'type': 'Electronics'}]
    assert calculate_total_charge('NJ', records) == 42.63

    # Test 8 - PA fur
    records = [{'name': 'Fur coat', 'price': 199.99, 'type': 'Clothing'}]
    assert calculate_total_charge('PA', records) == 211.99

    # Test 9 - Mixed types
    records = [{'name': 'Apples', 'price': 1.99, 'type': 'Wic Eligible food'},
               {'name': 'T-shirt', 'price': 19.99, 'type': 'Clothing'},
               {'name': 'Shoes', 'price': 59.99, 'type': 'Clothing'},
               {'name': 'Headphones', 'price': 39.99, 'type': 'Electronics'}]
    assert calculate_total_charge('PA', records) == 129.28

    # Test 10 - Mixed types
    records = [{'name': 'Apples', 'price': 1.99, 'type': 'Wic Eligible food'},
               {'name': 'T-shirt', 'price': 19.99, 'type': 'Clothing'},
               {'name': 'Shoes', 'price': 59.99, 'type': 'Clothing'},
               {'name': 'Headphones', 'price': 39.99, 'type': 'Electronics'}]
    assert calculate_total_charge('NJ', records) == 130.01


test_calculate_total_charge()
