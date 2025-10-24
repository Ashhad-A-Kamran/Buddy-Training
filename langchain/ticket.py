

from langchain_core.prompts import PromptTemplate, load_prompt
from langchain.chat_models import init_chat_model

from dotenv import load_dotenv

load_dotenv()


loaded_template = load_prompt("./langchain/ticket_classification_prompt.json")



support_tickets = [
    "I was charged twice for my last purchase. Can you please refund one of the payments?"
    "My internet connection keeps dropping every few minutes. Please fix this issue.",
    "I forgot my password and can't log into my account anymore.",
    "How long does it usually take for an order to be delivered?",
    "I updated my payment method but the system still shows my old card.",
    "The mobile app keeps crashing every time I try to upload a photo.",
    "I want to change my email address linked to the account.",
    "Do you offer any discounts for students?",
    "My account was suspended without warning. Please explain why.",
    "I can’t hear any sound when joining video calls on your platform.",
    "Can you provide an invoice for my last three transactions?",
    "I accidentally deleted my profile — can I recover it?",
    "The website is showing a 404 error when I try to open the settings page.",
    "What is your refund policy for digital products?",
    "My subscription renewal failed even though I have enough balance in my card.",
    "I’m not receiving any password reset emails.",
    "Could you tell me more about your premium membership benefits?",
    "The download button isn’t working on my dashboard.",
    "I want to deactivate my account permanently.",
    "My bank statement shows an incorrect billing name for your service."
]

llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")


outputs = []
for i in support_tickets:
    print("i: ", i)
    prompt = loaded_template.format(ticket=i)
    result = llm.invoke(prompt)
    print("result: ", result.content)
    outputs.append(result.content)

print(outputs)