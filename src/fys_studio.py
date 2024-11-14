# src/fys_studio.py

from interpreter import Interpreter

def main():
    code = """
    let x = 10
    let y = 20
    plot_signal("Buy", x + y)
    """
    interpreter = Interpreter(code)
    interpreter.execute()

if __name__ == "__main__":
    main()
