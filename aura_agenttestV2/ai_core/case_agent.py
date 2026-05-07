from langchain.tools import tool
from ai_core.llm_client import get_llm

llm = get_llm()

@tool
def generate_test_cases(swagger_text: str):
    """根据Swagger自动生成Pytest接口用例"""
    prompt = f"""
    你是专业测试开发，根据Swagger生成可运行的pytest用例：
    1. 包含正向、异常、边界场景
    2. 输出Python代码
    Swagger：{swagger_text}
    """
    return llm.invoke(prompt).content