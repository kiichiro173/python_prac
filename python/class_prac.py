class Person:
    def __init__(self, name, nationality, age):
        self.name = name
        self.nationality = nationality
        self.age = age
    
    def say_hello(self,name):
        print(f"こんにちは、{name}さん。私はきっちょもです。")