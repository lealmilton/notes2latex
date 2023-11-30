FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN python -m pip install -U pip

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y poppler-utils binutils texlive && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "app.py"]
