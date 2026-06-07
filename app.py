import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("AI 기반 해수 탄소 포집 최적 pH 예측 시스템")

st.write("""
해수의 pH에 따른 탄산종 분포와 탄소 저장 효율,
공정 비용을 분석하여 최적의 탄소 포집 조건을 탐색합니다.
""")

# 데이터

data = {
    "pH":[6,7,8,8.1,8.2,9,10],

    "CO2":[83,33,1,0.8,0.5,0.1,0],

    "HCO3":[17,67,91,91,88,50,9],

    "CO3":[0,0,8,8.2,11.5,49.9,91],

    "효율":[17,67,99,99.2,99.5,99.9,100],

    "비용":[10,15,25,28,32,60,100]
}

df = pd.DataFrame(data)

# 사용자 입력

selected_pH = st.selectbox(
    "해수 pH 선택",
    df["pH"]
)

# 선택된 데이터

row = df[df["pH"] == selected_pH].iloc[0]

efficiency = row["효율"]
cost = row["비용"]

score = efficiency - 0.5 * cost

st.subheader("분석 결과")

st.metric(
    "탄소 저장 효율",
    f"{efficiency:.1f}%"
)

st.metric(
    "공정 비용 지수",
    f"{cost:.1f}"
)

st.metric(
    "최적화 점수",
    f"{score:.1f}"
)

# 탄산종 설명

st.subheader("탄산종 분포")

st.write(
    f"CO₂ : {row['CO2']} %"
)

st.write(
    f"HCO₃⁻ : {row['HCO3']} %"
)

st.write(
    f"CO₃²⁻ : {row['CO3']} %"
)

# 추천

if 8 <= selected_pH <= 8.2:

    st.success(
        "효율과 비용을 동시에 고려했을 때 가장 적절한 운전 조건입니다."
    )

elif selected_pH >= 9:

    st.warning(
        "탄소 저장 효율은 높지만 비용 증가 및 스케일링 문제가 발생할 수 있습니다."
    )

else:

    st.warning(
        "탄소 저장 효율이 낮은 구간입니다."
    )

# 그래프

st.subheader("pH에 따른 탄산종 분포")

plt.figure(figsize=(8,4))

plt.plot(
    df["pH"],
    df["CO2"],
    marker="o",
    label="CO2"
)

plt.plot(
    df["pH"],
    df["HCO3"],
    marker="o",
    label="HCO3-"
)

plt.plot(
    df["pH"],
    df["CO3"],
    marker="o",
    label="CO3^2-"
)

plt.xlabel("pH")
plt.ylabel("비율 (%)")
plt.legend()

st.pyplot(plt)

# 데이터 표

st.subheader("학습 데이터")

st.dataframe(df)