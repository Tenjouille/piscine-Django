class   Intern:
    def __init__(self, name : str = None):
        if name == None:
            self.Name = "My name? I'm nobody, an intern, I have no name."
        else:
            self.Name = name

    def __str__(self):
        return self.Name
    
    def work(self):
        raise Exception("I'm just an intern, I can't do that...")
    
    class   Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def make_coffee(self):
        return self.Coffee()
    
if __name__ == "__main__":
    weirdo = Intern()
    Mark = Intern("Mark")

    print(f"HR : Your attention everyone, please meet our two new Interns. What are your names you guys ?")
    print(f"Intern 1 : {Mark.Name}")
    print(f"Intern 2 : {weirdo.Name}")

    coffee = Mark.make_coffee()
    print(coffee)

    try:
        weirdo.work()
    except Exception as e:
        print(e)