


class Intern:
    def __init__(self, character_chain="My name? I'm nobody, an intern, I have no name."):
        self.name = character_chain
    def __str__(self):
        return self.name
    
    class Coffee:
        def __init__(self, character_chain="This is the worst coffee you ever tasted."):
            self.character_chain = character_chain

        def __str__(self):
            return self.character_chain

    def work(self):
        raise NotImplementedError("I'm just an intern, I can't do that...")

    def make_coffee(self):
        return self.Coffee()


if __name__ == "__main__":
    intern = Intern()
    print(intern) # This uses the __str__ method of the Intern class

    second_intern = Intern("Mark")
    print(second_intern)

    try:
        intern.work()
    except Exception as e:
        print(f"Error: {e}")

    
    coffee = intern.make_coffee()
    print(coffee, coffee) # This uses the __str__ method of the Coffee class

