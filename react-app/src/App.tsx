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

async function getPrevCommmand(): Promise<string> {
  let prevCommand: string = "";
  try {
    const response = await axios.get('http://127.0.0.1:5000/get_prev');
    prevCommand = response.data.output;
  } catch (err) {
    console.error("Error finding prev command:", err)
  }
  return prevCommand;
}

function Terminal() {
  const [input, setInput] = useState<string>("");
  const [output, setOutput] = useState<string[]>([]);
  const inputRef = useRef<HTMLInputElement>(null);
  const [pathPrefix, setPathPrefix] = useState<string>("> ");
  const [isProgramActive, setProgramState] = useState<boolean>(false);

  const handleInput = async (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
        processCommand(input);
        setInput("");
    } else if (e.key === "ArrowUp") { 
        if (isProgramActive) {
          const prevCommand = await getPrevCommmand();
          setInput(prevCommand);
        }
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
        setProgramState(false);
        return;
      }
    } else { 
      // command to start the interpreter if it is not running    
      if (command.toLowerCase() === "lisp" || command.toLowerCase() === "racket") {
        setProgramState(true);
        setPathPrefix("Racket> "); 
        setOutput([...prevOutput]);
        return;
      }
    }
    //console.log("DEBUG");
    
    if (command.toLowerCase() === "clear") {
      try {
        await axios.delete('http://127.0.0.1:5000/clear_all');
        setOutput([]);
      } catch (err) {
        console.log("Error clearing cache:", err);
      }
      return;
    } else {
      // run interpreter
      const echo: string = pathPrefix + command; 
      if (isProgramActive) {
        console.log("test");
        const programOutput = await runInterpreter(command);
        setOutput([...prevOutput, echo, programOutput]);
      } else {
        setOutput([...prevOutput, echo]);
      }
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
        <span id = "input_prefix">{pathPrefix}</span>
        <input
          id = "terminal_input"
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
