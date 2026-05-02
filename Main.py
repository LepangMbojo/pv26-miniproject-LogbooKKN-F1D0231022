import sys
from PySide6.QtWidgets import QApplication
from UI_main import MainWindow

def main():
    app = QApplication(sys.argv)
    
    with open("style.qss", "r") as file:
        app.setStyleSheet(file.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()