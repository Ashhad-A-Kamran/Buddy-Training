from dotenv import load_dotenv

import os
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser, PydanticOutputParser 

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from langchain_core.prompts import PromptTemplate
load_dotenv()


# LLM
llm_endpoint = HuggingFaceEndpoint(repo_id = "google/gemma-2-2b-it", task="text-generation", )
# We wrap our huggingface llm
llm = ChatHuggingFace(llm=llm_endpoint)


# Parser
parser = JsonOutputParser()

# # Prompt Template NOT WORKING
# template = PromptTemplate(template = ("You are a helpful travel assistant. Suggest 3 cities to visit in {region}. For each city include: -city\n -country \n -reason (why its worth visitng\n\n."), input_variables=["region"], partial_variables={"format_instructions": parser.get_format_instructions()})

# template = PromptTemplate(
#     template=(
#         "You are a helpful travel assistant.\n"
#         "Suggest 3 cities to visit in {region}.\n\n"
#         "For each city, include:\n"
#         "- city\n- country\n- reason (why it's worth visiting)\n\n"
#         "{format_instructions}\n\n"
#     ),
#     input_variables=["region"],
#     partial_variables={"format_instructions": parser.get_format_instructions()},
# )


# # Prompt
# prompt = template.format(region = "Pakistan")

# # Getting result from LLM
# raw_result = llm.invoke(prompt)

# #Parsed result
# parsed_result = parser.parse(raw_result.content)

# print("Raw result: ", raw_result)

# print("Parsed result: ", parsed_result)


############################################################################################################################

from pydantic import BaseModel, Field
from typing import List

# define pydantic schema
class Cityrecommendation(BaseModel):
    city: str = Field(dsecription = "Name of the city")
    country: str = Field(dsecription = "Name of the coutry")
    reason: str = Field(dsecription = "Why this city is worth visiting")

class TravelSuggestion(BaseModel):
    recommendations: List[Cityrecommendation]


parser = PydanticOutputParser(pydantic_object=TravelSuggestion)

template = PromptTemplate(
    template=(
        "You are a helpful travel assistant.\n"
        "Suggest 3 cities to visit in {region}.\n\n"
        "For each city, include:\n"
        "- city\n- country\n- reason (why it's worth visiting)\n\n"
        "{format_instructions}\n\n"
    ),
    input_variables=["region"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

formated_prompt = template.format(region = "Pakistan")
raw_result = llm.invoke(formated_prompt)
print("Raw result: ", raw_result.content)

parsed_result = parser.parse(raw_result.content)
print("Parsed result: ", parsed_result)
