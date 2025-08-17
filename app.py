import gradio as gr
from transformers import pipeline
from datetime import datetime

# -----------------
# Load HuggingFace model (lightweight + efficient)
# -----------------
generator = pipeline("text2text-generation", model="google/flan-t5-base")

# -----------------
# Zodiac helper
# -----------------
def get_zodiac_sign(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        day, month = date_obj.day, date_obj.month
    except:
        return "Unknown"

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries "
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus "
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini "
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer "
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo "
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo "
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra "
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio "
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius "
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn "
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius "
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces "
    return "Unknown"

# -----------------
# Functions
# -----------------
def generate_prediction(name, date, time, place):
    zodiac = get_zodiac_sign(date)
    return f" Hello {name}, based on your birth details, your zodiac sign is {zodiac}. " \
           f"You may experience shifts in energy around {place}. Stay mindful and positive!"

def answer_question(name, date, time, place, question):
    zodiac = get_zodiac_sign(date)
    prompt = f"""
    You are a knowledgeable astrologer. 
    Person's name: {name}
    Birth place: {place}
    Zodiac sign: {zodiac}.
    The person asks: "{question}".
    Give a thoughtful astrology-based response that sounds mystical, 
    but stays positive and helpful. Do not repeat the question. 
    Avoid saying the person will literally become an astrologer.
    """
    result = generator(prompt, max_length=200, temperature=0.7)
    return result[0]["generated_text"]


# -----------------
# Styled Gradio UI
# -----------------
with gr.Blocks(css="""
    body {background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);}
    .gradio-container {max-width: 700px !important; margin: auto;}
    .card {background: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.2);}
    h1 {text-align: center; color: #fff; font-size: 2em; margin-bottom: 10px;}
    h2 {color: #333;}
""") as demo:

    gr.Markdown("<h1>AI Astrologer </h1>")
    gr.Markdown("<p style='text-align:center; color:white;'>Enter your details and ask the stars for guidance </p>")

    with gr.Column(elem_classes="card"):
        with gr.Row():
            name = gr.Textbox(label="Name")
            place = gr.Textbox(label="Birth Place")
        with gr.Row():
            date = gr.Textbox(label="Birth Date (YYYY-MM-DD)")
            time = gr.Textbox(label="Birth Time (HH:MM)", placeholder="Optional")

        prediction_btn = gr.Button(" Get Prediction", variant="primary")
        prediction_output = gr.Textbox(label="Your Astrology Prediction")

    with gr.Column(elem_classes="card"):
        gr.Markdown("### Ask the Stars")
        question = gr.Textbox(label="What do you want to ask?", placeholder="e.g. How is my career looking?")
        ask_btn = gr.Button("Ask Astrologer", variant="secondary")
        answer_output = gr.Textbox(label="Astrology Answer")

    # Button actions
    prediction_btn.click(fn=generate_prediction,
                         inputs=[name, date, time, place],
                         outputs=prediction_output)

    ask_btn.click(fn=answer_question,
                  inputs=[name, date, time, place, question],
                  outputs=answer_output)

demo.launch()
