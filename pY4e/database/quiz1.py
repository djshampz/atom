class Animal:

    sound = None
    
    def bark(self):
        self.sound = 'bark'
        print(self.sound)

dog = Animal()
dog.bark()
