import csv
csv_file = input('enter csv file name / path to read from: ')
txt_file = input('enter txt file name / path to write to: ')
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        i = 0
        for row in csv.reader(my_input_file):
            if i == 0:
                my_output_file.write(''.join(row)[1::] + '\n')
            else:
                my_output_file.write(''.join(row) + '\n')
            i += 1
    my_output_file.close()
