import React from 'react';
import './App.css';
import { useState , useEffect, useRef} from 'react';
import axios from 'axios';

async function runInterpreter(input: string): Promise<string> {
  let output: string = "";
  try {
    const response = await axios.post('http://127.0.0.1:5000/run_interpreter', {
      input: input
    });
    output = response.data.output;
  } catch(err) {
    console.error("Interpreter error processing input:", err);
  }
  return output;
};

function Terminal() {
  const [input, setInput] = useState<string>("");
  const [output, setOutput] = useState<string[]>([]);
  const inputRef = useRef<HTMLInputElement>(null);
  const [pathPrefix, setPathPrefix] = useState<string>("> ");
  let isProgramActive: boolean = false;

  const handleInput = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
        processCommand(input);
        setInput("");
    } else if (e.key === "ArrowUp") { // endpoint
        processCommand(input);
    }
  }

  // this allows the app to show previous input/outputs
  const processCommand = async (command: string) => {
    let prevOutput: string[];

    if (output.length > 0) {
      prevOutput = output;
    } else {
      prevOutput = [];
    }

    // check if interpreter programs is running
    if (isProgramActive) {
      // command to quit the interpreter if it is running
      if (command.toLowerCase() === "quit") {
        setPathPrefix("> ");
        isProgramActive = false;
        return;
      }
    } else { 
      // command to start the interpreter if it is not running    
      if (command.toLowerCase() === "lisp" || command.toLowerCase() === "racket") {
        isProgramActive = true;
        setPathPrefix("Racket> "); 
        return;
      }
    }
    
    if (command.toLowerCase() === "clear") {
      setOutput([]);
      return;
    } else {
      // run interpreter
      let programOutput: string = pathPrefix + command; 
      if (isProgramActive) {
        programOutput = await runInterpreter(command);
      }
      setOutput([...prevOutput, pathPrefix + command, programOutput]);
    }
  }

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  return(
    <div className = "Terminal">
      <div className = "Output">
        {output.map((line, index) => (
          <div key={index}>{line}</div>
        ))}
      </div>
      <div className = "Input">
        <span> {pathPrefix} </span>
        <input
          ref = {inputRef}
          value = {input}
          onChange={e=>setInput(e.target.value)}
          onKeyDown={handleInput}
          autoFocus
        />
      </div>
    </div>
  )
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        Racket Interpreter
      </header>
      <Terminal/>
    </div>
  );
}

export default App;
