FROM python:3.9-slim
WORKDIR /app
COPY serwis.py .
# Informujemy Dockera, że aplikacja nasłuchuje na porcie 8080
EXPOSE 8080
CMD ["python", "serwis.py"]
