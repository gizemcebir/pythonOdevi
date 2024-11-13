def flatten_list(nested_list):
    flattened = []
    for element in nested_list:
        if isinstance(element, list):
            # Eğer eleman bir liste ise, onu tekrar düzleştir
            flattened.extend(flatten_list(element))
        else:
            # Eğer eleman bir liste degilse, direk ekle
            flattened.append(element)
    return flattened

input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output = flatten_list(input_list)
print(output)
