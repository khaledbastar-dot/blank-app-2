import streamlit as st

st.title("🌟 آزمون علوم 🌟")
st.write("این آزمون شامل ۳ سوال است: یک سوال تشریحی، یک سوال درست/غلط و یک سوال چهارگزینه‌ای.")

st.markdown("---")

# =========================
# سوال درست/غلط
st.subheader("سوال ۱: درست/غلط")
question1 = "جهان تقریبا چند سال قبل بوجود اومد؟"
correct_answer1 = "14 میلیارد سال"
user_answer1 = st.text_input(question1, key="q1")

if st.button("ثبت پاسخ سوال ۱"):
    if user_answer1.strip() == correct_answer1:
        st.success("آفرین ✅ درست گفتی!")
    elif user_answer1.strip() != "":
        st.error(f"متاسفم ❌ جواب درست: {correct_answer1}")

st.markdown("---")

# =========================
# سوال چهارگزینه‌ای
st.subheader("سوال ۲: چهارگزینه‌ای")
question2 = "کدام سیاره نزدیک‌ترین به خورشید است؟"
options2 = ["الف) زمین", "ب) مریخ", "ج) عطارد", "د) زهره"]
user_answer2 = st.radio(question2, options2, key="q2")

if st.button("ثبت پاسخ سوال ۲"):
    if "ج) عطارد" in user_answer2:
        st.success("آفرین ✅ درست گفتی!")
    else:
        st.error("متاسفم ❌ جواب درست: ج) عطارد")

st.markdown("---")

# =========================
# سوال تشریحی
st.subheader("سوال ۳: تشریحی")
question3 = "توضیح بده چرا برگ گیاهان سبز است؟"
user_answer3 = st.text_area(question3, key="q3")

if st.button("ثبت پاسخ سوال ۳"):
    if user_answer3.strip() != "":
        st.info("جواب شما ثبت شد ✅")
