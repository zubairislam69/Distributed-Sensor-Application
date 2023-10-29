import React, { useEffect } from 'react';
import './App.css';
import mqtt from 'mqtt';

function App() {

  const topic = 'python/mqtt';
  const client_id = 'publish-' + Math.floor(Math.random() * 1000);

  useEffect(() => {
    const client = mqtt.connect('mqtt://broker.emqx.io:1883'); // MQTT broker and port

    const onConnect = () => {
      console.log('Connected to MQTT Broker!');
      publish();
    };

    client.on('connect', onConnect);

    const publish = () => {
      let msg_count = 1;
      const interval = setInterval(() => {
        const msg = `messages: ${msg_count}`;
        client.publish(topic, msg, function (err) {
          if (err) {
            console.log('Failed to send message to topic ' + topic);
          } else {
            console.log(`Send '${msg}' to topic '${topic}'`);
          }
        });

        msg_count++;
        if (msg_count > 5) {
          clearInterval(interval);
          client.end();
        }
      }, 1000); // Publish a message every 1 second
    };

    return () => {
      // Cleanup logic, if needed, when the component unmounts
      client.end();
    };
  }, []); // The empty dependency array ensures that the effect runs once when the component mounts


  return (
    <div className="App">
      <header className="App-header">
        <p>
          Hello!
        </p>
      </header>
    </div>
  );
}

export default App;
