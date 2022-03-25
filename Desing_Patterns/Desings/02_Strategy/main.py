from source import Warrior, UseBow, UseSword, UseHeal

knight = Warrior(UseSword(6))
knight.action()
knight.atributes()

archer = Warrior(UseBow(6))
archer.action()
archer.atributes()

healer = Warrior(UseHeal(6))
healer.action()
healer.atributes()
