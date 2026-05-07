from langchain.tools import tool
from ai_core.llm_client import get_llm

llm = get_llm()

@tool
def analyze_error_log(log: str):
    """分析日志，给出根因+修复方案"""
    prompt = f"""
    你是资深测试开发，请分析以下报错：
    1. 问题根因
    2. 修复方案
    日志：{log}
    """
    return llm.invoke(prompt).content