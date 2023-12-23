
#ReadingApp

## Mô Tả

Đây là API của ứng dụng ReadingApp, phát triển bởi nhóm 29.
## Cài Đặt

### Cài đặt Môi Trường Ảo

Trước hết, bạn cần cài đặt môi trường ảo Python:

```bash
python -m venv venv
```

### Kích Hoạt Môi Trường Ảo

Trên Windows:

```bash
venv\Scripts\activate
```

Trên macOS và Linux:

```bash
source venv/bin/activate
```

### Cài đặt Các Gói Phụ Thuộc

Cài đặt các gói cần thiết bằng pip:

```bash
pip install -r requirements.txt
```

## Chạy Ứng Dụng

Để chạy ứng dụng trên máy phát triển:

```bash
python manage.py runserver
```

## Phơi Bày API Sử Dụng ngrok

Cài đặt ngrok và chạy lệnh sau để phơi bày ứng dụng Django của bạn ra internet:

```bash
ngrok http 8000
```
Sao chép vào ALLOWED_HOSTS trong Settings và CSRF_TRUSTED_ORIGINS trong server/settings.py

## Giao Tiếp với API từ Java


Cập nhật vào values/strings.xml để lấy danh sách sách từ API:

```java
    <string name="api_base_url">https://b430-2405-4802-1cb2-a780-50b5-4adc-cecf-839f.ngrok-free.app/</string>
// Sử dụng Volley hoặc OkHttp để thực hiện yêu cầu mạng
```

---

 
