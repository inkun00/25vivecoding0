import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 진로 추천 🌟",
    page_icon="🚀",
    layout="wide",
)

# 화려한 CSS 스타일
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
}
.stApp {
    background: rgba(255, 255, 255, 0.9) !important;
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
}
.job-card {
    background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%);
    border-radius: 15px;
    padding: 1rem;
    margin: 0.5rem;
    text-align: center;
    transition: transform 0.3s;
}
.job-card:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# 헤더
st.markdown("# 🎉 당신만을 위한 MBTI 직업 추천 🎉")
st.markdown("---")

# MBTI 리스트
mbti_list = [
    "✨ INFP ✨", "🌟 INFJ 🌟", "💎 INTJ 💎", "🔑 ISFJ 🔑",
    "❄️ ISTJ ❄️", "🎨 ISTP 🎨", "🌊 ISFP 🌊", "⚡ ESTP ⚡",
    "🌈 ESFP 🌈", "🌻 ESFJ 🌻", "🚀 ENFJ 🚀", "💡 ENTP 💡",
    "🎯 ESTJ 🎯", "🔥 ENTJ 🔥", "🔍 ISFJ 🔍", "✨ ENFP ✨"
]

# 사이드바 선택
st.sidebar.markdown("## 🌈 성격 유형 선택")
selected_mbti = st.sidebar.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

# 추천 매핑
recommendations = {
    "✨ INFP ✨": ["🎨 아티스트", "✍️ 작가", "🧘‍♂️ 상담가"],
    "🌟 INFJ 🌟": ["🧑‍🏫 교수", "🖋️ 편집자", "🌱 사회복지사"],
    "💎 INTJ 💎": ["🔬 연구원", "📊 데이터 분석가", "💻 소프트웨어 엔지니어"],
    "🔑 ISFJ 🔑": ["🏥 간호사", "👩‍🏫 교사", "🏛️ 박물관 큐레이터"],
    "❄️ ISTJ ❄️": ["📚 행정가", "⚖️ 변호사", "🏗️ 건축가"],
    "🎨 ISTP 🎨": ["🚗 자동차 정비사", "🔧 기계 엔지니어", "🎥 영화 촬영감독"],
    "🌊 ISFP 🌊": ["📸 사진작가", "🎵 뮤지션", "👗 패션 디자이너"],
    "⚡ ESTP ⚡": ["🏀 프로 운동선수", "💼 세일즈 전문가", "🎤 이벤트 기획자"],
    "🌈 ESFP 🌈": ["💃 무용가", "🎭 배우", "🥳 파티 플래너"],
    "🌻 ESFJ 🌻": ["🍽️ 호텔 매니저", "👨‍👩‍👧‍👦 HR 담당자", "🎓 유치원 교사"],
    "🚀 ENFJ 🚀": ["🎤 연설가", "📣 마케팅 매니저", "🕊️ NGO 활동가"],
    "💡 ENTP 💡": ["💡 스타트업 창업가", "🧪 연구 발명가", "📺 방송인"],
    "🎯 ESTJ 🎯": ["🏛️ 공무원", "📈 경영 컨설턴트", "💼 CEO"],
    "🔥 ENTJ 🔥": ["📊 전략 기획자", "🏢 기업 이사", "🚀 프로젝트 매니저"],
    "🔍 ISFJ 🔍": ["🏥 물리치료사", "🧶 공예가", "📔 기록물 관리자"],
    "✨ ENFP ✨": ["🎨 그래픽 디자이너", "✈️ 여행 작가", "🎮 게임 개발자"],
}

# 각 직업 설명 매핑 (예시)
job_descriptions = {}
for jobs in recommendations.values():
    for job in jobs:
        job_descriptions[job] = f"{job}은(는) 이 직업의 주요 역할과 필요 역량을 설명하는 자리입니다. 자신의 성향과 흥미를 고려해 선택해 보세요!"

# 추천 표시 및 팝업
st.markdown(f"## 🔎 {selected_mbti} 유형을 위한 추천 직업 🔍")
cols = st.columns(3)
for idx, job in enumerate(recommendations.get(selected_mbti, [])):
    with cols[idx]:
        if st.button(job, key=f"{selected_mbti}_{idx}"):
            with st.modal(job):
                st.markdown(f"### {job}")
                st.write(job_descriptions.get(job, "상세 설명이 준비 중입니다."))

# 푸터
st.markdown("---")
st.markdown("**당신의 꿈을 응원합니다! 🌟 새로운 커리어 여정, 지금 시작해보세요! 🚀**")
