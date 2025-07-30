# Simple News Publisher – Backend
**v1** – *Minimal, open-source, single-publisher news API*  
*Built for people who just want to share their voice without code.*

---

## 🚀 Current Version (v1)
- FastAPI + PostgreSQL + JWT  
- CRUD articles (headline, body, category, tags, media, captions)  
- Auto-resize & optimize images/videos  
- Pagination + category filters (`?category=sports&skip=0&limit=10`)  
- Zero-migration: tables auto-created on first run  
- Single hard-coded publisher login (`publisher / secret`)

---

## 🔮 Roadmap
| Phase | When | What’s coming |
|-------|------|---------------|
| **v2** | Soon™ | • AI auto-publishing via LLM (OpenAI API)<br>• Full-text search & elastic filters<br>• Docker & docker-compose for one-command deploy |
| **v3** | Later | • Merge with **Intelligent DataLens** stack:<br> – Real-time collaboration<br> – Advanced AI Q&A on news data<br> – Interactive charts & dashboards<br> – Multi-user / role-based permissions |

---

## 🧩 Tech Stack (v1)
Python 3.12 • FastAPI • PostgreSQL • SQLAlchemy 2.0 • JWT • Pillow • Tailwind (frontend later)

---

## ⚡ Quick Start
### 1. Clone & install
```bash
git clone https://github.com/yourname/simple-news-publisher-backend.git
cd simple-news-publisher-backend
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

2. Configure
bash
Copy
cp .env.example .env
# edit .env with your DB & secret key
3. Run
bash
Copy
uvicorn app.main:app --reload
Open http://127.0.0.1:8000/docs for interactive Swagger docs.
🔑 Default Login
Table
Copy
Field	Value
Username	publisher
Password	secret
Get token:
bash
Copy
curl -X POST http://127.0.0.1:8000/api/v1/auth/login \
  -d "username=publisher" -d "password=secret"
Use the returned token as Authorization: Bearer <token>.
🧪 API Endpoints (v1)
Table
Copy
Method	Path	Purpose
POST	/api/v1/auth/login	Obtain JWT
GET	/api/v1/news	List articles
POST	/api/v1/news	Create article (multipart/form-data)
GET	/api/v1/news/{id}	Get single article
PUT	/api/v1/news/{id}	Update article
DELETE	/api/v1/news/{id}	Delete article
🤝 Contributing
We ❤️ contributions!
Discussions: open an Issue or start a Discussion before big PRs.
Code style: black + isort.
Branches:
main – stable v1
dev – bleeding edge / v2 work
Ideas welcome: AI prompts, search algorithms, Docker setup, tests, etc.
🔗 Related Projects
https://github.com/yourname/intelligent-datalens – our earlier project that will merge into v3 for AI dashboards & real-time collaboration.
📄 License
MIT – feel free to fork, hack, and deploy.
Star ⭐ the repo if you like the idea!
