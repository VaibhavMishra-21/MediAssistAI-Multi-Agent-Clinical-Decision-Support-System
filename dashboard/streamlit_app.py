import streamlit as st

from workflows.diagnosis_workflow import (
    run_medical_workflow
)

st.set_page_config(
    page_title="MediAssistAI",
    layout="wide"
)

st.title(
    "🏥 MediAssistAI"
)

st.markdown(
    """
    Educational medical analysis platform.

    Not intended for diagnosis.
    """
)

symptoms = st.text_area(
    "Patient Symptoms"
)

if st.button(
    "Analyze"
):

    with st.spinner(
        "Running specialist agents..."
    ):

        result = run_medical_workflow(
            symptoms
        )

    st.success(
        "Analysis Complete"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "Risk Level"
        )

        st.write(
            result["risk"]
        )

        st.subheader(
            "Symptom Findings"
        )

        st.write(
            result["findings"]
        )

    with col2:

        st.subheader(
            "Generated Report"
        )

        st.write(
            result["final_report"]
        )
