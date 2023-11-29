FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y poppler-utils pandoc binutils

RUN apt-get install -y texlive

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
