# 🧠 AI Multi-Agent Article Generator  
### FastAPI • CrewAI • Streamlit • Ollama (Local LLM)

An end-to-end AI content generation system powered by a multi-agent pipeline using CrewAI.  
The system runs entirely on **free, local LLMs using Ollama**, and provides a production-style backend (FastAPI) and a clean frontend (Streamlit).

---

## 🚀 Features

- **Multi-Agent Pipeline**
  - Research Agent  
  - Analysis Agent  
  - Writing Agent  
  - Quality Check Agent  

- **FastAPI Backend**
  - `/run` to generate articles  
  - `/download/<filename>` to retrieve generated files  
  - Clean JSON response  
  - Topic-based filenames  

- **Streamlit Frontend**
  - Text input for topic  
  - Step-by-step agent output in tabs  
  - Downloadable Markdown files  
  - Connects seamlessly with FastAPI  

- **Local LLM via Ollama**
  - Runs Qwen 2.5 7B locally  
  - Fully offline  
  - Zero API cost  

---

## 🧠 Tech Stack

- Python  
- FastAPI  
- CrewAI  
- Streamlit  
- Ollama  
- Uvicorn  

---

## 📦 Installation

### 1. Clone the repository
git clone https://github.com/FarhanIbrahim03/ai-multi-agent-article-generator.git
cd ai-multi-agent-article-generator


### 2. Create & activate virtual environment
python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # Mac/Linux

### 3. Install dependencies
pip install -r requirements.txt

### 4. Install Ollama
Download: https://ollama.com/download  
Pull model: ollama pull qwen2.5:7b


## 🚀 Running the App

### 1. Start FastAPI backend
uvicorn main:app --reload
API docs:
http://localhost:8000/docs

### 2. Start Streamlit frontend
Open a second terminal:
streamlit run frontend.py
UI:
http://localhost:8501

---

## 📂 Project Structure
.
├── agents.py # Multi-agent definitions
├── tasks.py # Task descriptions for each agent
├── crew.py # CrewAI pipeline
├── main.py # FastAPI backend
├── frontend.py # Streamlit UI
├── outputs/ # Generated markdown files
└── requirements.txt


---

## 📄 How It Works

1. User enters a topic in Streamlit  
2. Frontend sends request → FastAPI `/run`  
3. CrewAI agents execute:
   - Research  
   - Analysis  
   - Writing  
   - Quality Check  
4. Final article saved as markdown in `outputs/`  
5. Streamlit displays results + provides download link  

---

## 🛠 Future Enhancements

- PDF output  
- Writing tone/style options  
- Step-by-step visual progress  
- Deployment on Render/Railway  
- Improved UI styling  

---

## 👨‍💻 Author  
**Farhan Ibrahim**  
AI/ML Developer  
GitHub: https://github.com/FarhanIbrahim03  
LinkedIn: https://www.linkedin.com/in/  

---

