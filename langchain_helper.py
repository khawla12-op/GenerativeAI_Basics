from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY']= openapi_key
llm= OpenAI(temperature=0.7)
def generate_destination_name_and_hotels(destination):
    #Chain1:destination name
    prompt_template_name = PromptTemplate(
    input_variables=["destination"],
    template="I'm going to {destination} what are the best hotels there?",
)
    chain = LLMChain(llm=llm, prompt=prompt_template_name,output_key="destination_name")

    #Chain2:Restaurant items
    prompt_template_items = PromptTemplate(
    input_variables=["destination_name"],
    template="Give me a list of 5 hotels in {destination_name}",
)
    chain2 = LLMChain(llm=llm, prompt=prompt_template_items,output_key="destination_hotels")
    #Applying the sequential chain
    chain=SequentialChain(
       chains=[chain,chain2],
       input_variables=["destination"],
       output_variables=["destination_name","destination_hotels"])
    response=chain({"destination":"Marrakech"})
    return response
#Now let's test:
if __name__=="__main__":
    print(generate_destination_name_and_hotels('Moroccan'))