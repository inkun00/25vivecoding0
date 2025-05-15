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

# 직업 설명
job_descriptions = {
    # (생략: 이전에 작성된 그대로 유지)
}

# 추가 기능용 매핑: 추천 공부 방법
study_methods = {
    "✨ INFP ✨": ["감정일기로 자기 성찰하기", "창의적 글쓰기 워크숍 참여하기"],
    "🌟 INFJ 🌟": ["심리학 서적 탐구하기", "목표 로드맵 작성하기"],
    "💎 INTJ 💎": ["논리적 플래닝 연습하기", "데이터 분석 프로젝트 수행하기"],
    "🔑 ISFJ 🔑": ["케이스 스터디 학습", "조직적 학습 계획 짜기"],
    "❄️ ISTJ ❄️": ["체계적 노트 정리하기", "과거 문제 풀이 반복하기"],
    "🎨 ISTP 🎨": ["실습 위주 도구 사용", "짧은 동영상 강의 시청하기"],
    "🌊 ISFP 🌊": ["시각 자료 활용 학습", "프로젝트 기반 체험 학습하기"],
    "⚡ ESTP ⚡": ["실전 시뮬레이션 참여", "그룹 활동으로 아이디어 교환"],
    "🌈 ESFP 🌈": ["롤플레이 학습", "즉흥 발표 연습"],
    "🌻 ESFJ 🌻": ["토론 모임 참여", "피어 티칭 해보기"],
    "🚀 ENFJ 🚀": ["멘토링 프로그램 참여", "발표 연습과 피드백 받기"],
    "💡 ENTP 💡": ["디베이트 동아리 참여", "자유로운 브레인스토밍"],
    "🎯 ESTJ 🎯": ["목표 설정과 달성 기록하기", "케이스 스터디 분석"],
    "🔥 ENTJ 🔥": ["전략 게임으로 논리력 강화", "팀 프로젝트 리더 역할 맡기"],
    "🔍 ISFJ 🔍": ["상세 계획표 작성", "반복 학습으로 이해 심화"],
    "✨ ENFP ✨": ["아이디어 스케치하기", "다양한 관점으로 토론하기"],
}

# 잘 맞는 친구 유형
compatible_friends = {
    "✨ INFP ✨": ["🌈 ESFP 🌈", "💡 ENTP 💡"],
    "🌟 INFJ 🌟": ["✨ ENFP ✨", "🔑 ISFJ 🔑"],
    "💎 INTJ 💎": ["💡 ENTP 💡", "❄️ ISTJ ❄️"],
    "🔑 ISFJ 🔑": ["🌟 INFJ 🌟", "🌻 ESFJ 🌻"],
    "❄️ ISTJ ❄️": ["🎯 ESTJ 🎯", "💎 INTJ 💎"],
    "🎨 ISTP 🎨": ["⚡ ESTP ⚡", "💡 ENTP 💡"],
    "🌊 ISFP 🌊": ["✨ INFP ✨", "🌈 ESFP 🌈"],
    "⚡ ESTP ⚡": ["🎨 ISTP 🎨", "🌻 ESFJ 🌻"],
    "🌈 ESFP 🌈": ["✨ INFP ✨", "🌊 ISFP 🌊"],
    "🌻 ESFJ 🌻": ["🔑 ISFJ 🔑", "🚀 ENFJ 🚀"],
    "🚀 ENFJ 🚀": ["🌻 ESFJ 🌻", "💡 ENTP 💡"],
    "💡 ENTP 💡": ["✨ INFP ✨", "💎 INTJ 💎"],
    "🎯 ESTJ 🎯": ["❄️ ISTJ ❄️", "🔥 ENTJ 🔥"],
    "🔥 ENTJ 🔥": ["🎯 ESTJ 🎯", "💡 ENTP 💡"],
    "🔍 ISFJ 🔍": ["🌟 INFJ 🌟", "🌻 ESFJ 🌻"],
    "✨ ENFP ✨": ["🌟 INFJ 🌟", "🎨 ISTP 🎨"],
}

# 강점
strengths = {
    "✨ INFP ✨": "높은 공감 능력과 창의성",
    "🌟 INFJ 🌟": "깊은 통찰력과 비전 제시",
    "💎 INTJ 💎": "전략적 사고와 분석력",
    "🔑 ISFJ 🔑": "책임감과 세심함",
    "❄️ ISTJ ❄️": "신뢰성과 조직력",
    "🎨 ISTP 🎨": "문제 해결 능력과 실용성",
    "🌊 ISFP 🌊": "예술적 감수성과 융통성",
    "⚡ ESTP ⚡": "적응력과 에너지",
    "🌈 ESFP 🌈": "사교성과 즉흥성",
    "🌻 ESFJ 🌻": "사람 중심적 리더십",
    "🚀 ENFJ 🚀": "영향력과 동기부여 능력",
    "💡 ENTP 💡": "창의적 아이디어와 토론력",
    "🎯 ESTJ 🎯": "결단력과 실행력",
    "🔥 ENTJ 🔥": "리더십과 목표 지향성",
    "🔍 ISFJ 🔍": "충실함과 지원 능력",
    "✨ ENFP ✨": "열정과 호기심",
}

# 신경 써야 할 점
weaknesses = {
    "✨ INFP ✨": "우유부단함과 과도한 이상주의",
    "🌟 INFJ 🌟": "과도한 부담감과 자기희생",
    "💎 INTJ 💎": "감정 표현 부족과 완벽주의",
    "🔑 ISFJ 🔑": "변화 저항과 자기 주장 어려움",
    "❄️ ISTJ ❄️": "융통성 부족과 고집",
    "🎨 ISTP 🎨": "장기 계획 미흡과 감정 소홀",
    "🌊 ISFP 🌊": "계획성 부족과 충동성",
    "⚡ ESTP ⚡": "장기 목표 집중 어려움과 충동적 발언",
    "🌈 ESFP 🌈": "집중력 부족과 지나친 사교성",
    "🌻 ESFJ 🌻": "비판에 민감하고 과도한 통제욕",
    "🚀 ENFJ 🚀": "타인 기대 과다와 자기 돌봄 소홀",
    "💡 ENTP 💡": "산만함과 꾸준함 부족",
    "🎯 ESTJ 🎯": "권위적 태도와 융통성 부족",
    "🔥 ENTJ 🔥": "과도한 경쟁심과 타인 고려 부족",
    "🔍 ISFJ 🔍": "자기 돌봄 소홀과 과도한 부담",
    "✨ ENFP ✨": "집중력 분산과 감정 기복",
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
