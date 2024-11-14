// frontend/src/components/Editor.js

import React, { useState } from 'react';
import Editor from '@monaco-editor/react';

function CodeEditor({ onRunCode }) {
    const [code, setCode] = useState("// FYS Studio kodunuzu buraya yazın...");

    const handleRun = () => {
        onRunCode(code);
    };

    return (
        <div>
            <Editor
                height="400px"
                defaultLanguage="plaintext"
                defaultValue={code}
                onChange={setCode}
            />
            <button onClick={handleRun}>Çalıştır</button>
        </div>
    );
}

export default CodeEditor;
