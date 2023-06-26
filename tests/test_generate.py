import pytest
from gendiff.generate import generate_gendiff


file_path1 = 'tests/fixtures/file1.json'
file_path2 = 'tests/fixtures/file2.json'
file_path3 = 'tests/fixtures/file3.json'
r_result1 = 'tests/fixtures/right_answer1.txt'
r_result2 = 'tests/fixtures/right_answer2.txt'
r_result3 = 'tests/fixtures/right_answer3.txt'


@pytest.mark.parametrize('file1, file2, expected', [
    (file_path1, file_path2, r_result1),
    (file_path1, file_path1, r_result2),
    (file_path1, file_path3, r_result3)
])
def test_generate_gendiff(file1, file2, expected):
    result = generate_gendiff(file1, file2)
    with open(expected) as file:
        expected_result = file.read()
    assert result.strip() == expected_result.strip()
