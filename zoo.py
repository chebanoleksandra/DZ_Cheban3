class Animal:
    def about_animal(self, breathing, spine, eat, paws, tail, fur, anim_type):
        self.breathing = breathing
        self.spine = spine
        self.eat = eat
        self.paws = paws
        self.tail = tail
        self.fur = fur
        self.anim_type = anim_type


class Mammal(Animal):
    def about_mammal(self):
        super().__init__()
        self.anim_type = 'mammal'
        self.breathing = 'lungs'
        self.spine = 'spine'
        self.fur = 'fur'
        self.ears = 2


class Cat(Mammal):
    def __init__(self, name):
        super().__init__()
        self.eat = "cat's food"
        self.paws = 4
        self.tail = 1
        self.name = name
        self.about_mammal()


marcy = Cat('Marcy')

print(f'This is my cat {marcy.name}. All cats are {marcy.anim_type}s. '
      f'They breath with {marcy.breathing}, have a {marcy.spine} and most of them have {marcy.fur}.'
      f' Cats have {marcy.paws} paws, {marcy.tail} tail and {marcy.ears} ears. Home cats, like mine, eat {marcy.eat}.')