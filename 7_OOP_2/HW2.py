class EnumMeta(type):
    def __new__(cls, class_name, bases, dct):
        name_value = {}
        ex_collection = {}

        for key, value in dct.items():
            if not key.startswith('__'):
                name_value.update({key: value})

        dct.update({'name/value': name_value})
        myclass = super(EnumMeta, cls).__new__(cls, class_name, bases, dct)

        for attr, val in name_value.items():
            exemplar = myclass(val)
            setattr(myclass, attr, exemplar)
            ex_collection.update({attr:exemplar})

        myclass.exemplars = ex_collection

        return myclass

    def __iter__(self):
        return iter(self.__dict__['exemplars'].values())

    def __getitem__(self, item):
        if item in self.__dict__['exemplars']:
            return self.__dict__['exemplars'][item]
        else:
            raise KeyError(item)


class Enum(metaclass=EnumMeta):

    def __new__(cls, val):
        if val not in cls.__dict__['name/value'].values():
            raise ValueError('{} is not a valid Direction'.format(val))
        else:
            for exemplar in cls.exemplars.values():
                if exemplar.value == val:
                    return exemplar

        newobject = super().__new__(cls)
        newobject.__class__ = cls

        for k, v in cls.__dict__['name/value'].items():
            if v == val:
                newobject.name = k
                newobject.value = val

        return newobject

    def __str__(self):
        class_name = self.__class__.__name__
        attr_name = self.name
        value = self.value
        str = '<{}.{}:{}>'.format(class_name, attr_name, value)
        return str


class Direction(Enum):
    north = 0
    east = 90
    south = 180
    west = 270


# tests
print(Direction.north)
print(Direction.north.name)
print(Direction.north.value, '\n')

print(Direction.south)
print(Direction.south.name)
print(Direction.south.value, '\n')

print(id(Direction.north))
print(id(Direction(0)), '\n')

print(id(Direction.south))
print(id(Direction(180)), '\n')
# print(Direction(30))

print(Direction['west'], '\n')
#print(Direction['north-west'])

for i in Direction:
    print(i)


