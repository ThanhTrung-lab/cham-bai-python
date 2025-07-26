import streamlit as st
import io
import contextlib

st.title("🧠 Chấm bài Python đơn giản")

uploaded_file = st.file_uploader("📤 Tải lên file .py", type=["py"])
if uploaded_file:
    code = uploaded_file.read().decode("utf-8")
    st.code(code, language="python")
    st.write("🔍 Kết quả chạy:")
    try:
        with contextlib.redirect_stdout(io.StringIO()) as f:
            exec(code, {})
        st.success("✅ Không có lỗi!")
        st.text(f.getvalue())
    except Exception as e:
        st.error(f"❌ Lỗi: {e}")
