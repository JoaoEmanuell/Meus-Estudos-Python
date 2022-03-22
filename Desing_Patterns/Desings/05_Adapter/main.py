from source import Alarm, Person

emanuel = Person("Emanuel")
john = Person("John")
rebeca = Person("Rebeca")

alarm = Alarm()

alarm.add_person(emanuel)
alarm.add_person(john)
alarm.add_person(rebeca)

alarm.play()