import gradio as gr
from query import ask

def handle_query(question):
    result = ask(question)

    sources = "\n".join(
        [f"• {source}" for source in result["sources"]]
    )

    return result["answer"], sources


with gr.Blocks() as demo:

    gr.Markdown("# The Unofficial Guide")

    question = gr.Textbox(
        label="Ask a Question"
    )

    answer = gr.Textbox(
        label="Answer",
        lines=8
    )

    sources = gr.Textbox(
        label="Sources",
        lines=5
    )

    button = gr.Button("Ask")

    button.click(
        handle_query,
        inputs=question,
        outputs=[answer, sources]
    )

demo.launch()