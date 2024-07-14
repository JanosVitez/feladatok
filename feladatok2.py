with open('programming_languages.txt', 'r') as input_file, open('programming_languages_cleaned.txt', 'w') as output_file:
    
    header = input_file.readline().strip()
    output_file.write("year;programming language\n")

    for line in input_file:
        data = line.strip().split(';')
        year = data[0]
        language = data[1]
        output_file.write(f"{year};{language}\n")

print("Az adatok átmásolása sikeresen megtörtént.")
