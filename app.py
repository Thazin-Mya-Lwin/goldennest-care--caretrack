import streamlit as st
import pandas as pd

st.set_page_config(page_title="CareTrack AI", layout="wide")

st.title("CareTrack AI")
st.subheader("Daily Care Planner and Wellness Check Assistant for Senior Care Homes")

st.sidebar.header("CareTrack AI")
st.sidebar.write("Senior care workflow prototype for daily wellness planning and caregiver coordination.")

residents = {
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
    }
}

selected_resident = st.selectbox("Select Resident", list(residents.keys()))
profile = residents[selected_resident]

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

tasks = [
    "Wake up / morning check-in",
    "Morning hydration",
    "Wellness observation / health check reminder",
    "Insulin reminder / confirm skilled support if required",
    "Morning medication reminder",
    "Personal hygiene (toileting, brushing teeth, washing face)",
    "Diaper change / continence care",
    "Breakfast",
    "Light exercise / mobility (walk, stretching)",
    "Morning mood check",
    "Repositioning / comfort support",
    "Hydration reminder",
    "Lunch",
    "Afternoon medication reminder",
    "Diaper change / continence care (afternoon)",
    "Rest / nap",
    "Cognitive activities (reading, games, conversation)",
    "Social interaction / family time",
    "Afternoon mood check",
    "Follow-up wellness observation if needed",
    "Evening hydration",
    "Dinner",
    "Evening medication reminder",
    "Light activity / relaxation",
    "Personal hygiene (evening care)",
    "Diaper change / continence care (evening)",
    "Bedtime preparation",
    "Bedtime medication reminder",
    "Final toileting",
    "Sleep monitoring / safety check"
]

st.markdown("## Daily Wellness Checklist")

status_options = ["Complete", "Missed", "Delayed", "Not Needed Today"]
results = {}

for task in tasks:
    results[task] = st.selectbox(task, status_options, key=task)

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
    placeholder="Enter daily wellness observations, follow-up concerns, appetite notes, sleep notes, or communication notes here..."
)

if missed_count >= 3:
    st.error("High attention needed: several daily care tasks were missed.")
elif missed_count >= 1 or delayed_count >= 3:
    st.warning("Follow-up recommended: review incomplete or delayed tasks.")
else:
    st.success("Daily care activities are on track.")

st.markdown("## Shift Summary")

if missed_count >= 3:
    risk_level = "High"
elif missed_count >= 1 or delayed_count >= 3:
    risk_level = "Moderate"
else:
    risk_level = "Low"

st.write(f"Resident: {selected_resident}")
st.write(f"Risk level: {risk_level}")
st.write(f"Completed tasks: {complete_count}")
st.write(f"Missed tasks: {missed_count}")
st.write(f"Delayed tasks: {delayed_count}")
st.write(f"Tasks marked not needed today: {not_needed_count}")

if caregiver_notes.strip():
    st.write("Caregiver notes recorded.")
else:
    st.write("No caregiver notes entered yet.")
