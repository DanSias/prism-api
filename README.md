# PrismAPI

**PrismAPI** is a FastAPI-powered backend for executing AI prompts and managing user data. It offers secure endpoints, user authentication, and prompt history logging, making it easy to integrate with any front-end application.

## 🚀 Features

- FastAPI with automatic OpenAPI documentation
- Secure user management with JWT authentication
- Google Gemini AI integration for prompt execution
- `.env` support with `python-dotenv`
- Structured project layout for scalability
- Docker support for easy deployment

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/prism-api.git
cd prism-api
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file using the `.env.example` template:

```bash
cp .env.example .env
```

Edit `.env` and add your Google Gemini API key:

```env
GOOGLE_GEMINI_API_KEY="your-google-api-key"
DATABASE_URL="sqlite:///./prism_api.db"
ENVIRONMENT="development"
```

### 5. Run the Server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

- API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧪 Testing

Run tests using `pytest` (if installed):

```bash
pytest
```

---

## 🐳 Docker Support

Build and run the Docker container:

```bash
docker build -t prism-api .
docker run -p 8000:8000 prism-api
```

---

## 📂 Project Structure

```
prism-api/
├── .env               # Environment variables
├── .gitignore         # Git ignore rules
├── Dockerfile         # Docker container settings
├── README.md          # Project documentation
├── requirements.txt   # Python dependencies
└── app/
    ├── main.py        # FastAPI entry point
    ├── config.py      # Configuration settings
    ├── routes/        # API endpoints
    ├── models/        # Database models
    ├── schemas/       # Pydantic schemas
    └── services/      # Business logic and integrations
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is licensed under the MIT License.
