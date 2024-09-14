# Sequential Chain for Destination and Hotel Recommendation

## Aim of the Project

This project aims to build an intelligent assistant using LangChain and OpenAI's language model. The assistant helps users discover top hotels in a given travel destination by leveraging a **sequential chain** of prompts to generate context-aware responses. 

### Key Features:

- **Sequential Processing**: The project uses multiple chains of prompts to handle different stages of the conversation. The first prompt asks for the best hotels in a given destination, and the second prompt refines the response by listing five specific hotel options.
  
- **LangChain Framework**: The project utilizes LangChain's `SequentialChain` and `LLMChain` to structure the workflow, ensuring that the output from the first prompt (destination name) becomes the input for the second prompt (hotel recommendations).
  
- **Customizable Interactions**: The system is customizable to handle different travel-related queries, allowing for flexible integration into a broader travel recommendation platform.

### How it Works:

1. **Destination Inquiry**: The first chain uses the input destination (e.g., "Marrakech") to ask about the best hotels in that location.
2. **Hotel Recommendations**: The second chain generates a list of 5 specific hotel names based on the destination provided.
3. **Output**: The final response contains both the destination name and a list of recommended hotels.

The notebook cover also how to build a simple conversational chatbot that retains memory of past interactions, allowing for more natural and context-aware conversations.

- **Conversational Memory**: The chatbot retains previous conversation context using LangChain's `ConversationBufferWindowMemory`.
- **Question Answering**: Capable of answering questions, performing basic calculations, and providing explanations.

## Prerequisites

To get started, ensure you have the following installed:

- Python 3.7 or higher
- An OpenAI API key
- Required Python packages: `langchain`, `openai`, `streamlit`

## Installation


1. Create and activate a virtual environment:
  ```bash
   python -m venv venv
   venv\Scripts\activate
  ```
2. Install the required dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API in the secret_key.py file
4. To run the chatbot ,use the following command:
  ```bash
  streamlit run main.py
```


   
