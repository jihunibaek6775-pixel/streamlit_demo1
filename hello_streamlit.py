# hello_streamlit.py
import streamlit as st

# 제목 추가
st.title("🎉 내 첫 번째 Streamlit 앱!")

# 사이드바에 통계 추가
st.sidebar.divider()
st.sidebar.subheader("📊 통계")

col1, col2 = st.sidebar.columns(2)
with col1:
    st.metric("총 프롬프트", "127")
with col2:
    st.metric("총 사용자", "23")

st.sidebar.metric("오늘 등록", "5", delta="2")

# 홈 화면에 검색바 추가
search_query = st.text_input(
    "🔍 프롬프트 검색",
    placeholder="키워드를 입력하세요..."
)

if search_query:
    st.info(f"'{search_query}' 검색 결과 (기능 구현 예정)")




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