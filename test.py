import numpy as np
import pandas as pd
import streamlit as st
import datetime
import json
from mindmap import render_markdown
from pyvis.network import Network
from streamlit_markmap import markmap

def styled_text(text, background_color='yellow'):
    # span 태그를 사용하여 배경색 적용
    html_str = f"<span style='background-color:{background_color};'>{text}</span>"
    st.markdown(html_str, unsafe_allow_html=True)

def styled_hashtag(text, bg_color='#0d6efd', text_color='white'):
    # 스타일링된 해시태그를 위한 HTML 코드
    html_str = f"""
    <span style='
        background-color:{bg_color};
        color: {text_color};
        padding: 0.2em 0.5em;
        border-radius: 0.3em;
        font-size: 1em;
        margin: 0.1em;'>#{text}</span>
    """
    st.markdown(html_str, unsafe_allow_html=True)



name = '봉봉'
data = {
  "ThinkWide": {
    "기술개발": {
      "하드웨어 호환": [
        {"VR 헤드셋 지원": []},
        {"컨트롤러 옵션": []}
      ],
      "소프트웨어 인터랙션": [
        {"손동작 인식": []},
        {"음성 명령": []}
      ],
      "개발도구 통합": [
        {"Unity, Unreal Engine 플러그인": []}
      ],
      "네트워킹 및 안정성": [
        {"멀티플레이어 지원": []},
        {"데이터 동기화": []}
      ]
    },
    "플랫폼 구성": {
      "가상 현실 공간 설계": [
        {"공간의 레이아웃": []},
        {"상호작용 가능한 객체": []}
      ],
      "3D 모델링 및 아바타 시스템": [
        {"사용자 정의 아바타": []},
        {"표정 및 몸짓 표현": []}
      ],
      "데이터 관리 및 개인화 설정": [
        {"사용자 정보 저장": []},
        {"마인드맵 설정 기억": []}
      ]
    },
    "UI/UX 디자인": {
      "인터페이스 디자인": [
        {"직관적인 메뉴": []},
        {"가이드와 튜토리얼": []}
      ],
      "접근성 및 사용성 테스트": [
        {"다양한 사용자 테스트": []},
        {"피드백 반영": []}
      ]
    },
    "비즈니스 모델": {
      "시장 조사 및 경쟁 분석": [
        {"타겟 시장 정의": []},
        {"경쟁 서비스 분석": []}
      ],
      "가격 책정 및 수익 모델": [
        {"구독 모델, 일회성 구매": []},
        {"프리미엄 기능 설정": []}
      ],
      "마케팅 전략 및 브랜드 구축": [
        {"SNS, 인플루언서 마케팅": []},
        {"브랜딩 자료 개발": []}
      ]
    }
  }
}

st.set_page_config(page_title="markmap", layout="wide")





markdown_content = render_markdown(data)


st.header('🫧 {0}님의 첫 번째 마인드맵 : **ThinkWide** 프로젝트 가상 회의록 💡'.format(name))
st.markdown("""---""")
st.subheader('🪐회의 요약 :')
st.markdown('ThinkWide의 VR 마인드맵 도구 개발에 초점을 맞추어, 다양한 VR 헤드셋 호환성, 사용자 친화적인 인터페이스 및 컨트롤러 지원, 가상 공간 설계의 최적화, 그리고 마케팅 전략 수립에 대해 토론하고 구체적인 작업 방향을 설정했어요!:sparkles:')

hashtags = ["비즈니스 모델", "사용자 경험", "#UI/UX디자인", "기술개발", "테스트계획"]
colors = ["#FF6B6B", "#6BCB77", "#D65DB1", "#30475E", "#F7B801"]

for tag, color in zip(hashtags, colors):
    styled_hashtag(tag, color)


st.markdown("""---""")
with open('structured_markdown_data.md', encoding='utf-8') as fp:
    md = fp.read()
markmap(md,height=400)


## MultiSelect
location = st.multiselect("확인을 원하시는 키워드를 선택하세요",
                          ("사용자 경험", "비즈니스 모델", "UI/UX 디자인",
                           "기술 개발","테스트 계획"))
st.write(len(location), "가지를 선택했습니다.")




tab1, tab2, tab3 = st.tabs(["MINDMAP-NODE🫧", "키워드분석📈", "회의분석📊"])

with tab1:
    st.markdown('')
    st.markdown(markdown_content, unsafe_allow_html=True)




with tab2:
    st.markdown(f'#### 가장 많이 언급된 단어에요!')
    st.write("  ")
    st.markdown(f'##### 🥇 s')
    st.markdown(f'##### 🥈 s')
    st.markdown(f'##### 🥉 s')


with tab3:
    st.markdown(f'#### 냠냠 쩝쩝. 냠냠 쩝쩝.')
    st.markdown(f'※ 하하 호호')

