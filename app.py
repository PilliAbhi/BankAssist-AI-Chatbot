import streamlit as st
from chatbot.knowledge import get_related_options, get_subtopic_options, search_answer
import time

st.set_page_config(
    page_title="BankAssist AI",
    page_icon="🏦",
    layout="wide"
)

# ================= Sidebar =================

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2830/2830284.png",
        width=90
    )

    st.title("🏦 BankAssist AI")

    st.markdown("---")

    st.markdown("## 📌 Banking Services")

    services = [
        "Account Opening",
        "Minimum Balance",
        "ATM Card",
        "Passbook",
        "Net Banking",
        "Mobile Banking",
        "Credit Card",
        "Home Loan",
        "Education Loan",
        "Personal Loan",
        "Vehicle Loan",
        "Gold Loan",
        "UPI",
        "KYC",
        "Fixed Deposit"
    ]

    for service in services:
        st.markdown(f"✅ {service}")

# ================= Main =================

st.title("🏦 BankAssist AI")
st.write("Select a banking topic below.")

topics = [
    "Select a Topic",
    "Account Opening",
    "Minimum Balance",
    "ATM Card",
    "Passbook",
    "Net Banking",
    "Mobile Banking",
    "Credit Card",
    "Home Loan",
    "Education Loan",
    "Personal Loan",
    "Vehicle Loan",
    "Gold Loan",
    "UPI",
    "KYC",
    "Fixed Deposit"
]

selected = st.selectbox(
    "Choose a Banking Service",
    topics
)

if selected != "Select a Topic":
    subtopic_options = get_subtopic_options(selected)
    selected_subtopic = None

    if subtopic_options:
        subtopic_labels = [option["label"] for option in subtopic_options]
        selected_subtopic_label = st.selectbox(
            "Choose a product option",
            subtopic_labels
        )
        selected_subtopic = next(
            option["id"] for option in subtopic_options if option["label"] == selected_subtopic_label
        )
        result = search_answer(selected, selected_subtopic)
    else:
        related_options = get_related_options(selected)
        option_labels = [option["label"] for option in related_options]
        selected_option = st.selectbox(
            "What do you need help with?",
            option_labels
        )
        option_id = next(option["id"] for option in related_options if option["label"] == selected_option)
        result = search_answer(selected, option_id)
        selected_subtopic = selected_option

    if result:

        with st.spinner("Loading..."):
            time.sleep(0.5)

        st.subheader(result["title"])
        st.caption(
            f"Customer help flow: {selected} > {selected_subtopic if selected_subtopic else 'Overview'}"
        )
        st.write("")

        for paragraph in result["answer"]:
            st.markdown(f"<p style='font-size: 1.1rem; line-height: 1.8; margin-bottom: 1rem;'>{paragraph}</p>", unsafe_allow_html=True)

        st.write("")

    else:

        st.error("No information available in the Knowledge Base.")