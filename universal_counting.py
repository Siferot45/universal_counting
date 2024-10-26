
def calculate_structure_sum(*args):
    total = 0
    
    for element in args:
        # ���� ������� � �����, ��������� ���
        if isinstance(element, int):
            total += element
            
        # ���� ������� � ������, ��������� � �����
        elif isinstance(element, str):
            total += len(element)
            
        # ���� ������� � �������, ������������ ����� � ��������
        elif isinstance(element, dict):
            total += calculate_structure_sum(*element.keys())
            total += calculate_structure_sum(*element.values())
            
        # ���� ������� � ������, ������ ��� ���������, ���������� ������������ ��� ��������
        elif isinstance(element, (list, tuple, set)):
            total += calculate_structure_sum(*element)
    return total


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
