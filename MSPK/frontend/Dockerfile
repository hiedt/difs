FROM python:3.9.7-slim-buster

WORKDIR /app

RUN pip install --upgrade pip \
    && pip install streamlit

EXPOSE 8501

COPY . .

CMD ["streamlit", "run", "main.py"]