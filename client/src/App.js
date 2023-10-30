import React, { useEffect } from 'react';
import './App.css';
import mqtt from 'mqtt';
import Publisher from './Publisher';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Publisher />
      </header>
    </div>
  );
}

export default App;
