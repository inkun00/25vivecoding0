import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 진로 추천 🌟",
    page_icon="🚀",
    layout="wide",
)

# 화려한 CSS 스타일 및 애니메이션
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
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to   { opacity: 1; transform: translateY(0); }
}
.job-card {
    background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%);
    border-radius: 15px;
    margin: 1rem 0;
    overflow: hidden;
    transition: transform 0.3s, box-shadow 0.3s;
}
.job-card:hover {
    transform: scale(1.02);
    box-shadow: 0 8px 30px rgba(0,0,0,0.2);
}
.job-card summary {
    font-size: 1.2rem;
    font-weight: bold;
    cursor: pointer;
    padding: 1rem;
    list-style: none;
    outline: none;
}
.job-card summary::-webkit-details-marker {
    display: none;
}
.job-card[open] {
    background: linear-gradient(135deg, #c2e9fb 0%, #a1c4fd 100%);
}
.job-desc {
    padding: 1rem;
    font-size: 1rem;
    line-height: 1.4;
    animation: fadeIn 0.4s ease-out;
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

# 추가 기능용 매핑
study_methods = {
    "✨ INFP ✨": ["감성 일기를 쓰며 복습하기", "소규모 스터디 그룹에서 토론하기"],
    "🌟 INFJ 🌟": ["체계적인 플래너 작성", "마인드맵으로 정리하기"],
    # ... 나머지 유형도 유사한 리스트로 추가
}
compatible_friends = {
    "✨ INFP ✨": ["🌈 ESFP 🌈", "💡 ENTP 💡"],
    "🌟 INFJ 🌟": ["✨ ENFP ✨", "🔑 ISFJ 🔑"],
    # ... 나머지
}
strengths = {
    "✨ INFP ✨": "높은 공감 능력과 창의성",  
    "🌟 INFJ 🌟": "통찰력과 강한 직관력",  
    # ... 나머지
}
weaknesses = {
    "✨ INFP ✨": "결정을 미루는 경향",  
    "🌟 INFJ 🌟": "과도한 자기비판",  
    # ... 나머지
}

# 각 직업 설명 매핑
job_descriptions = {
    # 기존 매핑 유지
}

# 추천 표시
st.markdown(f"## 🔎 {selected_mbti} 유형을 위한 추천 직업 🔍", unsafe_allow_html=True)
for job in recommendations.get(selected_mbti, []):
    desc = job_descriptions.get(job, "상세 설명이 준비 중입니다.")
    html = f"""
<details class="job-card">
  <summary>{job}</summary>
  <div class="job-desc">{desc}</div>
</details>
"""
    st.markdown(html, unsafe_allow_html=True)

# 추가 정보 표시
st.markdown("---")
st.markdown("### 📚 추천 공부 방법")
for method in study_methods.get(selected_mbti, []):
    st.markdown(f"- {method}")

st.markdown("### 🤝 잘 맞는 친구 MBTI 유형")
st.markdown(", ".join(compatible_friends.get(selected_mbti, [])))

st.markdown("### 💪 강점 (좋은 점)")
st.markdown(strengths.get(selected_mbti, "정보가 없습니다."))

st.markdown("### ⚠️ 신경 써야 할 점")
st.markdown(weaknesses.get(selected_mbti, "정보가 없습니다."))

# 푸터
st.markdown("---")
st.markdown("**당신의 꿈을 응원합니다! 🌟 새로운 커리어 여정, 지금 시작해보세요! 🚀**")
