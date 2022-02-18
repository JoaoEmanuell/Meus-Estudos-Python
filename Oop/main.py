class Circus:
    def introduce(self, presenter : any) -> None:
        presenter.introduce_show()

class Juggler:

    def introduce_show(self) -> None:
        print("Juggler introduce your show")

class Clown:

    def introduce_show(self) -> None:
        print("Clown introduce your show")

class Tamer:
    
        def introduce_show(self) -> None:
            print("Tamer introduce your show")
        
if __name__ == '__main__':
    circus = Circus()
    juggler = Juggler()
    clown = Clown()
    tamer = Tamer()
    circus.introduce(juggler)
    circus.introduce(clown)
    circus.introduce(tamer)