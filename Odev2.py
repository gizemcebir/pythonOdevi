def reverse_list_elements(nested_list):
    reversed_list = []
    for element in nested_list:
        if isinstance(element, list):
            # Eğer eleman bir liste ise, onu tersine çevir
            reversed_list.append(reverse_list_elements(element))
        else:
            # Eğer eleman bir liste değilse, onu olduğu gibi ekle
            reversed_list.append(element)
    return reversed_list[::-1]

# Örnek kullanım
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output = reverse_list_elements(input_list)
print(output)
