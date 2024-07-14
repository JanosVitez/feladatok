#1. feladat
''''''''''
def get_integer_list():
    integer_list = []
    while True:
        num_input = input("Kérem adjon meg egy egész számot (vagy * vagy üres sor a kilépéshez): ")
        if num_input == "*" or num_input == "":
            break
        try:
            num = int(num_input)
            integer_list.append(num)
        except ValueError:
            print("Hibás bemenet! Csak egész számot, * vagy üres sort adhat meg.")

    return integer_list

# Tesztelés
print("Adja meg az egész számokat. * vagy üres sor a kilépéshez.")
numbers = get_integer_list()
print("Bekért számok:", numbers)
'''''''''

#2. feladat
'''''''''
def print_list_elements(lst):
    for elem in lst:
        print(elem)

example_list = [1, 2, 3, 4, 5]

print("A lista elemei:")
print_list_elements(example_list)
'''''''''

#3. feladat
'''''''''
def find_max(lst):
    max_elem = lst[0]
    for elem in lst:
        if elem > max_elem:
            max_elem = elem
    return max_elem

def find_min(lst):
    min_elem = lst[0]
    for elem in lst:
        if elem < min_elem:
            min_elem = elem
    return min_elem

def calculate_sum(lst):
    total_sum = 0
    for elem in lst:
        total_sum += elem
    return total_sum

example_list = [3, 7, 2, 9, 1, 5]

print("A lista legnagyobb eleme:", find_max(example_list))
print("A lista legkisebb eleme:", find_min(example_list))
print("A lista elemeinek összege:", calculate_sum(example_list))

'''''''''