# Su dung base image la python
FROM python:3.9-slim

# Thiet lap thu muc lam viec trong container
WORKDIR /app

# Cai dat Flask
RUN pip install Flask

# Sao chep ma nguon vao container
COPY app.py .

# Mo port 8000
EXPOSE 8000

# Lenh de chay ung dung khi container khoi dong
CMD ["python", "./app.py"]