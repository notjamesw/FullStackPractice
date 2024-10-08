# Lisp-Racket Interpreter Web Application

## Introduction
This web application was created with the intent of sharing the interpreter I recently built for Racket - a Lispy language I had learned in my first year of university! Although the interpreter is quite rudimentary, it goes through the full interpretation process and has decent capabilities, especially when it comes to calculator functions. you can check out the full description of the interpreter [here](https://github.com/notjamesw/Lisp-RacketInterpreter). 

## Tech stack :computer:
- React and Typescript to build a responsive webpage on the front end, and Axios to send HTTP requests to the API.
- Built a RESTful API with Flask on the backend and used GET, POST, and DELETE HTTP methods to process inputs, return outputs from the interpreter, and manage cached data
- Previous input data is cached in a FIFO stack with a set max size. 

## How to
While the interpreter is not active, the terminal will echo user inputs.

- `racket` or `lisp` to enter racket environment
- `quit` to leave racket environment
- `clear` to clear the terminal and all cached inputs
- press the `Up Arrow` to retrieve previous inputs

Completed version 1, you can check out the demo below!

[![Interpreter Demo](https://img.youtube.com/vi/_oXB38cosXI/0.jpg)](https://www.youtube.com/watch?v=_oXB38cosXI)
