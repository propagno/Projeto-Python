import gradio as gr
import openai

# Substitua pela sua chave de API da OpenAI
API_KEY = "API_KEY"

# Configure a chave de API
openai.api_key = API_KEY

def generate_text(prompt):
    """Gera texto usando a API OpenAI GPT-3.5-turbo."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Modelo mais recente
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100  # Configure conforme necessário
        )
        return response.choices[0].message['content'].strip()
    except openai.OpenAIError as e:
        return f"Erro ao gerar texto: {e}"

iface = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=5, label="Digite seu prompt"),
    outputs=gr.Textbox(label="Resposta da IA")
)

if __name__ == "__main__":
    iface.launch(share=True)