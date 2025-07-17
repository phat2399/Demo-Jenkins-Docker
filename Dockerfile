# Su dung base image la python
FROM python:3.9-slim

# Thiet lap thu muc lam viec trong container
WORKDIR /app

# Sao chep file requirements.txt va cai dat cac thu vien
# Day la buoc quan trong de cai dat pytest
COPY requirements.txt .
RUN pip install -r requirements.txt

# Sao chep toan bo ma nguon vao container
COPY . .

# Mo port 8000
EXPOSE 8000

# Lenh de chay ung dung khi container khoi dong
CMD ["python", "./app.py"]