


from langchain.chat_models import init_chat_model

from dotenv import load_dotenv

load_dotenv()



realistic_responses = [
    "What is the capital of Japan? Give one sentence",
    "How many continents are there on Earth? Give one sentence",
    "Convert 100 USD to Pakistani Rupees (approximate). Give one sentence",
    "Who was the first person to walk on the moon? Give one sentence",
    "What is the chemical symbol for water? Give one sentence",
    "What is 456 × 23? Give one sentence",
    "What year did World War II end? Give one sentence"
]

creative_responses = [
    "Imagine humans could fly — describe a normal day in that world. Give one paragraph",
    "Create a short dialogue between the Moon and the Sun. Give one paragraph",
    "Invent a new fairy tale creature and explain its powers. Give one paragraph",
    "Describe a futuristic city in the year 2500. Give one paragraph",
    "If sadness were a color, how would you describe it?",
    "Invent a new flavor of ice cream and explain why people would love it. Give one paragraph",
    "Design a chair that could be used in zero gravity.",
    "Imagine a smartphone for dogs — what features would it have? Give one paragraph"
]



# llm = init_chat_model(
#     "llama-3.3-70b-versatile", 
#     model_provider="groq", 
#     temperature=0.6)

# result = llm.invoke("what is the eid day")
# print(result.content)


temps = [0,1,1.5,2]


import json
all_results = {}

for i in temps:
    llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq", temperature=i)
    res_1_realistic, res_2_realistic = [], []
    res_1_creative, res_2_creative = [], []

    for j in realistic_responses:
        res_1_realistic.append(llm.invoke(j).content)
        res_2_realistic.append(llm.invoke(j).content)

    for j in creative_responses:
        res_1_creative.append(llm.invoke(j).content)
        res_2_creative.append(llm.invoke(j).content)

    all_results[i] = {
        "realistic_1": res_1_realistic,
        "realistic_2": res_2_realistic,
        "creative_1": res_1_creative,
        "creative_2": res_2_creative
    }


with open("responses.json", "w") as f:
    json.dump(all_results, f, indent=4)

print("Saved results to responses.json")