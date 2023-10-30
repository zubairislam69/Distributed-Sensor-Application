import React, { useEffect } from 'react'

import * as mqtt from 'mqtt/dist/mqtt'

const Publisher = () => {
    const caCertFile = 'ca_certificate/emqxsl-ca.crt'
    const clientId = "sensor-" + Math.random().toString(16).substring(2, 8);
    const username = "sensor-app";
    const password = "sensor123";

    const client = mqtt.connect("wss://ja5d193e.ala.us-east-1.emqxsl.com:8084/mqtt", {
        clientId,
        username,
        password,
        ca: [caCertFile],
        rejectUnauthorized: true
    });

    client.on('connect', () => {
        console.log("on connect")
    });

    function handleClick(message) {
        return client.publish('python/mqtt', message);
    }

    return (
        <button type="button" onClick={() => handleClick('false')}>
            Click
        </button>
    )
}

export default Publisher