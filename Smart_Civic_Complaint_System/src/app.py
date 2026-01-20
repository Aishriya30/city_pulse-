import streamlit as st
import pandas as pd
import uuid

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Smart Civic Complaint Management System",
    page_icon="🏛️",
    layout="wide"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
.main-title {
    text-align: center;
    color: #1f77b4;
    font-size: 34px;
    font-weight: 700;
}
.subtitle {
    text-align: center;
    font-size: 15px;
    color: #9aa0a6;
    margin-bottom: 25px;
}
.footer {
    text-align: center;
    color: gray;
    font-size: 13px;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.markdown('<div class="main-title">🏛️ Smart Civic Complaint Management System</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Centralized platform for automated civic complaint classification and monitoring</div>',
    unsafe_allow_html=True
)

# ---------------- Session State ----------------
if "complaints" not in st.session_state:
    st.session_state.complaints = []

# ---------------- Complaint Classification Logic ----------------
def classify_complaint(text):
    text = text.lower()

    electricity = ["power", "electricity", "voltage", "current", "transformer", "meter"]
    water = ["water", "leak", "pipeline", "tap", "overflow"]
    sanitation = ["garbage", "waste", "toilet", "drain", "sewage"]
    roads = ["road", "pothole", "traffic", "street", "speed breaker", "signal"]

    if any(w in text for w in electricity):
        return "Electricity Department"
    elif any(w in text for w in water):
        return "Water Supply Department"
    elif any(w in text for w in sanitation):
        return "Sanitation Department"
    elif any(w in text for w in roads):
        return "Roads & Transport Department"
    else:
        return "General Civic Department"

# ---------------- Layout ----------------
left, right = st.columns([1, 1.2])

# ================= LEFT: Citizen Portal =================
with left:
    st.markdown("### 📝 Citizen Complaint Portal")

    address = st.text_input(
        "📍 Address / Location",
        placeholder="Example: Anna Nagar, Chennai"
    )

    complaint = st.text_area(
        "🗒️ Enter your civic issue:",
        placeholder="Example: Garbage not collected near my house"
    )

    if st.button("📤 Submit Complaint", use_container_width=True):
        if complaint.strip() == "" or address.strip() == "":
            st.warning("⚠️ Please enter both address and complaint.")
        else:
            department = classify_complaint(complaint)
            complaint_id = str(uuid.uuid4())[:8]

            st.session_state.complaints.append({
                "Complaint ID": complaint_id,
                "Address": address,
                "Complaint Text": complaint,
                "Department": department,
                "Status": "Assigned"
            })

            st.success("✅ Complaint submitted successfully")
            st.info(
                f"""
**Complaint ID:** {complaint_id}  
**Address:** {address}  
**Assigned Department:** {department}  
**Status:** Assigned  
**Processing:** Automated Classification
"""
            )

# ================= RIGHT: Admin Dashboard =================
with right:
    st.markdown("### 🛠️ Admin Dashboard")

    if st.session_state.complaints:
        df = pd.DataFrame(st.session_state.complaints)

        st.markdown("#### 📋 Complaint History")
        st.dataframe(df, use_container_width=True)

        st.markdown("#### 📊 Department Statistics")
        dept_counts = df["Department"].value_counts()
        st.bar_chart(dept_counts)
    else:
        st.info("No complaints submitted yet.")

# ---------------- Footer ----------------
st.markdown(
    '<div class="footer">© 2025 Smart City Automation Project | Python & Streamlit</div>',
    unsafe_allow_html=True
)
