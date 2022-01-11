from source import interface

def main():
    inter = interface.interface()
    inter.Iniciar()

if __name__ == '__main__':
    try : main()
    except KeyboardInterrupt: pass
