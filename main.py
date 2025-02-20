import sys
from PyQt5.QtWidgets import QApplication
from PySnake import PySnake


def main():
    app = QApplication(sys.argv)
    window = PySnake()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
