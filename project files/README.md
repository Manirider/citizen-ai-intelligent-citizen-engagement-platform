
# CitizenAI - Government AI Chat Assistant

## 🌟 Project Overview
**CitizenAI** is an AI-powered chat assistant designed to improve communication between citizens and the government. It allows users to ask questions, submit feedback, and report concerns. The system uses IBM’s **Granite 3.3 2B Instruct Model** for AI responses and sentiment analysis to classify user inputs as Positive, Neutral, or Negative.

## 🚀 Key Features
- 💬 **AI Chat Assistant:** Get instant, intelligent responses to citizen queries.
- 🧐 **Sentiment Analysis:** Classifies each citizen’s input to understand overall sentiment trends.
- 📝 **Concern Reporting:** Automatically tracks negative feedback for quick issue identification.
- 📊 **Citizen Dashboard:** Visualizes recent concerns and sentiment summaries.
- 🔐 **User Authentication:** Simple login/logout system with session management.
- 🎨 **Responsive Frontend:** Clean, user-friendly design with easy navigation.

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **AI Model:** IBM Granite 3.3 2B Instruct Model (via Hugging Face Transformers)
- **NLP Pipeline:** Sentiment Analysis (Hugging Face Pipeline)
- **Deployment:** (Render.com / Heroku / Local)

## 📂 Project Structure
CitizenAI/
│
├── app.py                # Flask backend logic
├── requirements.txt      # Project dependencies
├── templates/            # HTML templates
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   ├── chat.html
│   ├── dashboard.html
│   └── login.html
├── static/
│   ├── css/
│   │   └── styles.css    # Custom CSS
│   └── images/           # Background and icons
└── README.md             # Project documentation

## ⚙️ Installation & Setup
1. **Clone the repository:**
```bash
git clone https://github.com/your-username/citizenai.git
cd citizenai
```

2. **Set up a virtual environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the Flask application:**
```bash
python app.py
```

5. **Open your browser:**
```
http://127.0.0.1:5000/
```

## 🔐 Login Credentials
| Username | username |
|----------|----------|
| admin    | password |

## ✅ Usage Flow
1. **Login** → Access the chat assistant and dashboard.
2. **Chat** → Ask questions or report issues.
3. **Sentiment Analysis** → Automatically performed for each message.
4. **Dashboard** → View aggregated sentiment data and reported concerns.
5. **Logout** → Safely exit the session.

## 📷 Screenshots (Add your project screenshots here)
- Login Page
- Chat Assistant
- Dashboard
- Services Page
- About Page

## 🚀 Deployment (Optional)
You can deploy this project to platforms like:
- [Render.com](https://render.com/)
- [Heroku](https://heroku.com/)
- [PythonAnywhere](https://pythonanywhere.com/)

**I can help you step-by-step with deployment if you need.**

## 👨‍💻 Author
Surya – [Your Contact Info (optional)]

## 📜 License
This project is for educational purposes.
