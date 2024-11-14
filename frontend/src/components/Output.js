// frontend/src/components/Output.js

import React from 'react';

function Output({ output }) {
    return (
        <div>
            <h3>Çıktı:</h3>
            <pre>{JSON.stringify(output, null, 2)}</pre>
        </div>
    );
}

export default Output;
