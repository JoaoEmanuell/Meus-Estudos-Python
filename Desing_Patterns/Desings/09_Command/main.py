from source import Button, Receptor
from source.commands import ButtonCommand

receptor = Receptor()
button = Button()
button.set_command(ButtonCommand(receptor, {
    'Hello' : 'World'
}))
button.action()