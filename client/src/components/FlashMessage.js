// FlashMessage.js
import React, { useState, useEffect } from 'react';

function FlashMessage({ message, duration = 3000 }) {
    const [visible, setVisible] = useState(true);

    useEffect(() => {
        const timer = setTimeout(() => {
            setVisible(false);
        }, duration);

        return () => clearTimeout(timer);
    }, [duration]);

    if (!visible) return null;

    return (
        <div className="flash-message">
            {message}
        </div>
    );
}

export default FlashMessage;
