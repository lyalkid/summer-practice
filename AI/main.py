import gradio as gr
from transformers import pipeline

# Создаем пайплайны для задач
classifier = pipeline('sentiment-analysis')
generator = pipeline('text-generation', model='gpt2')
translator = pipeline('translation_en_to_fr')

def classify_text(text):
    result = classifier(text)
    return result

def generate_text(text):
    result = generator(text, max_length=50)
    return result[0]['generated_text']

def translate_text(text):
    result = translator(text)
    return result[0]['translation_text']

# Создаем интерфейсы для каждой задачи
classify_interface = gr.Interface(fn=classify_text, inputs="text", outputs="label", title="Классификация текста")
generate_interface = gr.Interface(fn=generate_text, inputs="text", outputs="text", title="Генерация текста")
translate_interface = gr.Interface(fn=translate_text, inputs="text", outputs="text", title="Перевод текста")

# Объединяем интерфейсы в табы
app = gr.TabbedInterface([classify_interface, generate_interface, translate_interface], ["Классификация", "Генерация", "Перевод"])

app.launch()
