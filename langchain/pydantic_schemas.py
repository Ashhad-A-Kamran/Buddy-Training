from pydantic import BaseModel, Field
from typing import List
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()


class ChatReponse(BaseModel):
    intent: str = Field(..., description = "the detected user intent (e.g 'product_inquire', 'product_status', 'greeting')")

    confidence: float = Field(...,ge=0, le=1, description = "A confidence score between 0 and 1 representing how sure the model is about the intent")

    answer: str = Field(..., description = "The chatbot's primary response to the user query")

    follow_up_questions: List[str] = Field(default_factory = list, description = "Suggested follow-up questions to keep the conversation flowing (can be empty)")

model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

structured_model = model.with_structured_output(ChatReponse)

result = structured_model.invoke("Hi there! I ordered a smart watch last week but  I haven't received any update yet. Can you tell me the status of my order?")


print(result)