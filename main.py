from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
         if len (value) == 10 and value.isdigit():
              super().__init__(value)
         else:
              raise ValueError(f"Phone number should be 10 digits")
         

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def find_phone(self, phone_number):
       for p in self.phones:
            if str(p) == phone_number:
                return p
            else:
                continue

    def delete_phone(self, phone_number):
         self.phones.remove(phone_number)

    def edit_phone(self, old_phone, new_phone):
         self.phones = [p if str(p)!= old_phone else Phone(new_phone) for p in self.phones]


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add(self, record):
        self.data[record.name.value] = record
        print(f"Contact {record.name.value} added to address book")

    def find(self, name):
        return self.data.get(name)
    
        
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Contact {name} deleted from address book")
        else:
            print(f"Contact {name} not found")

    def show_all_records(self):
        if self.data:
            print("All contacts:")
            for record in self.data.values():
                print(record)
        else:
            print("Address book is empty.")
   
# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("0506088907")
john_record.add_phone("0668870032")

    # Додавання запису John до адресної книги
book.add(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("0376654321")
book.add(jane_record)

    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("0504688907", "0665086535")

print(john)  

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("0504688907")
print(f"{john.name}: {found_phone}")  

    # Видалення запису Jane
book.delete("Jane")

for name, record in book.data.items():
    print(record)

        
   
