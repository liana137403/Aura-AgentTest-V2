from langchain_openai import ChatOpenAI

def get_llm():
    return ChatOpenAI(
        api_key="sk-381890b52fe2450d90a8a1131373ea2e",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen-turbo",
        temperature=0.1
    )