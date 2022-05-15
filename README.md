# Lisp interpreter (SLY)

A simple interpreter of a Scheme-like toy Lisp, using SLY as a lexer and parser.

Supports evaulating source files, as well as REPL.

Credits to http://norvig.com/lispy.html

Grammar implemented:
```ebnf
seq = expr , seq | ;
expr = SYMBOL 
       | STRING
       | NUMBER
       | list ;
list = "(" , seq , ")" ;
```

## 1. Install dependencies

```
pip install poetry
poetry install
```

## 2. Run

### 2.1. File

```
(venv) work@pop-os:~/repos/lisp-interpreter$ python3 lisp-interpreter.py -f tests/fizzbuzz-lambda.scm
Parser debugging for LispParser written to parser.out
Source: 
(define fizzbuzz (lambda (x y) (
  (display
    (cond (( = (modulo x 15) 0 ) "FizzBuzz")
          (( = (modulo x 3) 0 ) "Fizz")
          (( = (modulo x 5) 0 ) "Buzz")
          (else x)))
  (newline)
  
  (if (< x y) (fizzbuzz (+ x 1) y)))))
 
(fizzbuzz 1 100)
Parsed AST:  [[define, fizzbuzz, [lambda, [x, y], [[display, [cond, [[=, [modulo, x, 15], 0], FizzBuzz], [[=, [modulo, x, 3], 0], Fizz], [[=, [modulo, x, 5], 0], Buzz], [else, x]]], [newline], [if, [<, x, y], [fizzbuzz, [+, x, 1], y]]]]], [fizzbuzz, 1, 100]]
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
```

### 2.2. REPL (no arguments)

```
(venv) work@pop-os:~/repos/lisp-interpreter$ python3 lisp-interpreter.py
Parser debugging for LispParser written to parser.out
> (* 21 37)
777
> (define fizzbuzz (lambda (x y) (
  (display
    (cond (( = (modulo x 15) 0 ) "FizzBuzz")
          (( = (modulo x 3) 0 ) "Fizz")
          (( = (modulo x 5) 0 ) "Buzz")
          (else x)))
  (newline)
  
  (if (< x y) (fizzbuzz (+ x 1) y)))))
> (fizzbuzz 5 20)                 
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
> 
```
