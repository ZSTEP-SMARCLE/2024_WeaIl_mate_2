import streamlit as st
import re
import pandas as pd
import papermill as pm
from pytube import YouTube

print("start")
st.set_page_config(
    page_title="Mate"
    #page_icon=
)

if 'page' not in st.session_state:
    st.session_state.page = 'main'

def switch_page(page):
    st.session_state.page = page
    st.experimental_rerun()

def extract_urls(text, max_urls=3):
    # URL 추출을 위한 정규 표현식 패턴
    url_pattern = re.compile(r'(https?://\S+)')
    urls = url_pattern.findall(text)
    # 최대 max_urls 개수만큼 URL 추출
    return urls[:max_urls]

st.markdown(
    """
    <style>
    @font-face {
        font-family: 'Godo';
        font-style: normal;
        font-weight: 400;
        src: url('//fastly.jsdelivr.net/korean-webfonts/1/corps/godo/Godo/GodoM.woff2') format('woff2'), url('//fastly.jsdelivr.net/korean-webfonts/1/corps/godo/Godo/GodoM.woff') format('woff');
    }
    p {
        font-family: 'Godo';  /* 폰트 적용 */
        
    }
    .st-emotion-cache-1kyxreq div{
        max-width: 700px;
    }
    .st-emotion-cache-9aoz2h div{
        
    }
    [data-testid="stButton"] {
        display: flex;
        justify-content: flex-end;
    }
    [data-testid="stExpander"] {
        background-color: rgba(210, 206, 255, 0.5); /* 원하는 색상으로 변경 */
    }
    [data-testid="stExpanderToggleIcon"] {
        visibility: hidden;
        pointer-events: none;
    }
    .st-emotion-cache-p5msec {
        pointer-events: none;
        visibility: hidden;
    }
    .st-emotion-cache-9aoz2h e1vs0wn30 div{
        max-width: 100px;
    }
    [data-testid="stChatInputTextArea"] {
        background-color: rgba(210, 206, 255, 0.5); /* 원하는 색상으로 변경 */
    }
    [data-testid="baseButton-secondary"] {
        background-color:#c0bbff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

thumbnail_physical=[
    "https://img.youtube.com/vi/Cmt82yiNtQo/0.jpg",
    "https://img.youtube.com/vi/EcFVv-Ktj-U/0.jpg",
    "https://img.youtube.com/vi/IFnU3sYNs1U/0.jpg",
    "https://img.youtube.com/vi/28kn2IQEWRk/0.jpg",
    "https://img.youtube.com/vi/jIxspQ2Z2zo/0.jpg",
    "https://img.youtube.com/vi/os8Vym4xQwM/0.jpg"
]

thumbnail_mental=[
    "https://img.youtube.com/vi/mxq81tdtPXA/0.jpg",
    "https://img.youtube.com/vi/uvy9T_coMYw/0.jpg",
    "https://img.youtube.com/vi/iKPK99hQAJk/0.jpg",
    "https://img.youtube.com/vi/ULWUxxhzlo8/0.jpg",
    "https://img.youtube.com/vi/2u3G-vHNWLs/0.jpg",
    "https://img.youtube.com/vi/jpN8YqQV1N0/0.jpg"
]

youtube_physical=[
    "https://www.youtube.com/watch?v=Cmt82yiNtQo",
    "https://www.youtube.com/watch?v=EcFVv-Ktj-U",
    "https://www.youtube.com/watch?v=IFnU3sYNs1U",
    "https://www.youtube.com/watch?v=28kn2IQEWRk",
    "https://www.youtube.com/watch?v=jIxspQ2Z2zo",
    "https://www.youtube.com/watch?v=os8Vym4xQwM"
]

youtube_mental=[
    "https://www.youtube.com/watch?v=mxq81tdtPXA",
    "https://www.youtube.com/watch?v=uvy9T_coMYw",
    "https://www.youtube.com/watch?v=iKPK99hQAJk",
    "https://www.youtube.com/watch?v=ULWUxxhzlo8",
    "https://www.youtube.com/watch?v=2u3G-vHNWLs",
    "https://www.youtube.com/watch?v=jpN8YqQV1N0"
]

notebook_path = "WeaIl_gpt.ipynb"  # 실제 파일 경로로 변경
output_path = "output_gpt.ipynb"  # 결과 저장 경로 (선택 사항)
apikey = st.secrets["OPENAI_API_KEY"] # api키 받아오는거 

def chat(inputs):
    st.session_state.input = inputs
    #여기에 코랩 연결 필요합니다.
    nb = pm.execute_notebook(
        notebook_path,
        output_path,  # 결과 저장 (선택 사항)
        parameters={"input_string": inputs, "input_key": apikey},  # 변수 전달
        output_variables=["output_string"]
    )
    with open('output.txt', 'r') as file:
            output = file.read()

    #output="코랩연결 https://www.youtube.com/watch?v=Cmt82yiNtQo https://www.youtube.com/watch?v=jIxspQ2Z2zo https://www.youtube.com/watch?v=os8Vym4xQwM"
    #여기에 코랩 연결 필요합니다.
    st.session_state.answer = extract_urls(output, 3)
    print(st.session_state.answer)
    for k in st.session_state.answer:
        if k.endswith(')'):
            k=k[:-1]
    
    st.session_state.thumbnails = []
    for k in st.session_state.answer:
        yt = YouTube(k)
        st.session_state.thumbnails.append(yt.thumbnail_url) 
    print("gpt 실행")
    switch_page("result")

@st.experimental_dialog("추천 영상입니다.")    
def movie(url):
    st.video(url)
#=================[ 위 : 함수 부분 / 아래 : 작동 부분 ]===============

st.logo("./img/logo.png", link=None, icon_image=None)
#웹 배포 후엔 배포된 링크 넣으면 됨
if st.session_state.page == 'main':
    with st.container(height=100, border=0):
        st.empty()
    st.image("./img/ment.png", width=700)
    #st.subheader("장애 아동에게 꼭 필요한 학습 컨텐츠를 쉽고 간편하게 제공합니다.")
    if st.button("컨텐츠 추천받기"):
        print("챗봇으로 넘어가기")
        switch_page("search")
    
    st.image("./img/physical.png", width=330)
    #st.subheader("몸이 불편한 아동을 위한 추천 컨텐츠")
    with st.expander("", expanded=1):
        psc=st.columns(6)
        for i in range(6):
            with psc[i]:
                st.image(thumbnail_physical[i])
                if st.button("영상 보기", key=i+1, use_container_width=1):
                    movie(youtube_physical[i])
    st.image("./img/mental.png", width=360)
    #st.subheader("마음이 불편한 아동을 위한 추천 컨텐츠")
    with st.expander("",expanded=1):
        mtl=st.columns(6)
        for i in range(6):
            with mtl[i]:
                st.image(thumbnail_mental[i])
                if st.button("영상 보기", key=i+7, use_container_width=1):
                    movie(youtube_mental[i])
    

elif st.session_state.page == 'search':
    with st.container(height=100, border=0):
        st.empty()
    st.markdown("원하시는 컨텐츠가 있나요?")
    st.markdown("AI가 원하시는 학습 컨텐츠를 찾아드릴게요.")
    if st.button("메인화면"):
        print("메인으로 넘어가기")
        switch_page("main")
    col0, col1 = st.columns([1, 12])
    with col0:
        with st.popover(""):
            st.write("추천하는 검색어입니다.")
            if st.button("시각장애인을 위한 유튜브 추천", use_container_width=1):
                chat("시각장애인을 위한 유튜브 추천 영상을 추천해서 링크를 같이 첨부해줘. 단, 채널이나 유저가 아닌 영상의 링크만 첨부해줘.")
            if st.button("지적장애인을 위한 엔터테인먼트 영상", use_container_width=1):
                chat("지적장애인을 위한 엔터테인먼트 영상을 추천해줄 수 있나요? 유튜브 링크를 같이 첨부해줘요. 단, 채널이나 유저가 아닌 영상의 링크만 첨부해주세요.")
            if st.button("지체장애인을 위한 운동 영상", use_container_width=1):
                chat("지체장애인을 위한 운동 영상을 추천해서 링크를 같이 첨부해줘. 단, 채널이나 유저가 아닌 영상의 링크만 첨부해줘.")
    with col1:
        input_text = st.chat_input("여기에 입력해주세요.")
        if input_text:
            chat(input_text)     
                    
elif st.session_state.page == 'result':
    with st.container(height=100, border=0):
        st.empty()
    if st.button("메인화면"):
        print("메인으로 넘어가기")
        switch_page("main")    
    col0, col1 = st.columns([1, 12])
    with col0:
        with st.popover(""):
            st.write("추천하는 검색어입니다.")
            if st.button("시각장애인을 위한 유튜브 추천", use_container_width=1):
                chat("시각장애인을 위한 유튜브 추천 영상을 추천해서 링크를 같이 첨부해줘. 단, 채널이나 유저가 아닌 영상의 링크만 첨부해줘.")
            if st.button("지적장애인을 위한 엔터테인먼트 영상", use_container_width=1):
                chat("지적장애인을 위한 엔터테인먼트 영상을 추천해줄 수 있나요? 유튜브 링크를 같이 첨부해줘요. 단, 채널이나 유저가 아닌 영상의 링크만 첨부해주세요.")
            if st.button("지체장애인을 위한 운동 영상", use_container_width=1):
                chat("지체장애인을 위한 운동 영상을 추천해서 링크를 같이 첨부해줘. 단, 채널이나 유저가 아닌 영상의 링크만 첨부해줘.")
    with col1:
        input_text = st.chat_input("여기에 입력해주세요.")
        if input_text:
            chat(input_text)
    st.write("검색 결과입니다.")
    with st.expander("",expanded=1):
        ytv = st.columns(3)
        for i in range(3):
            with ytv[i]:
                print(st.session_state.answer[i])
                st.image(st.session_state.thumbnails[i])
                if st.button("영상 보기", key=i+20, use_container_width=1):
                    movie(st.session_state.answer[i])