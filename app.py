import pandas as pd
import matplotlib.pyplot as plt
#1. DataFrame
data = {
    'Họ và tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyên cần': [8.0, 8.5, 7.0, 9.0, 7.5, 6.0, 8.5, 7.0, 7.5, 9.0],
    'Giữa kỳ': [7.5, 8.0, 6.5, 9.0, 7.0, 6.0, 8.5, 7.0, 7.5, 9.0],
    'Cuối kỳ': [8.0, 8.5, 6.5, 9.0, 7.5, 6.0, 8.5, 7.0, 7.5, 9.5]
}
df = pd.DataFrame(data)

print("--- BẢNG DỮ LIỆU BAN ĐẦU ---")
print(df)
print("\n" + "="*50 + "\n")

#2. Tính điểm tổng kết
df['Tong_ket'] = (0.2 * df['Chuyên cần'] + 0.3 * df['Giữa kỳ'] + 0.5 * df['Cuối kỳ']).round(2)

#3. Xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    elif diem >= 7.0:
        return 'Khá'
    elif diem >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

print("--- BẢNG SAU KHI TÍNH TỔNG KẾT VÀ XẾP LOẠI ---")
print(df)
print("\n" + "="*50 + "\n")


#4. Thống kê
dtb_lop = df['Tong_ket'].mean()
max_sv = df.loc[df['Tong_ket'].idxmax()]
min_sv = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = len(df[df['Tong_ket'] >= 5.0])

print("--- THỐNG KÊ KẾT QUẢ HỌC TẬP ---")
print(f"Điểm tổng kết trung bình của lớp: {dtb_lop:.2f}")
print(f"Sinh viên có điểm tổng kết cao nhất: {max_sv['Họ và tên']} ({max_sv['Tong_ket']})")
print(f"Sinh viên có điểm tổng kết thấp nhất: {min_sv['Họ và tên']} ({min_sv['Tong_ket']})")
print(f"Số sinh viên đạt (điểm tổng kết >= 5): {so_sv_dat}")
print("\n" + "="*50 + "\n")

#5. Trực quan hóa
plt.figure(figsize=(10, 5))
plt.bar(df['Họ và tên'], df['Tong_ket'], color='skyblue', edgecolor='black')
plt.xlabel('Tên sinh viên')
plt.ylabel('Điểm tổng kết')
plt.title('Biểu đồ cột điểm tổng kết của 10 sinh viên')
plt.ylim(0, 10)

for i, val in enumerate(df['Tong_ket']):
    plt.text(i, val + 0.2, str(val), ha='center', va='bottom')

plt.show()
