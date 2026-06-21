import gradio as gr
from teacher import AITeacher

teacher = AITeacher("physics_dataset.json")

def ask(question):
    return teacher.answer_question(question)

demo = gr.Interface(
    fn=ask,
    inputs=gr.Textbox(
        label="Ask Physics Question"
    ),
    outputs=gr.Textbox(
        label="AI Teacher Answer"
    ),
    title="Physics AI Teacher"
)

demo.launch()
