# Aura-AgentTest V2.0 AI自动化测试平台

## 技术栈
- Python + Pytest + Playwright
- HttpClient 高可用封装（重试+日志+熔断）
- MySQL/Redis 连接池
- PO 模式 UI 自动化
- FastAPI Mock 服务
- LangChain AI Agent
- Streamlit 可视化中台
- Docker + Jenkins + Locust

---

## 核心功能
✅ 高可用 HTTP 客户端
✅ 接口自动化测试
✅ UI 自动化 PO 模式
✅ AI 自动执行测试
✅ AI 日志根因分析
✅ Mock 服务 + 批量造数
✅ 失败自动截图 + Allure 报告
✅ Docker 容器化
✅ CI/CD 流水线
✅ 性能压测

---

## 快速启动
```bash
pip install -r requirements.txt
playwright install chromium
streamlit run ai_core/web_app.py