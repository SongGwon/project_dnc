import streamlit as st

# 가상환경 프로젝트 추가(simple)
# streamlit 라이브러리 설치
# app.py 실행했을 때

st.title("NEWS COLLECTIOR")
st.text("DAUM 뉴스를 수집합니다.")

st.set_page_config(
    page_title= "뉴스 수집기"
    #pag_icon= "./image"
)

st.title("NEWS COLLECTOR")
st.text("DAUM 뉴스를 수집합니다.")

with st.form(key="form"):
    category = st.text_input("수집 할 뉴스 카테고리를 입력하세요.").strip()
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(category)






