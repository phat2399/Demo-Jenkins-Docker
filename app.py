from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    html_content = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <title>Jenkins & Docker Demo</title>
        <style>
            body {{
                background-color: #2c3e50; /* Nền tối */
                color: #ecf0f1; /* Chữ sáng */
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                text-align: center;
                padding: 40px;
                border-radius: 10px;
                background-color: #34495e;
            }}
            h1 {{
                color: #1abc9c; /* Màu xanh ngọc */
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 CI/CD Pipeline Đã Tự Động Cập Nhật Nhé!</h1>
            <p>Trang này đã được triển khai tự động bởi Jenkins.</p>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)