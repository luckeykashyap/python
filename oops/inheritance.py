# class Animal:
#     pass 

class Cat:
    def __init__(self,cat_name):
        print("i am initialized firstly")
        self.cat_name = cat_name

    def display(self):
        print("This is a cat")
    
    def display_name(self):
        print("my cat name is ", self.cat_name)

cat_obj = Cat("tom")
cat_obj.display()
cat_obj.display_name()
print("****************")
cat_obj = Cat("kitty")
cat_obj.display()
cat_obj.display_name()


# print(Cat.a)
# Cat.display()




