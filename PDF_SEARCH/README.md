## Giới Thiệu
### Cấu trúc
```
Script_Python/
└── PDF_SEARCH/
    ├── findpdf.py
    ├── README.md
    └── requirements.txt
```
### requirements
Khởi tạo
`pip install -r requirements.txt`
thay đổi đường dẫn trong `findpdf.py`.
nếu không sử dụng GPU thì thay đổi `reader = easyocr.Reader(['en'], gpu=True)` `gpu=True` sang `gpu=False`
