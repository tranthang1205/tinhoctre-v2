# Project THT V2

## Chuẩn bị

Yêu cầu `python3.8+`

Clone project

```bash
git clone [link] ~/tinhoctre
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