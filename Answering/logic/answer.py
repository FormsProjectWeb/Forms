import openai
from Forms.settings import OPEN_AI_KEY

openai.api_key = OPEN_AI_KEY

def answerRelatedTo(question, M=False, subject='', topics=''):
    answer = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
        {
            'role': 'user',
            'content': prompt(subject, topics, question, M)
        }
        ],
        temperature = 0.3
    )
    return answer['choices'][0]['message']['content']

def prompt (subject, topics, question, M=False):
    if M:
        return f"""
        Basándote en el contexto de {subject}, y teniendo en cuenta que se encuentran principalmente los temas de: {topics}
        Recibirás una pregunta abierta relacionada al tema, así que debes leer cuidadosamente la pregunta y responder lo más breve posible, no te extiendas. Aquí está la pregunta abierta que debes responder:

        {question}

        Recuerda, tu respuesta debe ser breve, no te extiendas.
        """
    return f"""
    Basándote en el contexto de {subject}, y teniendo en cuenta que se encuentran principalmente los temas de: {topics}
    Recibirás una pregunta de selección múltiple. Debes leer cuidadosamente la pregunta y las opciones de respuesta proporcionadas. Es crucial que analices la información relevante y apliques tu comprensión para identificar la respuesta correcta. No debes proporcionar una explicación ni justificar tu elección. Solo debes indicar la letra correspondiente a la respuesta correcta (A, B, C, D). Asegúrate de considerar solo la información proporcionada y tu conocimiento general si es aplicable. Aquí está la pregunta de selección múltiple que debes responder:

    {question}

    Recuerda, tu respuesta debe ser únicamente la letra de la opción que consideres correcta.
    """