FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

#COPY src /app/src
COPY . .

# Run tests first, DUH! We can't deploy crap code!
RUN pip install --no-cache-dir -r test/requirements.txt
RUN pytest /app

EXPOSE 8501

CMD [ "streamlit", "run", "src/main.py" ]