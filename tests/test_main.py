from app.main import process_data

# test that the function correctly removes duplicate elements.
# Provide a list with duplicates and assert the output matches the expected deduplicated list.
def test_process_data_removes_duplicates():
    input_data = [1, 2, 2, 3, 1, 4]
    expected = [1, 2, 3, 4]
    assert process_data(input_data) == expected

#  Test that the function handles empty lists correctly.
#  Pass an empty list and assert the result is also an empty list.
def test_process_data_empty_list():
    assert process_data([]) == []

# Test that the function leaves lists without duplicates unchanged.
#  Pass a list with unique elements and assert the output is identical to the input.
def test_process_data_no_duplicates():
    input_data = [1, 2, 3]
    expected = [1, 2, 3]         
    assert process_data(input_data) == expected
    
