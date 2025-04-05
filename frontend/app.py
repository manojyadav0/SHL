import streamlit as st
import requests

st.title("SHL Assessment Recommender")

query = st.text_area("Enter job description or requirement text")

if st.button("Get Recommendations"):
    response = requests.post(
        "http://localhost:8000/recommend", json={"query": query}
    )
    data = response.json()["recommendations"]

    for i, item in enumerate(data, 1):
        st.markdown(f"### {i}. [{item['name']}]({item['url']})")
        st.write(f"**Type:** {item['test_type']}")
        st.write(f"**Duration:** {item['duration']}")
        st.write(f"**Remote Testing:** {item['remote_support']}")
        st.write(f"**Adaptive/IRT Support:** {item['adaptive_support']}")
        st.write(item["description"])
        st.markdown("---")
