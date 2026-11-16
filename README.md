# AI 助手

一个基于 Streamlit + DeepSeek API 的对话式 AI 应用，支持多会话管理、自定义人设、流式输出。

## 功能

- **多会话管理**：新建、切换、删除对话，历史自动保存到本地
- **自定义人设**：每个对话可独立设置昵称和性格，切换对话时人设自动恢复
- **流式输出**：回答逐字显示，不用等整段生成完
- **Token 统计**：每次回答显示输入/输出 token 数，方便估算成本
- **错误提示**：Key 无效、余额不足、网络不通都有明确中文提示

## 技术栈

| 层 | 选型 |
|---|---|
| 界面 | Streamlit 1.67.0 |
| 模型调用 | OpenAI SDK 3.46.0（OpenAI 兼容格式） |
| 模型 | DeepSeek `deepseek-chat` |
| 存储 | 本地 JSON 文件（`data/chats.json`） |

## 快速开始

### 1. 准备环境

需要 Python 3.10 以上（开发环境为 3.12）。

```bash
cd D:\learn
python -m venv .venv1
.\.venv1\Scripts\activate
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 API Key

去 [platform.deepseek.com](https://platform.deepseek.com) 注册并创建 API Key，然后在 PowerShell 里设置环境变量：

```powershell
$env:DEEPSEEK_API_KEY = "sk-你的key"
```

> 环境变量只对当前窗口有效。关掉窗口后要重新设置。

### 4. 启动

```bash
cd D:\learn
streamlit run xuexi/app.py
```

浏览器会自动打开 `http://localhost:8501`。

## 项目结构

```
D:\learn\
├── xuexi\
│   └── app.py              # 主程序（全部逻辑在这一个文件里）
├── data\
│   └── chats.json          # 对话数据（首次运行自动创建，不进 git）
├── notes\                  # 学习笔记
├── requirements.txt
├── .gitignore
└── README.md
```

## 已知限制

- **必须在 `D:\learn` 目录下启动**：数据文件用的是相对路径 `data/chats.json`，换个目录启动会读不到历史
- **数据存在本地**：换电脑或删掉 `data/` 目录，历史对话就没了
- **无账号体系**：单机单人使用，不能多端同步
- **无并发处理**：多个浏览器标签同时开，可能互相覆盖数据

## 后续计划

- [ ] 对话标题自动总结（现在是取第一句话前 12 字）
- [ ] 对话搜索
- [ ] 导出为 Markdown
- [ ] 部署到公网