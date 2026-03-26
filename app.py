import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="GoldenNest Care", layout="wide")

st.markdown("""
    <style>
    .banner {
        background: linear-gradient(90deg, #FFF7E6 0%, #EAF2F8 100%);
        padding: 20px 25px;
        border-radius: 16px;
        margin-bottom: 20px;
        border: 1px solid #E0D3A8;
    }
    .banner-title {
        font-size: 40px;
        font-weight: 700;
        color: #8B6F1E;
        margin-bottom: 5px;
    }
    .banner-subtitle {
        font-size: 24px;
        font-weight: 600;
        color: #1F3B5B;
        margin-bottom: 8px;
    }
    .banner-text {
        font-size: 16px;
        color: #4B5563;
    }
    .founder-card {
        background-color: #F9FAFB;
        border: 1px solid #D9E2EC;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="banner">
        <div class="banner-title">GoldenNest Care</div>
        <div class="banner-subtitle">Smarter Daily Care for Seniors</div>
        <div class="banner-text">
            A multi-facility senior care coordination platform for wellness tracking,
            caregiver support, medication support documentation, and daily reporting.
        </div>
    </div>
""", unsafe_allow_html=True)

st.sidebar.header("GoldenNest Care")
st.sidebar.write("Senior care workflow prototype for daily wellness planning, caregiver coordination, and reporting.")

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

selected_date = st.date_input("Care Date", value=date.today())
selected_facility = st.selectbox("Select Facility", list(facilities.keys()))
facility_data = facilities[selected_facility]

selected_resident = st.selectbox("Select Resident", list(facility_data["residents"].keys()))
profile = facility_data["residents"][selected_resident]
assigned_caregiver = st.selectbox("Assigned Caregiver", facility_data["caregivers"])

st.markdown("## Resident Profile")

col1, col2 = st.columns(2)

with col1:
    st.info(f"""
**Name:** {selected_resident}  
**Age:** {profile['Age']}  
**DOB:** {profile['DOB']}  
**Room:** {profile['Room']}  
**Emergency Contact:** {profile['Emergency Contact']}
""")

with col2:
    st.info(f"""
**Primary Condition:** {profile['Primary Condition']}  
**Mobility Status:** {profile['Mobility Status']}  
**Cognitive Status:** {profile['Cognitive Status']}  
**Medication Support:** {profile['Medication Support']}  
**Allergies:** {profile['Allergies']}
""")

st.markdown("### Wellness Priorities")
st.write(profile["Wellness Priorities"])

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

medication_df = pd.DataFrame(
    {
        "Medication Name": [""] * st.session_state.med_rows,
        "Strength": [""] * st.session_state.med_rows,
        "Schedule": [""] * st.session_state.med_rows,
        "Instructions": [""] * st.session_state.med_rows,
        "Physician Reference": [""] * st.session_state.med_rows
    }
)

edited_medications = st.data_editor(
    medication_df,
    num_rows="dynamic",
    use_container_width=True,
    key="med_table"
)

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

def render_task_section(title, task_list):
    st.markdown(f"## {title}")
    for task in task_list:
        results[task] = st.selectbox(task, status_options, key=task)

render_task_section("Morning Routine", morning_tasks)
render_task_section("Daytime Activities", day_tasks)
render_task_section("Engagement & Monitoring", engagement_tasks)
render_task_section("Evening Routine", evening_tasks)
render_task_section("Night Routine", night_tasks)

df = pd.DataFrame(list(results.items()), columns=["Task", "Status"])

st.markdown("## Daily Status")
st.dataframe(df, width="stretch")

complete_count = (df["Status"] == "Complete").sum()
missed_count = (df["Status"] == "Missed").sum()
delayed_count = (df["Status"] == "Delayed").sum()
not_needed_count = (df["Status"] == "Not Needed Today").sum()

st.markdown("## Summary")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Completed", int(complete_count))
c2.metric("Missed", int(missed_count))
c3.metric("Delayed", int(delayed_count))
c4.metric("Not Needed", int(not_needed_count))

caregiver_notes = st.text_area(
    "Caregiver Notes",
    placeholder="Enter appetite notes, hydration concerns, behavioral observations, sleep notes, mobility concerns, or family communication notes..."
)

if missed_count >= 3:
    st.error("High attention needed: several daily care tasks were missed.")
elif missed_count >= 1 or delayed_count >= 3:
    st.warning("Follow-up recommended: review incomplete or delayed tasks.")
else:
    st.success("Daily care activities are on track.")

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

st.markdown("## Daily Report")

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

st.text_area("Generated Daily Report", value=report_text, height=350)

st.download_button(
    label="Download Daily Report",
    data=report_text,
    file_name=f"{selected_resident.lower().replace(' ', '_')}_daily_report.txt",
    mime="text/plain"
)

st.markdown("## Founder")
founder_col1, founder_col2 = st.columns([1, 3])

with founder_col1:
    st.image("founder.jpg", width=220)

with founder_col2:
    st.markdown("""
        <div class="founder-card">
            <h3 style="margin-top:0; color:#8B6F1E;">THAZIN MYA LWIN</h3>
            <p style="font-size:18px; font-weight:600; color:#1F3B5B; margin-bottom:8px;">
                Founder of GoldenNest Care
            </p>
            <p style="font-size:15px; color:#4B5563; line-height:1.6;">
                MBA candidate building a smarter daily care coordination platform for senior care homes.
                GoldenNest Care is designed to improve daily wellness tracking, caregiver coordination,
                reporting, and operational visibility across senior living facilities.
            </p>
        </div>
    """, unsafe_allow_html=True)
