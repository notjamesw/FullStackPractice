import React from 'react';
import './App.css';
import { useState , useEffect, useRef} from 'react';

function Terminal() {
  const [input, setInput] = useState<string>("");
  const [output, setOutput] = useState<string[]>([]);
  const inputRef = useRef<HTMLInputElement>(null);
  const [pathPrefix, setPathPrefix] = useState<string>("> ");

  const handleInput = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
        processCommand(input);
        setInput("");
    }
  }

  // this allows the app to show previous input/outputs
  const processCommand = (command: string) => {
    let prevOutput: string[];

    if (output.length > 0) {
      prevOutput = output;
    } else {
      prevOutput = [];
    }

    setOutput([...prevOutput, pathPrefix + command, command + "operation"]);
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
