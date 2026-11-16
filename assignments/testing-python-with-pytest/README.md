# 📘 Assignment: Testing Python Programs with pytest

## 🎯 Objective

Learn how automated tests help you check that Python functions work correctly. You will use `pytest` to write tests for normal inputs, edge cases, and expected errors.

## 📝 Tasks

### 🛠️ Write Your First Unit Tests

#### Description
Read the functions in `starter_code.py` and create a test file named `test_starter_code.py`. Write tests that check the expected behavior of each function with typical inputs.

#### Requirements
Completed program should:

- Install pytest and run tests with the `pytest` command
- Import the functions from `starter_code.py`
- Include at least one test for `calculate_average()`
- Include at least one test for `is_valid_password()`
- Include at least one test for `find_max()`
- Use clear test names that describe the behavior being checked


### 🛠️ Test Edge Cases and Errors

#### Description
Expand the test suite to cover unusual inputs and confirm that invalid input produces the expected error.

#### Requirements
Completed program should:

- Test an average calculated from multiple numbers
- Test the empty-list behavior of `calculate_average()`
- Test both valid and invalid passwords
- Test `find_max()` with negative numbers and a single-item list
- Confirm that `find_max()` raises `ValueError` for an empty list using `pytest.raises`
- Finish with all tests passing and no failures reported by pytest
