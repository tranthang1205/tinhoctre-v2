# Project THT V2

## Chuẩn bị

Yêu cầu `python3.8+`

Clone project

```bash
git clone https://github.com/tranthang1205/tinhoctre-v2 ~/tinhoctre
```

```bash
cd ~/tinhoctre
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Khởi tạo Database

```bash
python3 manage.py migrate
```

## Tạo tài khoản Admin

```bash
python3 manage.py createsuperuser
```

## Chay server

```bash
python3 manage.py runserver
```

## Load data 
```bash
thư mục fixtures là thư mục lưu dữ liệu của datebase
file ing.yaml lưu toàn bộ dữ liệu
-> tạo file ing.yaml -> thêm dữ liệu -> upload data bằng câu lệnh: python3 manage.py loaddata ing
* Lưu ý: chỉ được loaddata 1 lần, muốn cập nhật thì xóa đi tạo lại
```

## Trick
#
- xuống dòng trong file ing.yaml -> thêm dấu `|`

```yaml
- model: backend.About
  pk: 1
  fields:
    name: Maruuu
    step: |
      Maru Mogi

      Maru Mogi

      Maru Mogi
```
#
- Mỗi khi sửa css nếu không nhận trong html thì sửa `?v=..`
```html
<link rel="stylesheet" href="{% static 'CSS/food.css' %}?v=3">
```