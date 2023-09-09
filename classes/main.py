class Person:
    Sexes = {"Male": True, "Female": False}

    def __init__(self, Sex: bool = True, name: str = "default_name"):
        self.name = name
        if Sex: self.Sex = "Male"
        else: self.Sex = "Female"

class Baby(Person):
    def __init__(self, Annoying: bool = True, Sex: bool = True, name: str = "default_name"):
        Person.__init__(self, Sex, name)
        self.wanted = not Annoying

def main():
    nevets = Person(Person.Sexes["Male"],"nevets")
    print(nevets.name, nevets.Sex)

    minhthu = Baby(False, Person.Sexes["Female"],"minhthu")

    print(minhthu.name, minhthu.Sex, "Wanted:", minhthu.wanted)

if __name__ == "__main__": main()