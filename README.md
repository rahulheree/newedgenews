# 📰 Simple News Publisher – Backend

**Version 1.0** | *Open-source, zero-setup news API for solo publishers*  
**Built with FastAPI + PostgreSQL + JWT**  
Write. Publish. Share. No coding required.

---

### ✅ Features
- Full CRUD for news: headline, body, category, tags, media, captions  
- Auto image/video resize & optimization  
- Pagination with filters: `?category=sports&skip=0&limit=10`  
- Instant setup: DB tables auto-created at first run  
- Minimal auth: one default user (`publisher` / `secret`)  

---

### 🔐 Auth & JWT
**Login Credentials**  
- Username: `publisher`  
- Password: `secret`  
Get token:  
```bash
curl -X POST http://127.0.0.1:8000/api/v1/auth/login \
  -d "username=publisher" -d "password=secret"
Use: Authorization: Bearer <token>

⚙️ Tech Stack
FastAPI • Python 3.12 • PostgreSQL • SQLAlchemy 2.0 • Pillow • JWT
(Tailwind CSS planned for frontend)

🚀 Getting Started
bash
Copy
Edit
git clone https://github.com/yourname/simple-news-publisher-backend.git
cd simple-news-publisher-backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env          # edit DB_URL and SECRET_KEY in .env
uvicorn app.main:app --reload
Access: http://127.0.0.1:8000/docs (Swagger UI)

🔌 API Overview
Method	Endpoint	Purpose
POST	/api/v1/auth/login	Login & get JWT
GET	/api/v1/news	List all news articles
POST	/api/v1/news	Create article (multipart/form-data)
GET	/api/v1/news/{id}	Get article by ID
PUT	/api/v1/news/{id}	Update article
DELETE	/api/v1/news/{id}	Delete article

🧠 Roadmap
v2 – Coming Soon
• AI-powered auto-publishing (OpenAI API)
• Full-text search & elastic filtering
• Docker + docker-compose (one-liner deployment)

v3 – Planned
• Merge with Intelligent DataLens
• Real-time collaboration + AI Q&A
• Rich charts & dashboards
• Role-based multi-user support

🤝 Contributing
We ❤️ contributors!

main: stable v1

dev: active v2
Please open Issues or Discussions before large PRs.
Formatting: black + isort.

🪪 License
MIT – use freely.
Star ⭐ the repo if you liked it.

arduino
Copy
Edit

Let me know if you want a **frontend version**, deployment badge setup, or GitHub-ready repo boil
