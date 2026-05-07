from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.tools import tool
from langchain.prompts import ChatPromptTemplate
from ai_core.llm_client import get_llm
from ai_core.log_agent import analyze_error_log
from ai_core.case_agent import generate_test_cases
import subprocess
import sys

llm = get_llm()

@tool
def run_api_test():
    """执行接口自动化测试"""
    r = subprocess.run([sys.executable, "-m", "pytest", "test_cases/test_api_auto.py", "-v"], capture_output=True, text=True)
    return f"{'✅成功' if r.returncode==0 else '❌失败'}\n{r.stdout}"

@tool
def run_ui_test():
    """执行UI自动化测试"""
    r = subprocess.run([sys.executable, "-m", "pytest", "test_cases/test_ui_po.py", "-v"], capture_output=True, text=True)
    return f"{'✅成功' if r.returncode==0 else '❌失败'}\n{r.stdout}"

tools = [run_api_test, run_ui_test, analyze_error_log, generate_test_cases]

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是AI测试助手，可执行测试、生成用例、分析日志"),
    ("user", "{input}"),
    ("assistant", "{agent_scratchpad}")
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)