# error
# print(a) => NameError - değişken hatası
# int('1a5') => ValueError - değer hatası
# print('1a'5) => SyntaxError - yazım hatası
# print(8/0) => ZeroDivisionError - sıfıra bölme hatası


"""
Docstring for error





Exception hierarchy
The class hierarchy for built-in exceptions is:

BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    ├── PythonFinalizationError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning

"""


# while :
#     try:
#         x = int (input("x: "))
#         y = int (input("y: "))
#         print(x/y)
#     except Exception as e:
#         print(" x ve y'yi girerken tam sayı olarak girin!....", e)
#     else:
#         break





c = 0
while True:
    try:
        x = int (input("x: "))
        y = int (input("y: "))
        print(x/y)
    except Exception as e:
        print(" x ve y'yi girerken tam sayı olarak girin!....", e)
        c  = c + 1
        if c==3:
            print("hakkın bitti mal oğlan:)")
            break
    else:
        break




    finally:
        print("try except çalıştı....")
