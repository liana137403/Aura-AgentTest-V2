import streamlit as st
from ai_core.test_agent import agent_executor

st.title("🤖 Aura-AgentTest V2.0 AI测试中台")
st.subheader("全链路自动化测试平台")

st.divider()
st.subheader("1️⃣ AI执行自动化测试")
task = st.text_input("输入指令：执行接口测试 / 执行UI测试 / 生成用例 / 分析日志")

if st.button("🚀 运行AI测试任务"):
    with st.spinner("AI执行中..."):
        res = agent_executor.invoke({"input": task})
        st.success("执行完成")
        st.code(res["output"])

st.divider()
st.subheader("2️⃣ AI日志根因分析")
log = st.text_area("粘贴报错日志")
if st.button("🔍 分析根因"):
    res = agent_executor.invoke({"input": f"分析日志：{log}"})
    st.write(res["output"])