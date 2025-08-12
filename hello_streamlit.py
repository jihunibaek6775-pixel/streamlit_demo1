# hello_streamlit.py
import streamlit as st

# 제목 추가
st.title("🎉 내 첫 번째 Streamlit 앱!")

# 텍스트 추가
st.write("안녕하세요! Streamlit으로 만든 웹 애플리케이션입니다.")

# 버튼 추가
if st.button("클릭해보세요!"):
    st.success("버튼이 클릭되었습니다! 🎊")

# 실행방법
# python hello_streamlit.py (x)
# streamlit run hello_streamlit.py (o)

# app.py의 제목 부분 수정
st.title("🐦 프롬프트 트위터 v1.1")  # 버전 추가
st.markdown("**유용한 LLM 프롬프트를 공유하는 공간입니다** ✨")  # 이모지 추가

st.title("오류 발생 없이 재배포 도전하기")