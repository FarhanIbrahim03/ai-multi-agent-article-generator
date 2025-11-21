import streamlit as st
import requests

FASTAPI_URL = "http://localhost:8000/run"

# ----------- UI CONFIG -----------
st.set_page_config(
    page_title="AI Multi-Agent Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Multi-Agent Article Generator")
st.write("Generate research, analysis, and a polished article using your CrewAI backend.")

topic = st.text_input("🔍 Enter a topic to generate the article:")

if st.button("✨ Generate Article"):
    if not topic:
        st.warning("Please enter a topic!")
    else:
        with st.spinner("Running agents… Please wait ⏳"):
            response = requests.post(FASTAPI_URL, json={"topic": topic})

        if response.status_code == 200:
            data = response.json()
            st.success("🎉 Article generated successfully!")

            # Tabs for cleaner navigation
            tab1, tab2, tab3 = st.tabs(["📄 Final Article", "🧠 Steps Breakdown", "📥 Download"])

            with tab1:
                st.subheader("📄 Final Article")
                st.write(data["final_article"])

            with tab2:
                st.subheader("🧠 Agent Steps Output")
                steps = data.get("steps", {})
                for step, text in steps.items():
                    st.markdown(f"### 🔹 {step.capitalize()}")
                    st.write(text)
                    st.markdown("---")

            with tab3:
                st.subheader("📥 Download Your File")

                if "download_url" in data:
                    DOWNLOAD_BASE = "http://localhost:8000"
                    download_url = DOWNLOAD_BASE + data["download_url"]

                    st.markdown(
                        f"[⬇️ Click here to download the article]({download_url})",
                        unsafe_allow_html=True
                    )

                else:
                    st.warning("No downloadable file found.")

        else:
            st.error("❌ Backend error. Check FastAPI logs.")
