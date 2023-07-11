import pytest
import os
from gendiff.generate import generate_gendiff


current_dir = os.path.dirname(os.path.abspath(__file__))
file1 = os.path.join(current_dir, 'fixtures/file1.json')
file2 = os.path.join(current_dir, 'fixtures/file2.json')
file3 = os.path.join(current_dir, 'fixtures/file3.json')
file4 = os.path.join(current_dir, 'fixtures/file4.json')
file_path1 = os.path.join(current_dir, 'fixtures/file1.yml')
file_path2 = os.path.join(current_dir, 'fixtures/file2.yml')
file_path3 = os.path.join(current_dir, 'fixtures/file3.yml')
file_path4 = os.path.join(current_dir, 'fixtures/file4.yml')
r_result1 = os.path.join(current_dir, 'fixtures/right_answer1.txt')
r_result2 = os.path.join(current_dir, 'fixtures/right_answer2.txt')
r_result3 = os.path.join(current_dir, 'fixtures/right_answer3.txt')
r_result4 = os.path.join(current_dir, 'fixtures/right_answer4.txt')


@pytest.mark.parametrize('file1, file2, expected', [
    (file1, file2, r_result1),
    (file1, file1, r_result2),
    (file1, file3, r_result3),
    (file1, file4, r_result4),
    (file_path1, file_path2, r_result1),
    (file_path1, file_path1, r_result2),
    (file_path1, file_path3, r_result3),
    (file_path1, file_path4, r_result4)
])
def test_generate_gendiff(file1, file2, expected):
    result = generate_gendiff(file1, file2)
    with open(expected) as file:
        expected_result = file.read()
    assert result.strip() == expected_result.strip()
