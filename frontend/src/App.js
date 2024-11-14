// frontend/src/App.js

import React, { useState } from 'react';
import CodeEditor from './components/Editor';
import Output from './components/Output';
import Chart from './components/Chart';
import axios from 'axios';

function App() {
    const [output, setOutput] = useState("");
    const [chartData, setChartData] = useState([]);

    const runCode = async (code) => {
        try {
            const response = await axios.post("http://localhost:8000/run-code", { code });
            setOutput(response.data.output);
            if (response.data.output.chartData) {
                setChartData(response.data.output.chartData);
            }
        } catch (error) {
            setOutput(`Hata: ${error.response ? error.response.data.detail : "Bilinmeyen hata"}`);
        }
    };

    return (
        <div>
            <h1>FYS Studio Web Tabanlı Yorumlayıcı</h1>
            <CodeEditor onRunCode={runCode} />
            <Output output={output} />
            {chartData.length > 0 && <Chart data={chartData} />}
        </div>
    );
}

export default App;

