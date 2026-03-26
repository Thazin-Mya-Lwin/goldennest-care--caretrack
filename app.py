import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="GoldenNest Care", layout="wide")

st.markdown("""
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        color: #8B6F1E;
        margin-bottom: 0;
    }
    .sub-title {
        font-size: 24px;
        color: #2C3E50;
        margin-top: 0;
        margin-bottom: 10px;
    }
    .tagline {
        font-size: 18px;
        color: #5D6D7E;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">GoldenNest Care</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Smarter Daily Care for Seniors</p>', unsafe_allow_html=True)
st.markdown('<p class="tagline">A multi-facility senior care coordination platform for wellness tracking, caregiver support, medication support documentation, and daily reporting.</p>', unsafe_allow_html=True)

st.sidebar.header("GoldenNest Care")
st.sidebar.write("Senior care workflow prototype for daily wellness planning, caregiver coordination, and reporting.")

facilities = {
    "GoldenNest Oakland": {
        "caregivers": ["Alice Tan", "Michael Lee", "Sarah Johnson"],
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
            }
        }
    },
    "GoldenNest San Leandro": {
        "caregivers": ["Emily Garcia", "David Kim", "Nina Patel"],
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
            }
        }
    },
    "GoldenNest Fremont": {
        "caregivers": ["Kevin Brown", "Olivia Chen", "Grace Lopez"],
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

st.markdown("## Medication Support Memo")

m1, m2 = st.columns(2)

with m1:
    med_name = st.text_input("Medication Name", placeholder="e.g. Lisinopril")
    med_strength = st.text_input("Strength", placeholder="e.g. 10 mg")
    med_schedule = st.text_input("Schedule", placeholder="e.g. 8:00 AM / 8:00 PM")

with m2:
    med_instruction = st.text_area(
        "Support Instructions",
        placeholder="Reminder, with food, monitor hydration, physician note reference, etc."
    )
    physician_reference = st.text_input(
        "Physician Order Reference",
        placeholder="Optional memo or reference note"
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

Medication Support Memo:
- Medication Name: {med_name if med_name else "Not entered"}
- Strength: {med_strength if med_strength else "Not entered"}
- Schedule: {med_schedule if med_schedule else "Not entered"}
- Support Instructions: {med_instruction if med_instruction else "Not entered"}
- Physician Order Reference: {physician_reference if physician_reference else "Not entered"}

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

st.markdown("## Monetization Idea")

pricing_df = pd.DataFrame({
    "Plan": ["Starter", "Professional", "Enterprise"],
    "Monthly Price": ["$99/facility", "$249/facility", "Custom pricing"],
    "Best For": ["Small care homes", "Growing multi-site operators", "Large operators with custom needs"],
    "Includes": [
        "Resident tracking, daily checklist, caregiver notes",
        "Multi-facility support, daily reports, medication support memo, dashboards",
        "Advanced reporting, integrations, admin controls, training and support"
    ]
})

st.dataframe(pricing_df, width="stretch")

st.markdown("## Founder")
founder_col1, founder_col2 = st.columns([1, 3])

with founder_col1:
    st.image("WhatsApp-Image-2026-02-26-at-11.22.46-PM.jpg", width=180)

with founder_col2:
    st.markdown("### THAZIN MYA LWIN")
    st.write("Founder of GoldenNest Care")
    st.write("MBA candidate building a smarter daily care coordination platform for senior care homes.")
