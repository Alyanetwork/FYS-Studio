Proje Yapısı: FYS Studio Web Tabanlı Yorumlayıcı
Teknoloji Seçimi ve Kullanılacak Araçlar
Frontend: React ve Monaco Editor ile gelişmiş bir kod düzenleyici ve kullanıcı arayüzü.
Backend: FastAPI ile Python tabanlı API. Backend, FYS Studio kodlarını çalıştıracak yorumlayıcı işlevini görür.
Grafiksel Çıktı: Plotly.js ile grafiksel sonuçları gösterme.
Kod Renklendirme: Monaco Editor, profesyonel kod düzenleme deneyimi sunar.
Çıktı ve Hata Yönetimi: JSON formatında detaylı çıktı ve hata raporlaması.
Tam Dosya Yapısı
plaintext
Kodu kopyala
FYS-Studio-Web/
├── frontend/                # React tabanlı frontend uygulaması
│   ├── src/
│   │   ├── components/      # React bileşenleri
│   │   │   ├── Editor.js    # Kod editörü bileşeni
│   │   │   ├── Output.js    # Çıktı bileşeni
│   │   │   └── Chart.js     # Grafiksel çıktı bileşeni
│   │   └── App.js           # Ana uygulama bileşeni
│   └── public/
├── backend/                 # FastAPI tabanlı backend uygulaması
│   ├── main.py              # FastAPI ana dosyası
│   ├── fys_interpreter.py   # FYS Studio yorumlayıcı entegrasyonu
│   └── requirements.txt     # Backend bağımlılıkları
├── examples/                # Örnek FYS Studio kod dosyaları
│   ├── moving_average_analysis.fys  
│   └── rsi_analysis.fys
└── README.md                # Proje açıklamaları
Backend - backend/main.py (FastAPI)
Backend, FYS Studio kodlarını alır, yorumlar ve JSON formatında geri döndürür.

1. backend/fys_interpreter.py
Bu dosya, daha önce geliştirdiğimiz Interpreter (Yorumlayıcı) sınıfını kullanarak gelen kodu yorumlayacak ve sonucu döndürecektir. Çıktı, JSON formatında grafik ve metinsel verileri içerecek.

python
Kodu kopyala
# backend/fys_interpreter.py

from interpreter import Interpreter

def run_fys_code(code):
    interpreter = Interpreter(code)
    result = interpreter.execute()
    return result
2. backend/main.py
FastAPI ile kodu alan, çalıştıran ve JSON formatında sonuç döndüren API.

python
Kodu kopyala
# backend/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fys_interpreter import run_fys_code

app = FastAPI()

class FYSCodeRequest(BaseModel):
    code: str

@app.post("/run-code")
async def run_code(request: FYSCodeRequest):
    try:
        result = run_fys_code(request.code)
        return {"output": result, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"error": str(e), "status": "error"})
Backend'i Çalıştırma

Bağımlılıkları yükleyin:

bash
Kodu kopyala
pip install fastapi uvicorn
Backend'i başlatın:

bash
Kodu kopyala
uvicorn main:app --reload
Frontend (React) - frontend/src/App.js
React arayüzü, kullanıcıların FYS Studio kodlarını yazması ve çalıştırması için gelişmiş bir kod editörü ve grafiksel çıktı alanı sağlar.

1. frontend/src/components/Editor.js (Monaco Editor ile Kod Editörü)
Gelişmiş kod düzenleyici ile profesyonel bir deneyim sağlar.

javascript
Kodu kopyala
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
2. frontend/src/components/Output.js (Sonuçları Gösteren Bileşen)
API’dan dönen çıktıyı JSON formatında gösterir.

javascript
Kodu kopyala
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
3. frontend/src/components/Chart.js (Grafik Gösterimi için)
Plotly kullanarak grafiksel çıktıları görselleştirir.

javascript
Kodu kopyala
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
4. frontend/src/App.js
Frontend ve backend’i entegre ederek FYS Studio kodunun çalıştırılmasını sağlar.

javascript
Kodu kopyala
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
Frontend'i Çalıştırma

React uygulamasının bağımlılıklarını yükleyin:

bash
Kodu kopyala
npm install @monaco-editor/react axios plotly.js react-plotly.js
Frontend uygulamasını çalıştırın:

bash
Kodu kopyala
npm start
Örnek Kullanım ve Test
Kullanım: Kullanıcı, FYS Studio dilinde bir kod yazıp “Çalıştır” butonuna tıklayarak çalıştırabilir. Kodun çıktısı, metinsel veya grafiksel olarak görüntülenecektir.

Test: Backend ve frontend üzerinde birim testler ve bütünleşik testler ile sistem doğrulama yapılabilir.

README.md
markdown
Kodu kopyala
# FYS Studio Web Tabanlı Yorumlayıcı

FYS Studio, finansal analizler ve grafiksel gösterimler için tasarlanmış özel bir programlama dilidir. Bu web tabanlı yorumlayıcı ile FYS Studio kodlarını yazabilir ve analiz sonuçlarını doğrudan tarayıcınızda görüntüleyebilirsiniz.

## Özellikler

- **Kod Düzenleyici**: Monaco Editor ile profesyonel bir kod düzenleme deneyimi.
- **Grafik Gösterimi**: Plotly.js kullanarak grafiksel çıktı.
- **JSON Formatında Çıktı ve Hata Yönetimi**: Çıktı ve hata mesajları JSON formatında detaylı olarak sunulur.

## Kurulum

1. Projeyi klonlayın:
   ```bash
   git clone https://github.com/username/FYS-Studio-Web.git
   cd FYS-Studio-Web
Backend Bağımlılıklarını Yükleyin ve Çalıştırın:

bash
Kodu kopyala
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
Frontend Bağımlılıklarını Yükleyin ve Çalıştırın:

bash
Kodu kopyala
cd ../frontend
npm install
npm start
Kullanım
Kod Yazma: FYS Studio kodunuzu editöre yazın.
Çalıştırma: "Çalıştır" butonuna tıklayın.
Sonuç Görüntüleme: Çıktıyı metin veya grafik olarak görüntüleyin.
Lisans
MIT Lisansı.

yaml
Kodu kopyala

---

Bu yapı ile **FYS Studio Web Tabanlı Yorumlayıcı** projesi profesyonel bir seviyede tamamlanmıştır. Bu proje, kullanıcı dostu bir arayüz, gelişmiş kod düzenleyici ve grafiksel çıktı özellikleri ile kullanıcıların FYS Studio dilini tam anlamıyla kullanabilmesini sağlar.





