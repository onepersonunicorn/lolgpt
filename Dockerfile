# PlayMCP in KC (Git 소스 빌드) 등 컨테이너 배포용.
# ⚠️ ENV PORT=8000 필수 — main.py는 PORT가 있어야 Streamable HTTP(0.0.0.0:8000)로 뜬다.
#    (이전 Smithery stdio 전용 Dockerfile은 포트를 열지 않아 KC 헬스체크에서 Failed)
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

ENV PORT=8000
EXPOSE 8000

CMD ["python", "main.py"]
