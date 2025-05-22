# Email Notification Microservice 🚀

This project demonstrates a Python microservices-based architecture for sending email notifications using:

- 🧩 FastAPI for the REST API
- ⚙️ Celery for background task processing
- 💌 SendGrid for email delivery
- 🧠 Retry logic with exponential backoff
- 🐳 Docker Compose for orchestration

---

## 📁 Project Structure

```
email_notification_app/
├── .env.template
├── docker-compose.yml
├── user_service/
│   ├── Dockerfile
│   ├── main.py
│   ├── celery_app.py
│   └── requirements.txt
├── worker/
│   ├── Dockerfile
│   ├── tasks.py
│   ├── celery_app.py
│   └── requirements.txt
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/email-notification-app.git
cd email-notification-app
```

### 2. Create Your `.env` File

Copy the template and fill in your SendGrid details:

```bash
cp .env.template .env
```

Edit `.env`:

```env
REDIS_URL=redis://redis:6379/0
SENDGRID_API_KEY=your_sendgrid_api_key_here
FROM_EMAIL=your_verified_sender@example.com
```

> ⚠️ Make sure the `FROM_EMAIL` is a verified sender in your SendGrid dashboard.

---

### 3. Run the App

```bash
docker-compose up --build
```

- FastAPI available at: `http://localhost:8000`
- Celery worker runs in background, listens to Redis

---

## 📬 Test the Email Notification

Use `curl` or Postman to send a signup request:

```bash
curl -X POST http://localhost:8000/signup \
  -H "Content-Type: application/json" \
  -d '{"email": "your_email@example.com", "name": "YourName"}'
```

✅ If successful, you should see the email in your inbox!

---

## 🔁 Retry Logic

If email sending fails, Celery will:
- Retry up to 3 times
- Use exponential backoff (wait longer each time)

---

## 📌 Future Improvements

- Add Flower dashboard for monitoring Celery
- Store email delivery logs in PostgreSQL
- Add authentication to the API

---

## 📝 License

This project is open-source and free to use. MIT License.
