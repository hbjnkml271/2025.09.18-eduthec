import streamlit as st

st.title('Streamlit 데모 앱')
st.header('여러가지 Streamlit 요소 예시')

# 텍스트
st.write('이것은 일반 텍스트입니다.')

# 버튼
if st.button('버튼을 눌러보세요!'):
    st.success('버튼이 눌렸습니다!')


# 입력창
name = st.text_input('이름을 입력하세요:')
if name:
    st.write(f'안녕하세요, {name}님!')

# 성별 선택
gender = st.radio('성별을 선택하세요:', ['남성', '여성'])
st.write(f'선택한 성별: {gender}')

# 슬라이더
age = st.slider('나이', 0, 100, 25)
st.write(f'선택한 나이: {age}')

# 체크박스
if st.checkbox('차트 보여주기'):
    import numpy as np
    import pandas as pd
    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(df)

# 이미지
st.image('https://static.streamlit.io/examples/dog.jpg', caption='강아지 이미지')

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
