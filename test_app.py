from app import app

def test_home_page_status_code():
    """Kiểm tra trang chủ có trả về mã 200 OK không."""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

def test_home_page_content():
    """Kiểm tra trang chủ có chứa nội dung mong muốn không."""
    with app.test_client() as client:
        response = client.get('/')
        # Sửa lại chuỗi kiểm tra thành nội dung đúng
        assert b"CI/CD Pipeline" in response.data