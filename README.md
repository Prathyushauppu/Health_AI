# 🩺 Health_AI

Health_AI is a conversational AI & analytics-driven application designed to help users ask health-related questions, predict possible medical conditions from symptoms, and provide basic treatment guidance.  
This project combines FastAPI-based backend services, a simple web UI, and AI-powered responses.

---

##  📌 Features

- Ask health-related questions using natural language  
- Predict medical conditions based on user symptoms  
- Provide basic treatment suggestions  
- Web-based interface for user interaction  
- FastAPI backend with REST endpoints  
- Organized folder structure for easy scaling  
- Demo video available  

> ⚠️ _This application is for educational purposes only and should not be considered medical advice._

---

## 📂 Folder Structure

Health_AI/
│
├── Document/ # Documentation, reference files
│
├── Project file/ # Core project files, source code
│
├── Video Demo/ # Demo video files
│
└── README.md # Project Overview

yaml
Copy code

> If you provide the content of **Project file folder**, I can expand this section with exact code details.

---

## 🏗️ Tech Stack

| Component  | Technology |
|------------|------------|
| Backend    | FastAPI / Python |
| AI Model   | OpenAI API / LLM |
| Frontend   | Basic Web UI (HTML/JavaScript) |
| Deployment | Local / Cloud option |
| Docs       | Markdown |

---

## 🧠 Core Functionalities

### 🔹 1) **Ask Question**
Users can ask general medical questions.  
The system forwards the query to the AI engine to generate responses.

### 🔹 2) **Predict Condition**
User selects symptom(s) → AI evaluates → returns possible conditions.

Example Output:
Possible conditions:
• Common cold
• Sinusitis
• Flu

markdown
Copy code

### 🔹 3) **Treatment Suggestion**
Provides general guidance like:
• Drink fluids
• OTC medicines
• Visit clinician if persists

yaml
Copy code

---

## ⚙️ Setup & Installation

###  1) Clone the Repository
```bash
git clone https://github.com/Prathyushauppu/Health_AI.git
cd Health_AI
 2) Install Dependencies
bash
Copy code
pip install -r requirements.txt
If you share the dependencies file, I will update this section precisely.

 3) Run Server
bash
Copy code
uvicorn main:app --reload
Backend now available at:
➡ http://127.0.0.1:8000

▶️ Demo
A demo video can be found inside:

css
Copy code
/Video Demo
You may upload to YouTube + place link here.

🔌 API Endpoints (Expected)
Method	Endpoint	Description
POST	/ask	Ask general health questions
POST	/predict	Predict condition from symptoms
GET	/docs	Auto API documentation

🧪 Example Usage
 1) Ask Question
Request:

json
Copy code
{ "question": "How to reduce fever?" }
Response:

css
Copy code
• Stay hydrated
• Paracetamol
• Rest
🚀 Future Improvements
- Add ML-based symptom classification
- Add disease database
- Multi-language support
- Improved UI
- Chat history

⚠️ Disclaimer
This system is not a medical device.
For educational/testing only.
Consult a licensed doctor for real medical guidance.

👤 Author
Prathyusha Uppuluri (Prathyushauppu)
🔗 GitHub: https://github.com/Prathyushauppu
