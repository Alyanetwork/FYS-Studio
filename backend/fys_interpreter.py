# backend/fys_interpreter.py

from interpreter import Interpreter

def run_fys_code(code):
    interpreter = Interpreter(code)
    result = interpreter.execute()
    return result
