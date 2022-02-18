from source import House, Person
        
if __name__ == '__main__':
    ana_house = House()
    ana = Person('Ana')
    
    ana.set_place(ana_house)
    ana_house.set_owner(ana)

    owner = ana_house.get_owner()
    owner.introduce_yourself()
    ana.introduce_place()
