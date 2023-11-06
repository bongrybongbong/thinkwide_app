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

meeting_data = ' **ThinkWide 가상 회의록 (일부)**

**회의 날짜:** 2023년 11월 4일  
**참석자:** 김태희(팀장), 이민호(개발자), 박서준(기획자), 정수정(UI/UX 디자이너), 최우식(마케팅 담당자)

---

**김태희:** 여러분, 오늘 모인 주제는 ThinkWide의 VR 마인드맵 도구 개발에 대한 논의입니다. 각자의 의견을 자유롭게 나눠보도록 해요.

**이민호:** 저희가 우선 해결해야 할 것은 VR 헤드셋 호환성이에요. 다양한 제조사의 헤드셋을 지원해야 하니까요.

**박서준:** 맞아요, 사용자가 자신이 이미 가지고 있는 장비로 바로 접속할 수 있게 하는 것이 중요하죠. 기획적으로는 사용자 경험을 최우선에 두고 싶어요.

**정수정:** UI/UX 측면에서도 그렇습니다. VR에서는 직관적인 인터페이스가 필수적이에요. 손짓 하나로도 마인드맵의 노드를 쉽게 조작할 수 있도록 디자인하려고 해요.

**최우식:** 마케팅 관점에서 볼 때, 우리 서비스의 독창성을 강조해야 해요. VR 마인드맵이라는 점을 부각시켜야 시장에서 주목받을 수 있을 거예요.

**김태희:** 좋습니다. 그럼 이민호님, VR 컨트롤러에 대한 지원은 어떻게 진행하고 있나요?

**이민호:** 현재 HTC Vive와 Oculus Rift의 컨트롤러에 대한 지원을 개발 중입니다. 다른 제품에 대해서도 호환성을 확장할 계획이에요.

**박서준:** 그리고 가상 공간의 레이아웃은 사용자가 마인드맵을 최대한 쉽게 확장할 수 있게 설계되어야 해요. 사용자가 공간의 제약을 느끼지 않도록요.

**정수정:** 네, 그 부분에 대해서는 저도 동의해요. 사용자가 공간에 대한 제약 없이 창의력을 발휘할 수 있도록 하는 것이 중요하니까요.

**최우식:** 그리고 우리 서비스의 이용 사례들을 마케팅 자료로 만들어야 할 것 같아요. 실제로 사람들이 VR 마인드맵을 어떻게 활용할 수 있는지 보여줄 수 있으면 좋겠네요.

**김태희:** 모두 좋은 의견입니다. 오늘 논의한 내용을 바탕으로 각자의 업무에 착수하도록 하고, 정기적으로 진행 상황을 공유합시다. 회의를 마치겠습니다.'



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
    st.markdown(meeting_data)

