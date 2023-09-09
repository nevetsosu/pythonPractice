class Person:
    name : str = "default"
    age : int = 0
    gender : bool = True

    def __init__(self, copyData: 'Person' = None) -> None:
        if (copyData != None):
            self.name = copyData.name
            self.age = copyData.age
            self.gender = copyData.gender

    @staticmethod
    def mutatorFunction(person : 'Person', name : str, age : int, gender : bool):
        person.name = name
        person.age = age
        person.gender = gender

    # we can pass objects of this class by using the cls keyword
    def CopyLeftToRight(person1 : 'Person', person2 : 'Person'):
        person1.name = person2.name
        person1.age = person2.age
        person1.gender = person2.gender


def main():
    test_person = Person()

    Person.mutatorFunction(test_person, "Steven", 20, True)

    new_person = Person(test_person)
    print(test_person.name, test_person.age, test_person.gender)
    print(new_person.name, new_person.age, new_person.gender)

if __name__ == "__main__": main()