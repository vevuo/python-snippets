import csv
import string
from random import choice
from itertools import islice

class codeGenerator:
    def generate_ordered_codes(self, code_amount=100, prefix='TEST'):
        self.codes = list()

        for i in range(1, code_amount + 1):
            self.codes.append(prefix + str(i).zfill(4))

    def generate_random_codes(self, code_amount=100, code_length=8, prefix='CDE'):
        self.codes = set()        
        characters = list(string.ascii_uppercase)

        while(len(self.codes) < code_amount):
            code = prefix
            for _ in range(code_length - len(prefix)):
                code = code + choice(characters)
            self.codes.add(code)

    def write_to_csv(self, filename="test_codes.csv"):
        try:
            with open(filename, mode="w", newline='') as file_object:
                csv_writer = csv.writer(file_object, delimiter=';')
                for code in self.codes:
                    csv_writer.writerow([code])                    
        except IOError as e:
            print(f'I/O error: {e}')

    def print_codes(self, print_rows=10):
        if print_rows > len(self.codes):
            print_rows = len(self.codes)

        for code in islice(self.codes, print_rows):
            print(code)


def main():
    code_generator = codeGenerator()
    #code_generator.generate_ordered_codes()
    code_generator.generate_random_codes(code_amount=10000)
    code_generator.print_codes()
    code_generator.write_to_csv()

if __name__ == "__main__":
    main()