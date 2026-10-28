# Gaussian-Distribution

Bài thực hành về phân phối chuẩn (Gaussian) bằng Python: sinh dữ liệu,
vẽ biểu đồ và kiểm tra tính chuẩn.

## Nội dung

- Sinh dữ liệu Gaussian với `np.random.normal`
- Vẽ histogram và đường mật độ xác suất
- Kiểm tra tính chuẩn: skewness, kurtosis, Shapiro-Wilk, Q-Q plot

## Yêu cầu

- Python 3.9 trở lên
- Các thư viện trong `requirements.txt`

## Cài đặt và chạy

```bash
git clone https://github.com/mongthedan-jpg/Gaussian-Distribution.git
cd Gaussian-Distribution
pip install -r requirements.txt
python Gaussian.py
```

## Công thức

f(x) = 1 / (σ√(2π)) · exp(−(x − μ)² / (2σ²))

Quy tắc 68-95-99.7: khoảng 68% giá trị nằm trong ±1σ, 95% trong ±2σ,
99.7% trong ±3σ.

## Tác giả

mongthedan-jpg
