import streamlit as st

st.title('학교급 및 학년 선택')

# 학교급 선택
school_type = st.radio('학교급을 선택하세요:', ['초등학교', '중학교', '고등학교'])

# 학년 선택 (학교급에 따라 동적으로 변경)
if school_type == '초등학교':
    grade = st.radio('학년을 선택하세요:', [f'{i}학년' for i in range(1, 7)])
    st.write(f'선택한 학교급: {school_type}, 학년: {grade}')
elif school_type == '중학교':
    grade = st.radio('학년을 선택하세요:', [f'{i}학년' for i in range(1, 4)])
    st.write(f'선택한 학교급: {school_type}, 학년: {grade}')
elif school_type == '고등학교':
    grade = st.radio('학년을 선택하세요:', [f'{i}학년' for i in range(1, 4)])
    st.write(f'선택한 학교급: {school_type}, 학년: {grade}')
