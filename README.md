# Email Notification Microservice

This app demonstrates a Python-based REST API with background email notifications using Celery, Redis, and SendGrid.

## Features

- FastAPI for REST API
- Celery + Redis for background processing
- Retry logic on email failure
- Docker Compose setup

## Usage

1. Copy `.env.template` to `.env` and fill in your SendGrid details.
2. Run: `docker-compose up --build`
3. Test: POST to `http://localhost:8000/signup`

## Environment Variables

```env
REDIS_URL=redis://redis:6379/0
SENDGRID_API_KEY=your_key_here
FROM_EMAIL=your_verified_sender@example.com
