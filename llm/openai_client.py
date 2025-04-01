from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.runnables import Runnable
from typing import List


class OpenAIClient:
    def __init__(self, model: str = "gpt-4", temperature: float = 0.2):
        self.llm: Runnable = ChatOpenAI(model_name=model, temperature=temperature)

    def get_completion(self, prompt: str) -> str:
        messages = [HumanMessage(content=prompt)]
        response = self.llm.invoke(messages)
        return response.content
