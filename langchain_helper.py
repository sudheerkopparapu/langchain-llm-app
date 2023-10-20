import langchain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools, initialize_agent, AgentType
from dotenv import load_dotenv
import pandas as pd
import numpy as np

load_dotenv()


def generate_pet_name(animal_type, color_of_pet):
    llm = OpenAI(temperature = 0.7)
    
    prompt_template_name = PromptTemplate(
        input_variables = ['animal_type', 'pet_color'],
        template = "I have a {animal_type} pet which is {pet_color} in colour. I want a cool name for it Suggest me five cool names for my pet by considering the color."
    )

    name_chain = LLMChain(llm = llm, prompt = prompt_template_name, output_key = "pet_name")

    response = name_chain({'animal_type': animal_type,
                           'pet_color': color_of_pet})
    return response

def langchain_agent():
    llm = OpenAI(temperature = 0.5)
    
    tools = load_tools(['wikipedia', 'llm-math'], llm = llm)
    agent = initialize_agent(tools, llm, agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)
    
    result = agent.run('What is the average age of a dog? Multiply the age by 3')
    print(result)

if __name__ == "__main__":
    print(generate_pet_name('cow','white'))
    
    # to run the agent
    # langchain_agent()
