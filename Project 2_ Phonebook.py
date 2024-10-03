class PhoneBook:
  def __init__(self):
    phone_book = {}
    name = ''
    number = ''
    self.phone_book = phone_book
    self.name = name
    self.number = number
  def add_contact(self, name, number):
    self.phone_book[name] = number

  def search_contact(self, name):
    if name in self.phone_book:
      return self.phone_book[name]
    else:
      return "Contact not found."

  def delete_contact(self, name):
    if name in self.phone_book:
      del self.phone_book[name]
      return "Contact deleted successfully."
    else:
      return "Contact not found."

  def display_contacts(self):
    if not self.phone_book:
      return "Phone book is empty."
    else:
      return self.phone_book