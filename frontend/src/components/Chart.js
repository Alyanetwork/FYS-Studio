// frontend/src/components/Chart.js

import React from 'react';
import Plot from 'react-plotly.js';

function Chart({ data }) {
    return (
        <Plot
            data={data}
            layout={{ title: 'FYS Studio Çıktı Grafiği' }}
        />
    );
}

export default Chart;
