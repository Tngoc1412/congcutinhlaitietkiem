import streamlit as st
st.image("logo.jpg")
# Cấu hình trang
st.set_page_config(page_title="Tính Lãi Tiết Kiệm", page_icon="💰", layout="centered")

st.title("💰 Ứng Dụng Tính Lãi Gửi Tiết Kiệm_NGUYỄN HỒ THẢO NGỌC")

# Tạo form nhập liệu với 2 cột cho gọn gàng
col1, col2 = st.columns(2)

with col1:
    so_tien_gui = st.number_input("Số tiền gửi (VNĐ):", min_value=0.0, value=100000000.0, step=1000000.0, format="%.0f")
    ky_han = st.number_input("Kỳ hạn (Tháng):", min_value=1, value=6, step=1)

with col2:
    lai_suat = st.number_input("Lãi suất (%/năm):", min_value=0.0, value=5.0, step=0.1)
    hinh_thuc = st.selectbox("Hình thức nhận lãi:", ["Cuối kỳ", "Hàng tháng", "Hàng quý"])

# Nút thực hiện tính toán
if st.button("🧮 Tính Toán", type="primary"):
    # Công thức tính lãi suất cơ bản: Tiền lãi = Số tiền gửi * Lãi suất * (Kỳ hạn / 12)
    tong_tien_lai = so_tien_gui * (lai_suat / 100) * (ky_han / 12)
    tong_tien_goc_lai = so_tien_gui + tong_tien_lai
    
    # Xử lý tính toán tiền lãi định kỳ theo hình thức nhận
    if hinh_thuc == "Cuối kỳ":
        tien_lai_dinh_ky = tong_tien_lai
        nhan_label = "Tiền lãi nhận cuối kỳ"
    
    elif hinh_thuc == "Hàng tháng":
        tien_lai_dinh_ky = tong_tien_lai / ky_han
        nhan_label = "Tiền lãi nhận hàng tháng"
    
    elif hinh_thuc == "Hàng quý":
        # Kiểm tra nếu kỳ hạn nhỏ hơn 1 quý (3 tháng)
        if ky_han < 3:
            st.warning("⚠️️ Kỳ hạn dưới 3 tháng không thể áp dụng nhận lãi hàng quý. Hệ thống đang hiển thị mức nhận lãi cuối kỳ.")
            tien_lai_dinh_ky = tong_tien_lai
            nhan_label = "Tiền lãi nhận cuối kỳ"
        else:
            so_quy = ky_han / 3
            tien_lai_dinh_ky = tong_tien_lai / so_quy
            nhan_label = "Tiền lãi nhận hàng quý"

    # Hiển thị kết quả tính toán
    st.markdown("---")
    st.subheader("📊 Kết Quả Tính Toán")
    
    # Sử dụng st.metric để giao diện hiển thị đẹp và chuyên nghiệp hơn
    st.metric("Tổng số tiền gốc và lãi", f"{tong_tien_goc_lai:,.0f} VNĐ")
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric("Tổng tiền lãi", f"{tong_tien_lai:,.0f} VNĐ")
    with col_res2:
        st.metric(nhan_label, f"{tien_lai_dinh_ky:,.0f} VNĐ")
