import gradio as gr
from datetime import datetime

#astrology logic/rulebased

def get_zodiac_sign(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        day, month = date_obj.day, date_obj.month
    except:
        return "Unknown"

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries ♈"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus ♉"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini ♊"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer ♋"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo ♌"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo ♍"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra ♎"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio ♏"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius ♐"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn ♑"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius ♒"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces ♓"
    return "Unknown"

def generate_prediction(name, date, time, place):
    zodiac = get_zodiac_sign(date)
    return f"✨ Hello {name}, based on your birth details, your zodiac sign is {zodiac}. " \
           f"You are likely to find new opportunities around {place}. Trust your instincts and stay positive!"

def answer_question(name, date, time, place, question):
    q = question.lower()
    zodiac = get_zodiac_sign(date)

    if "career" in q:
        return f"🌟 {name}, as a {zodiac}, your career stars indicate steady growth. Hard work will pay off soon!"
    elif "love" in q or "relationship" in q:
        return f"💖 {name}, love energies are strong for {zodiac}. Be open to new connections."
    elif "health" in q:
        return f"💪 {name}, {zodiac} energy suggests you focus on balance. Prioritize rest and self-care."
    else:
        return f"🔮 The universe whispers patience, {name}. As a {zodiac}, trust the timing of your journey."

# Gradio UI
with gr.Blocks(theme="default") as demo:
    gr.Markdown("## ✨ AI Astrologer 🔮")
    gr.Markdown("Enter your birth details and receive astrology-based insights.")

    with gr.Row():
        name = gr.Textbox(label="Name")
        date = gr.Textbox(label="Birth Date (YYYY-MM-DD)")
        time = gr.Textbox(label="Birth Time (HH:MM)", placeholder="Optional")
        place = gr.Textbox(label="Birth Place")

    prediction_btn = gr.Button("Get Prediction")
    prediction_output = gr.Textbox(label="Prediction")

    prediction_btn.click(fn=generate_prediction,
                         inputs=[name, date, time, place],
                         outputs=prediction_output)

    gr.Markdown("### ❓ Ask a Free Question")
    question = gr.Textbox(label="Your Question")
    answer_output = gr.Textbox(label="Astrology Answer")
    ask_btn = gr.Button("Ask the Astrologer")

    ask_btn.click(fn=answer_question,
                  inputs=[name, date, time, place, question],
                  outputs=answer_output)

demo.launch()
