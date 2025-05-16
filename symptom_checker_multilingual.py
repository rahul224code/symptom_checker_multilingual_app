import streamlit as st

# Show logo
st.image("logo.png", width=120)

# App title
st.markdown("<h1 style='color:#045e84;'>SymptomChecker</h1>", unsafe_allow_html=True)
st.markdown("### An AI-Based Symptom Suggestion App (By You)")

# Language selection
lang = st.selectbox("Select Language / भाषा चुनें / ভাষা বেছে নিন", ["English", "Hindi", "Bengali"])

# Multilingual symptom data
symptoms_dict = {
    "English": {
        "Headache": ("Paracetamol, Ibuprofen", "Rest, drink water, avoid stress."),
        "Cold & Sneezing": ("Cetirizine, Nasal Spray", "Avoid dust, steam inhalation."),
        "Acidity": ("Antacids (Gelusil, Rantac)", "Avoid spicy and oily foods."),
        "Fever": ("Paracetamol", "Stay hydrated and rest."),
        "Cough": ("Cough syrup (Dextromethorphan)", "Avoid cold drinks, steam inhalation."),
        "Allergies": ("Antihistamines (Loratadine)", "Avoid allergens, use air purifiers.")
    },
    "Hindi": {
        "सिरदर्द": ("पैरासिटामोल, आइबुप्रोफेन", "आराम करें, पानी पिएं, तनाव से बचें।"),
        "जुकाम और छींक": ("सेटिरीज़िन, नेज़ल स्प्रे", "धूल से बचें, भाप लें।"),
        "अम्लता": ("ऐंटासिड (जेलसिल, रैनटैक)", "मसालेदार और तली हुई चीज़ों से बचें।"),
        "बुखार": ("पैरासिटामोल", "पानी पिएं और आराम करें।"),
        "खांसी": ("कफ सिरप (डेक्स्ट्रोमेथॉर्फन)", "ठंडे पेय से बचें, भाप लें।"),
        "एलर्जी": ("एंटीहिस्टामाइन (लोरेटाडीन)", "एलर्जेन से बचें, एयर प्यूरीफायर का उपयोग करें।")
    },
    "Bengali": {
        "মাথাব্যথা": ("প্যারাসিটামল, আইবুপ্রোফেন", "বিশ্রাম নিন, জল খান, স্ট্রেস এড়িয়ে চলুন।"),
        "ঠান্ডা ও হাঁচি": ("সেটিরিজিন, নাকের স্প্রে", "ধুলা এড়িয়ে চলুন, ভাপ নিন।"),
        "অম্লতা": ("অ্যান্টাসিড (জেলুসিল, র্যানটাক)", "ঝাল ও ভাজা খাবার এড়িয়ে চলুন।"),
        "জ্বর": ("প্যারাসিটামল", "জল পান করুন এবং বিশ্রাম নিন।"),
        "কাশি": ("কাশির সিরাপ (ডেক্সট্রোমেথরফান)", "ঠান্ডা পানীয় এড়িয়ে চলুন, ভাপ নিন।"),
        "অ্যালার্জি": ("অ্যান্টিহিস্টামিন (লোরাটাডিন)", "অ্যালার্জেন এড়িয়ে চলুন, এয়ার পিউরিফায়ার ব্যবহার করুন।")
    }
}

# Symptom selection
symptoms = list(symptoms_dict[lang].keys())
selected_symptoms = st.multiselect("Select Your Symptoms:", symptoms)

# Output results
if selected_symptoms:
    st.subheader("Suggested Treatments:")
    for symptom in selected_symptoms:
        drugs, advice = symptoms_dict[lang][symptom]
        st.markdown(f"#### {symptom}")
        st.markdown(f"- **Drugs:** {drugs}")
        st.markdown(f"- **Advice:** {advice}")
        st.markdown("---")

st.markdown("<small style='color:gray;'>Disclaimer: For educational use only. Always consult a registered pharmacist or doctor before taking any medication.</small>", unsafe_allow_html=True)
