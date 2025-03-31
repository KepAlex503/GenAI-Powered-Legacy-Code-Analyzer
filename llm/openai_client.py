from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


class OpenAIClient:
    def __init__(self, model: str = "gpt-4o", temperature: float = 0.2):
        self.llm = ChatOpenAI(model_name=model,
                              temperature=temperature)

    def get_completion(self, prompt: str) -> str:
        messages = [HumanMessage(content=prompt)]
        response = self.llm(messages)
        return response.content
