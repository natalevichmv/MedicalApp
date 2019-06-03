import tkinter
import tkinter.font


from interface.login_window import LoginWindow
from controller.controller import Controller


def create_controller():
    return Controller()


def create_view():
    root = tkinter.Tk()
    root.withdraw()
    default_font = tkinter.font.nametofont("TkDefaultFont")
    default_font.configure(family='Droid Sans Mono', size=18)

    LoginWindow(root, create_controller())
    return root


def main():
    create_view().mainloop()


if __name__ == '__main__':
    main()
