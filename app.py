import streamlit as st
import pandas as pd
from datetime import date
from pathlib import Path

st.set_page_config(
    page_title="GoldenNest Care",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
:root {
    --gold: #C9A227;
    --gold-light: #E7C766;
    --gold-soft: #FFF6DD;
    --blue: #1F4E79;
    --blue-dark: #163956;
    --blue-soft: #EAF2FB;
    --bg: #F8FAFD;
    --card: #FFFFFF;
    --text: #243447;
    --muted: #5B6B7A;
    --border: #E3EAF3;
    --success-bg: #ECF9F1;
    --success-border: #2F9E5B;
    --warn-bg: #FFF6E8;
    --warn-border: #D9921A;
    --danger-bg: #FDECEC;
    --danger-border: #D64545;
}

html, body, [class*="css"] {
    font-family: "Segoe UI", sans-serif;
}

.stApp {
    background: linear-gradient(180deg, #FFFCF4 0%, #F6F9FD 100%);
    color: var(--text);
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, var(--blue) 0%, var(--blue-dark) 100%);
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stDateInput label {
    color: #F4F7FB !important;
    font-weight: 600;
}

.main-title-card {
    background: linear-gradient(135deg, #FFF7E3 0%, #EEF5FD 100%);
    border: 1px solid #E7D7A4;
    border-radius: 24px;
    padding: 24px 28px;
    margin-bottom: 22px;
    box-shadow: 0 12px 30px rgba(31, 78, 121, 0.08);
}

.brand-row {
    display: flex;
    align-items: center;
    gap: 18px;
}

.logo-circle {
    width: 78px;
    height: 78px;
    min-width: 78px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 30px;
    font-weight: 800;
    box-shadow: 0 10px 24px rgba(201, 162, 39, 0.28);
}

.brand-title {
    font-size: 40px;
    font-weight: 800;
    color: #8A6A12;
    line-height: 1.05;
    margin: 0;
}

.brand-subtitle {
    font-size: 21px;
    font-weight: 700;
    color: var(--blue);
    margin-top: 4px;
    margin-bottom: 6px;
}

.brand-text {
    font-size: 15px;
    color: var(--muted);
    margin: 0;
    line-height: 1.6;
}

.section-shell {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 18px 18px 16px 18px;
    margin-bottom: 18px;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.05);
}

.profile-box {
    background: linear-gradient(180deg, #FFFFFF 0%, #FBFCFE 100%);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 16px;
    box-shadow: 0 8px 20px rgba(15, 23, 42, 0.04);
}

.mini-note {
    background: linear-gradient(135deg, #FFF9E8 0%, #F7FBFF 100%);
    border-left: 6px solid var(--gold);
    border-radius: 14px;
    padding: 14px 16px;
    color: var(--muted);
    margin-top: 8px;
}

.status-good {
    background: var(--success-bg);
    border-left: 6px solid var(--success-border);
    border-radius: 14px;
    padding: 14px 16px;
    color: #20613A;
    font-weight: 700;
    margin-top: 10px;
}

.status-watch {
    background: var(--warn-bg);
    border-left: 6px solid var(--warn-border);
    border-radius: 14px;
    padding: 14px 16px;
    color: #8B5A08;
    font-weight: 700;
    margin-top: 10px;
}

.status-alert {
    background: var(--danger-bg);
    border-left: 6px solid var(--danger-border);
    border-radius: 14px;
    padding: 14px 16px;
    color: #8A2323;
    font-weight: 700;
    margin-top: 10px;
}

.founder-card {
    background: linear-gradient(135deg, #FFFFFF 0%, #F8FBFF 100%);
    border: 1px solid #DDE7F2;
    border-radius: 20px;
    padding: 22px;
    box-shadow: 0 10px 26px rgba(31, 78, 121, 0.08);
}

.photo-placeholder {
    background: linear-gradient(180deg, #FFF7E6 0%, #F2F7FD 100%);
    border: 1px solid #E4EAF3;
    border-radius: 18px;
    text-align: center;
    padding: 28px 10px;
    color: var(--blue);
}

div.stButton > button {
    background: linear-gradient(135deg, var(--blue) 0%, #2C689B 100%);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.62rem 1rem;
    font-weight: 700;
}

div.stDownloadButton > button {
    background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.62rem 1rem;
    font-weight: 800;
}

div[data-testid="stMetric"] {
    background: linear-gradient(180deg, #FFFFFF 0%, #FBFCFE 100%);
    border: 1px solid var(--border);
    padding: 10px 12px;
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(15, 23, 42, 0.04);
}

h2, h3 {
    color: var(--blue);
}

.block-label {
    font-size: 14px;
    font-weight: 700;
    color: var(--blue);
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="brand-row">
    <img src="GoldenNest-Care-logo-design.jpeg" alt="GoldenNest Care Logo" style="width:140px; height:auto; border-radius:16px;">
    <div>
        <div class="brand-title">GoldenNest Care</div>
        <div class="brand-subtitle">Smarter Daily Care for Seniors</div>
        <div class="brand-text">
            A multi-facility senior care coordination platform for wellness tracking, caregiver support,
            medication support documentation, and daily reporting.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("## GoldenNest Care")
st.sidebar.write("Luxury-style senior care workflow dashboard for daily coordination, documentation, and reporting.")

facilities = {
    "GoldenNest Oakland": {
        "caregivers": ["Alice Tan", "Michael Lee", "Sarah Johnson", "Brenda Scott"],
        "residents": {
            "Mary Johnson": {
                "Age": 82,
                "DOB": "03/14/1943",
                "Room": "A-12",
                "Emergency Contact": "Linda Johnson - Daughter - (510) 555-0182",
                "Primary Condition": "Dehydration risk, arthritis",
                "Mobility Status": "Assisted walking",
                "Cognitive Status": "Alert, occasional forgetfulness",
                "Medication Support": "Blood pressure medication reminder at 8:00 AM and 8:00 PM",
                "Allergies": "Penicillin",
                "Wellness Priorities": "Hydration reminders, daily walk support, mood check"
            },
            "Robert Lee": {
                "Age": 87,
                "DOB": "09/21/1938",
                "Room": "B-07",
                "Emergency Contact": "James Lee - Son - (415) 555-0144",
                "Primary Condition": "Diabetes support needs, fall risk",
                "Mobility Status": "Walker assistance",
                "Cognitive Status": "Alert and oriented",
                "Medication Support": "Meal-related medication reminder and wellness follow-up",
                "Allergies": "None reported",
                "Wellness Priorities": "Meal monitoring, mobility support, evening wellness check"
            },
            "Helen Morris": {
                "Age": 89,
                "DOB": "12/02/1936",
                "Room": "A-08",
                "Emergency Contact": "Karen Morris - Daughter - (510) 555-0191",
                "Primary Condition": "Mild dementia, sleep disturbance",
                "Mobility Status": "Supervised walking",
                "Cognitive Status": "Memory support needed",
                "Medication Support": "Evening medication reminder",
                "Allergies": "None reported",
                "Wellness Priorities": "Orientation prompts, safety checks, bedtime monitoring"
            },
            "Samuel Green": {
                "Age": 78,
                "DOB": "08/11/1947",
                "Room": "B-02",
                "Emergency Contact": "Marcus Green - Son - (510) 555-0125",
                "Primary Condition": "Hypertension, low appetite",
                "Mobility Status": "Independent",
                "Cognitive Status": "Alert",
                "Medication Support": "Morning medication reminder",
                "Allergies": "Aspirin",
                "Wellness Priorities": "Meal encouragement, hydration, blood pressure routine reminder"
            }
        }
    },
    "GoldenNest San Leandro": {
        "caregivers": ["Emily Garcia", "David Kim", "Nina Patel", "Lauren Diaz"],
        "residents": {
            "Sofia Martinez": {
                "Age": 79,
                "DOB": "11/05/1946",
                "Room": "C-03",
                "Emergency Contact": "Elena Martinez - Niece - (650) 555-0198",
                "Primary Condition": "Early-stage dementia",
                "Mobility Status": "Independent with supervision",
                "Cognitive Status": "Memory support needed",
                "Medication Support": "Daily medication reminder at 9:00 AM",
                "Allergies": "Sulfa drugs",
                "Wellness Priorities": "Orientation prompts, hydration, emotional reassurance"
            },
            "George Patel": {
                "Age": 84,
                "DOB": "06/19/1941",
                "Room": "C-07",
                "Emergency Contact": "Priya Patel - Daughter - (510) 555-0159",
                "Primary Condition": "Fall risk, hypertension",
                "Mobility Status": "Walker support",
                "Cognitive Status": "Alert",
                "Medication Support": "Morning and evening medication reminder",
                "Allergies": "None reported",
                "Wellness Priorities": "Mobility support, hydration, safety monitoring"
            },
            "Lillian Brooks": {
                "Age": 86,
                "DOB": "04/22/1940",
                "Room": "C-09",
                "Emergency Contact": "Jason Brooks - Son - (510) 555-0117",
                "Primary Condition": "Moderate dementia",
                "Mobility Status": "Assisted walking",
                "Cognitive Status": "Frequent memory redirection needed",
                "Medication Support": "Medication reminder with supervision",
                "Allergies": "None reported",
                "Wellness Priorities": "Redirection, hydration, family communication"
            }
        }
    },
    "GoldenNest Fremont": {
        "caregivers": ["Kevin Brown", "Olivia Chen", "Grace Lopez", "Monica Rivera"],
        "residents": {
            "Helen Wong": {
                "Age": 90,
                "DOB": "01/08/1936",
                "Room": "D-02",
                "Emergency Contact": "Jason Wong - Son - (408) 555-0112",
                "Primary Condition": "Limited mobility, pressure sore risk",
                "Mobility Status": "Wheelchair assistance",
                "Cognitive Status": "Alert, mild memory decline",
                "Medication Support": "Pain medication reminder and evening care follow-up",
                "Allergies": "Aspirin",
                "Wellness Priorities": "Repositioning support, hydration, comfort care"
            },
            "Anna Cruz": {
                "Age": 81,
                "DOB": "07/30/1944",
                "Room": "D-05",
                "Emergency Contact": "Maria Cruz - Daughter - (925) 555-0166",
                "Primary Condition": "Post-hospital recovery support",
                "Mobility Status": "Supervised walking",
                "Cognitive Status": "Alert and oriented",
                "Medication Support": "Medication reminder after meals",
                "Allergies": "None reported",
                "Wellness Priorities": "Meal support, walking, rest monitoring"
            },
            "Peter Young": {
                "Age": 88,
                "DOB": "05/15/1938",
                "Room": "D-10",
                "Emergency Contact": "Angela Young - Daughter - (408) 555-0173",
                "Primary Condition": "Mild cognitive impairment",
                "Mobility Status": "Walker support",
                "Cognitive Status": "Occasional confusion",
                "Medication Support": "Noon medication reminder",
                "Allergies": "Latex",
                "Wellness Priorities": "Routine cues, hydration, social interaction"
            },
            "Rosa Delgado": {
                "Age": 85,
                "DOB": "10/01/1941",
                "Room": "D-12",
                "Emergency Contact": "Carlos Delgado - Son - (408) 555-0184",
                "Primary Condition": "Advanced dementia support needs",
                "Mobility Status": "Full assistance",
                "Cognitive Status": "High supervision needed",
                "Medication Support": "Scheduled support reminders with documentation",
                "Allergies": "None reported",
                "Wellness Priorities": "Safety monitoring, comfort care, continence care"
            }
        }
    }
}

st.markdown('<div class="section-shell">', unsafe_allow_html=True)
colf1, colf2, colf3 = st.columns(3)
with colf1:
    selected_date = st.date_input("Care Date", value=date.today())
with colf2:
    selected_facility = st.selectbox("Select Facility", list(facilities.keys()))
with colf3:
    facility_data = facilities[selected_facility]
    selected_resident = st.selectbox("Select Resident", list(facility_data["residents"].keys()))
assigned_caregiver = st.selectbox("Assigned Caregiver", facility_data["caregivers"])
st.markdown('</div>', unsafe_allow_html=True)

profile = facility_data["residents"][selected_resident]

st.markdown('<div class="section-shell">', unsafe_allow_html=True)
st.markdown("## Resident Profile")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="profile-box">', unsafe_allow_html=True)
    st.markdown(f"""
**Name:** {selected_resident}  
**Age:** {profile['Age']}  
**DOB:** {profile['DOB']}  
**Room:** {profile['Room']}  
**Emergency Contact:** {profile['Emergency Contact']}
""")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="profile-box">', unsafe_allow_html=True)
    st.markdown(f"""
**Primary Condition:** {profile['Primary Condition']}  
**Mobility Status:** {profile['Mobility Status']}  
**Cognitive Status:** {profile['Cognitive Status']}  
**Medication Support:** {profile['Medication Support']}  
**Allergies:** {profile['Allergies']}
""")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="mini-note">
<b>Wellness Priorities:</b> {profile["Wellness Priorities"]}
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-shell">', unsafe_allow_html=True)
st.markdown("## 💊 Medication Support List")
st.caption("Caregivers can add, review, or update multiple medication support entries for a resident.")

if "med_rows" not in st.session_state:
    st.session_state.med_rows = 3

col_a, col_b = st.columns([1, 1])
with col_a:
    if st.button("➕ Add Medication Row"):
        st.session_state.med_rows += 1
with col_b:
    if st.button("➖ Remove Medication Row") and st.session_state.med_rows > 1:
        st.session_state.med_rows -= 1

default_rows = st.session_state.get("med_table_data")
if default_rows is None or len(default_rows) != st.session_state.med_rows:
    medication_df = pd.DataFrame(
        {
            "Medication Name": [""] * st.session_state.med_rows,
            "Strength": [""] * st.session_state.med_rows,
            "Schedule": [""] * st.session_state.med_rows,
            "Instructions": [""] * st.session_state.med_rows,
            "Physician Reference": [""] * st.session_state.med_rows
        }
    )
else:
    medication_df = pd.DataFrame(default_rows)

edited_medications = st.data_editor(
    medication_df,
    num_rows="dynamic",
    use_container_width=True,
    key="med_table"
)
st.session_state.med_table_data = edited_medications.to_dict(orient="records")
st.markdown('</div>', unsafe_allow_html=True)

morning_tasks = [
    "Wake up / morning check-in",
    "Morning hydration",
    "Wellness observation / health check reminder",
    "Insulin reminder / confirm skilled support if required",
    "Morning medication reminder",
    "Personal hygiene (toileting, brushing teeth, washing face)",
    "Diaper change / continence care",
    "Breakfast"
]

day_tasks = [
    "Light exercise / mobility (walk, stretching)",
    "Morning mood check",
    "Repositioning / comfort support",
    "Hydration reminder",
    "Lunch",
    "Afternoon medication reminder",
    "Diaper change / continence care (afternoon)",
    "Rest / nap"
]

engagement_tasks = [
    "Cognitive activities (reading, games, conversation)",
    "Social interaction / family time",
    "Afternoon mood check",
    "Follow-up wellness observation if needed"
]

evening_tasks = [
    "Evening hydration",
    "Dinner",
    "Evening medication reminder",
    "Light activity / relaxation",
    "Personal hygiene (evening care)",
    "Diaper change / continence care (evening)"
]

night_tasks = [
    "Bedtime preparation",
    "Bedtime medication reminder",
    "Final toileting",
    "Sleep monitoring / safety check"
]

status_options = ["Complete", "Missed", "Delayed", "Not Needed Today"]
results = {}

def render_task_section(title, task_list, key_prefix):
    st.markdown('<div class="section-shell">', unsafe_allow_html=True)
    st.markdown(f"## {title}")
    for i, task in enumerate(task_list):
        results[task] = st.selectbox(task, status_options, key=f"{key_prefix}_{i}")
    st.markdown('</div>', unsafe_allow_html=True)

render_task_section("Morning Routine", morning_tasks, "morning")
render_task_section("Daytime Activities", day_tasks, "day")
render_task_section("Engagement & Monitoring", engagement_tasks, "engage")
render_task_section("Evening Routine", evening_tasks, "evening")
render_task_section("Night Routine", night_tasks, "night")

df = pd.DataFrame(list(results.items()), columns=["Task", "Status"])

st.markdown('<div class="section-shell">', unsafe_allow_html=True)
st.markdown("## Daily Status")
st.dataframe(df, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

complete_count = (df["Status"] == "Complete").sum()
missed_count = (df["Status"] == "Missed").sum()
delayed_count = (df["Status"] == "Delayed").sum()
not_needed_count = (df["Status"] == "Not Needed Today").sum()

st.markdown('<div class="section-shell">', unsafe_allow_html=True)
st.markdown("## Summary")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Completed", int(complete_count), border=True)
c2.metric("Missed", int(missed_count), border=True)
c3.metric("Delayed", int(delayed_count), border=True)
c4.metric("Not Needed", int(not_needed_count), border=True)

caregiver_notes = st.text_area(
    "Caregiver Notes",
    placeholder="Enter appetite notes, hydration concerns, behavioral observations, sleep notes, mobility concerns, or family communication notes..."
)

if missed_count >= 3:
    st.markdown('<div class="status-alert">High attention needed: several daily care tasks were missed.</div>', unsafe_allow_html=True)
elif missed_count >= 1 or delayed_count >= 3:
    st.markdown('<div class="status-watch">Follow-up recommended: review incomplete or delayed tasks.</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="status-good">Daily care activities are on track.</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

if missed_count >= 3:
    risk_level = "High"
elif missed_count >= 1 or delayed_count >= 3:
    risk_level = "Moderate"
else:
    risk_level = "Low"

medications_for_report = edited_medications.fillna("").to_dict(orient="records")
formatted_meds = []
for i, med in enumerate(medications_for_report, start=1):
    if any(str(v).strip() for v in med.values()):
        formatted_meds.append(
            f"{i}. Name: {med['Medication Name'] or 'Not entered'} | "
            f"Strength: {med['Strength'] or 'Not entered'} | "
            f"Schedule: {med['Schedule'] or 'Not entered'} | "
            f"Instructions: {med['Instructions'] or 'Not entered'} | "
            f"Physician Ref: {med['Physician Reference'] or 'Not entered'}"
        )

med_report_text = "\n".join(formatted_meds) if formatted_meds else "No medication entries recorded."

report_text = f"""
Facility: {selected_facility}
Date: {selected_date}
Resident: {selected_resident}
Assigned Caregiver: {assigned_caregiver}
Risk Level: {risk_level}

Completed Tasks: {complete_count}
Missed Tasks: {missed_count}
Delayed Tasks: {delayed_count}
Not Needed Today: {not_needed_count}

Medication Support List:
{med_report_text}

Caregiver Notes:
{caregiver_notes if caregiver_notes else "No caregiver notes entered."}
"""

st.markdown('<div class="section-shell">', unsafe_allow_html=True)
st.markdown("## Daily Report")
st.text_area("Generated Daily Report", value=report_text, height=330)
st.download_button(
    label="Download Daily Report",
    data=report_text,
    file_name=f"{selected_resident.lower().replace(' ', '_')}_daily_report.txt",
    mime="text/plain"
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-shell">', unsafe_allow_html=True)
st.markdown("## Founder")
founder_col1, founder_col2 = st.columns([1, 3])

with founder_col1:
    image_path = Path(__file__).parent / "founder.jpeg"
    if image_path.exists():
        st.image(str(image_path), width=220)
    else:
        st.markdown("""
        <div class="photo-placeholder">
            <div style="font-size:48px;">👩‍💼</div>
            <div style="font-weight:800; margin-top:8px;">Founder Photo</div>
            <div style="font-size:14px; color:#5B6B7A; margin-top:6px;">
                Add founder.jpg to your project folder
            </div>
        </div>
        """, unsafe_allow_html=True)

with founder_col2:
    st.markdown("""
        <div class="founder-card">
            <h3 style="margin-top:0; color:#8A6A12;">THAZIN MYA LWIN</h3>
            <p style="font-size:18px; font-weight:700; color:#1F4E79; margin-bottom:8px;">
                Founder of GoldenNest Care
            </p>
            <p style="font-size:15px; color:#4B5D70; line-height:1.75;">
                MBA candidate building a smarter daily care coordination platform for senior care homes.
                GoldenNest Care is designed to improve daily wellness tracking, caregiver coordination,
                reporting, and operational visibility across senior living facilities.
            </p>
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
