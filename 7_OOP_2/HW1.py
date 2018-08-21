class Descriptor:
    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        return getattr(instance, self.label, self)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError
        else:
            return setattr(instance, self.label, value)

    def __delete__(self, instance):
        return delattr(instance, self.label)


class BePositive:
    some_value = Descriptor('some')
    another_value = Descriptor('another')


