# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Animal:
    def __init__(self, name, age, voice='groal'):
        self.name = name
        self.age = age
        self.voice = voice

    def make_voice(self):
        print(self.voice)


class Fish(Animal):
    def __init__(self, name, age, scales, voice):
        super().__init__(name, age, voice)
        self.scales = scales

    def swim(self):
        print("i'm swimming, oh, it's titan!")


class Dog(Animal):
    def __init__(self, name, age, breed, voice):
        super().__init__(name, age, voice)
        self.breed = breed

    def bark(self):
        print('Bark!')


class Raven(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age)
        self.voice = voice
        self.color = name

    def fly_around_corpse(self):
        print('oooh, meat....')


# fish = Fish('Nemo', 2, 'silver', 'bul-bul')
# dog = Dog('Spark', 5, 'pitbull', 'bark!')
# bird = Raven('Qarasique', 6, 'white', 'bravo!')

# animals = [fish, dog, bird]

# for i in animals:
#     i.make_voice()

# fish.swim()
# dog.bark()
# bird.fly_around_corpse()


# Создал фабрику, которая может создавать любой класс, доступный ей в пространстве имен

class Factory:
    def __init__(self):
        print("Factory is started.")

    def make_class(self, class_name, *args):
        obj = eval(f"{class_name}({', '.join(map(repr, args))})")
        return obj


factory = Factory()
dog = factory.make_class('Dog', 'Spark', 5, 'pitbull', 'bark!')
fish = factory.make_class('Fish', 'Nemo', 2, 'silver', 'bul-bul')
bird = factory.make_class('Raven', 'Qarasique', 6, 'white', 'bravo!')

animals = [fish, dog, bird]

for i in animals:
    i.make_voice()

fish.swim()
dog.bark()
bird.fly_around_corpse()