from app.main_window import MainWindow
import tkinter as tk


def main() -> None:
    """Запуск оконного приложения."""
    root = tk.Tk()
    root.withdraw()  # Прячем главное окно Tk, чтобы оно не появлялось
    MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
