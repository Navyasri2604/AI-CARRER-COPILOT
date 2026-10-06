# AI Career Copilot

AI Career Copilot is a powerful, locally-run web application designed to help you build a clear, actionable path to your next career move. It analyzes your resume, compares it against your target role, builds a customized roadmap, and helps you practice for interviews.

## 🚀 Tech Stack

- **Frontend**: React (Vite), React Router, Lucide Icons, Custom CSS (Glassmorphism, Dark Mode)
- **Backend**: Django 3.2, Django REST Framework, SQLite
- **AI/ML**: Natural Language Processing (Local), TF-IDF Vectors, PyMuPDF for document parsing

## ✨ Key Features

- **Resume Analysis**: Upload your PDF/DOCX resume and receive an instant, AI-powered breakdown of your skills, formatting, and ATS compatibility.
- **Career Roadmapping**: Generate a targeted, step-by-step learning plan comparing your current skill set to your desired role.
- **Interview Lab**: Practice behavioral and technical questions tailored to your field with structured feedback.
- **Skill Gap Identification**: Pinpoint exactly which skills you need to learn to maximize your leverage.
- **Modern UI/UX**: Enjoy a sleek, premium, highly responsive user interface.

## 🛠️ Getting Started

### Prerequisites

- Node.js (v18+)
- Python (v3.7+)

### 1. Clone the repository

```bash
git clone https://github.com/Navyasri2604/AI-CARRER-COPILOT.git
cd AI-CARRER-COPILOT
```

### 2. Set up the Django Backend

Navigate to the backend directory and set up the Python virtual environment:

```bash
cd AI-CARRER-COPILOT-main
python -m venv env
env\Scripts\activate  # On Windows
# source env/bin/activate # On macOS/Linux

# Install dependencies
pip install -r requirements.txt
pip install Django==3.2.20 django-crispy-forms==1.14.0 djangorestframework==3.14.0 PyMuPDF python-dotenv

# Run migrations
python manage.py migrate

# Start the Django development server
python manage.py runserver
```

The backend server will run on `http://localhost:8000`.

### 3. Set up the React Frontend

Open a new terminal window/tab, navigate to the frontend directory, and start the Vite server:

```bash
cd frontend
npm install
npm run dev
```

The React frontend will be available at `http://localhost:5173`. 

---
*Built with modern web technologies.*
