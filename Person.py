class Person:

    def __init__(self, name = ' ', age = ' ',contact_num = ' ',address = ' '):
        self.name = name
        self.age = age
        self.contact_num = contact_num
        self.address = address
        self.sched = None

    def __str__(self):
        return self.name + '\n' + str(self.age)  + '\n' + self.contact_num + '\n'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def contact_num(self):
        return self._contact_num

    @contact_num.setter
    def contact_num(self, contact_num):
        self._contact_num = contact_num

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address
    
    

