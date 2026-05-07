# Aura-AgentTest V2.0

## 项目简介
Aura-AgentTest V2.0 是面向后端与 Web 应用的全链路自动化测试平台，整合接口自动化、UI E2E 自动化、数据驱动测试、Mock 服务、AI 智能测试能力、可视化报告、容器化部署与 CI/CD 流水线于一体。

项目采用分层架构设计，从底层基础工具封装、自动化引擎搭建，到 AI Agent 能力落地、工程化持续集成，形成一套可复用、可扩展、可部署、可接入流水线的标准化测试解决方案，适用于业务系统回归测试、版本迭代自动化验收、线上问题辅助定位等实际业务场景。

## 技术栈
- 编程语言：Python 3.10
- 接口测试：Requests、Tenacity、自定义高可用 HTTP 客户端
- UI 自动化：Playwright、PageObject 设计模式
- 测试框架：Pytest、Allure 可视化报告
- 数据驱动：YAML 配置文件解析、参数化用例管理
- 中间件：MySQL、Redis 连接池封装
- Mock 服务：FastAPI、Faker 海量测试数据生成
- AI 能力：LangChain、大模型 LLM 接入、自定义 Agent 工具调用
- 可视化中台：Streamlit
- 容器化：Docker
- 持续集成：Jenkinsfile 流水线
- 性能测试：Locust 高并发压测

## 项目架构与目录结构
```
aura_agenttestV2/
├── core/ # 底层基础能力封装
│ ├── http_client.py # 高可用 HTTP 请求客户端
│ ├── db_utils.py # MySQL 数据库连接池工具
│ └── redis_utils.py # Redis 缓存操作封装
├── utils/ # 通用工具层
│ └── yaml_parser.py # YAML 配置与用例解析工具
├── pages/ # UI 自动化 PageObject 分层
│ ├── base_page.py # 页面公共基类
│ └── login_page.py # 登录页元素与业务操作封装
├── mock_server/ # 本地 Mock 服务
│ └── main.py # FastAPI Mock 接口与造数逻辑
├── ai_core/ # AI 智能测试核心模块
│ ├── llm_client.py # 大模型统一调用封装
│ ├── case_agent.py # 接口用例智能生成 Agent
│ ├── log_agent.py # 日志异常根因分析 Agent
│ ├── test_agent.py # 测试任务调度与工具编排
│ └── web_app.py # Streamlit 可视化操作中台
├── test_cases/ # 自动化测试用例仓库
│ ├── test_api_auto.py # 接口自动化业务用例
│ ├── test_ui_po.py # UI E2E 自动化用例
│ └── test_api.yaml # YAML 数据驱动用例配置
├── conftest.py # Pytest 全局 Fixture、钩子函数、失败自动截图
├── Dockerfile # 项目容器化构建配置
├── Jenkinsfile # CI/CD 自动化流水线配置
├── locustfile.py # 接口高并发压测脚本
├── requirements.txt # 项目依赖清单
└── README.md # 项目说明文档
```


## 核心功能设计与实现
### 1. 底层高可用基础封装
- 封装通用 HTTP 客户端，支持 GET/POST 常用请求方法，内置失败重试、超时控制、异常捕获机制。
- 统一格式化请求日志、响应日志、接口耗时、状态码输出，便于问题追溯。
- 实现 MySQL、Redis 连接池封装，支持自动重连、连接复用，提供常用查询与读写能力，可完成接口落库数据一致性校验。

### 2. Pytest 测试框架与数据驱动
- 通过全局 Fixture 管理测试生命周期，实现环境初始化、资源自动回收。
- 基于 YAML 文件实现配置与代码分离，支持接口用例参数化、多环境配置隔离。
- 集成 Pytest 钩子函数，用例执行失败自动触发截图、绑定堆栈日志，与 Allure 报告关联展示。

### 3. Playwright UI 自动化（PO 模式）
- 采用 PageObject 分层思想，封装页面公共操作与独立页面元素业务逻辑。
- 封装元素等待、页面跳转、表单输入、断言校验等通用能力，降低用例编写冗余度。
- 模拟真实登录业务流程，完成正向场景全链路自动化校验。

### 4. FastAPI Mock 服务与测试数据构造
- 本地搭建 Mock 接口，解耦前端 / 测试对后端依赖，支持业务场景快速模拟。
- 基于 Faker 生成海量合规虚拟业务数据，可用于接口入参、数据库批量造数场景。

### 5. Allure 可视化测试报告
- 自动收集用例执行结果、接口报文、失败截图、异常堆栈。
- 报告按模块分类展示，支持趋势统计、失败用例快速定位，适配版本迭代回归复盘。

### 6. AI 智能测试 Agent 能力
- 封装大模型统一调用客户端，配置超时、基础 Prompt 管理。
- 基于 LangChain 实现自定义工具编排：支持执行接口测试、执行 UI 测试、异常日志根因分析。
- 支持输入自然语言指令，自动调度对应测试任务并返回执行结果与日志。

### 7. Streamlit 可视化中台
- 提供 Web 可视化操作界面，无需命令行即可触发自动化测试任务。
- 集成日志异常分析入口，粘贴报错日志自动解析根因与优化建议。
- 统一聚合所有测试能力，降低使用门槛，便于团队快速上手。

### 8. 工程化与持续集成
- 支持 Docker 一键镜像构建，打包 Python 环境、项目代码、Playwright 运行依赖，实现环境一致性。
- Jenkinsfile 定义流水线流程，包含依赖安装、接口测试、UI 测试、报告生成等阶段，可配置代码提交触发、定时回归任务。
- 基于 Locust 实现接口高并发压测，模拟多用户请求，统计 TPS、响应耗时、错误率，辅助性能瓶颈分析。

## 快速启动部署
### 1. 环境依赖安装
```bash
pip install -r requirements.txt
```
### 2. 安装 Playwright 浏览器内核
```bash
playwright install chromium
```

### 3. 大模型配置
修改 ai_core/llm_client.py，配置合法的大模型 APIKey 与请求地址：
```python
from langchain_openai import ChatOpenAI

def get_llm():
    return ChatOpenAI(
        api_key="your-api-key",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen-turbo"
    )
```
### 4. 启动可视化测试中台
```bash
streamlit run ai_core/web_app.py
```
默认访问地址：http://localhost:8501
### 5. 本地执行自动化测试
执行接口自动化
```bash
pytest test_cases/test_api_auto.py -v --alluredir=allure-results
```
执行 UI 自动化
```bash
pytest test_cases/test_ui_po.py -v --alluredir=allure-results
```
查看 Allure 测试报告
```bash
allure serve allure-results
```
### 6. 容器化启动
```bash
docker build -t aura-test-v2 .
```
```bash
docker run -p 8501:8501 aura-test-v2
```
## 项目适用场景
- 业务系统版本迭代回归自动化验收
- 接口、Web 前端 E2E 流程自动化覆盖
- 测试用例统一管理、批量执行与报告沉淀
- 日常问题日志智能分析、缩短定位耗时
- 团队内部测试工具平台复用与二次扩展
- CI/CD 流程接入，实现提交即自动化校验
