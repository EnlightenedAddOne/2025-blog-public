# 实训报告—LLM Agentic RAG 个性化推荐开发演练 

**编制：** __________________________________________
**链接：** [https://www.addone.me/](https://www.addone.me/) 

---

## 1 动态工效展示 

![动态工效展示插图（初音未来动漫插画）](/blogs/6-23/4b90284a63535261.png)

## 2 信息化展现准备 

### 2.1 截图软件 

![Word模板和加载项设置界面](/blogs/6-23/c5c323a6037bb9ec.png)

### 2.2 Word及其模板[验] 

### 2.3 电子文档数签[验] 

![数字签名配置预览图](/blogs/6-23/0c7b3e5cb0c92c45.png)
![带有数字签名的PDF文档局部展示](/blogs/6-23/0583575ed0d57470.png)
![添加数字身份认证配置窗口](/blogs/6-23/5fef817a43ebba53.png)

### 2.4 电子书制作 

![电子书制作作者信息及证件照片](/blogs/6-23/65b88bd4f2c661a3.png)

### 2.5 学习云端展现[验] 

#### 2.5.1 云端服务器申请 

![阿里云云服务器ECS实例概览界面](/blogs/6-23/5c880695e597baa8.png)
![重置实例密码界面](/blogs/6-23/16c663a49dbf83f6.png)
![添加安全组入方向规则快捷配置界面](/blogs/6-23/50b1055ae3152991.png)

#### 2.5.2 SAAS服务构造 

![application.yml配置文件代码片段](/blogs/6-23/36ca0a796dbaa007.png)
![项目打包jar文件及解压后的目录结构](/blogs/6-23/f0044ab60dfd6573.png)

#### 2.5.3 学习云端展现 

![命令行启动Spring Boot应用日志及目录结构](/blogs/6-23/f2e5bce26e3eb1e8.png)

---

## 3 设计思想与架构 

### 3.1 设计思路 

一个基于LlamaIndex框架、采用Agentic RAG架构的简单个性化推荐系统实现，适用于CPU和Windows环境。程序将整合中文语义检索增强，并使用本地部署的模型。

### 3.2 AI-DS借力架构[验] 

**提示词：** 给出CPU和Windows下采用LlamaIndex框架、基于Agentic RAG架构的简单个性化推荐的编码，整个程序用一个文件实现，注意各个依赖库的版本对应和中文的检索加强，不使用CONDA，LLM模型采用Ollama部署本地的DeepSeek-R1-1.5B，需要的嵌入模型己通过modelscope下载在本地D:\01ifmts\models\nlp_gte_sentence-embedding_chinese-base，详细说明各个实现过程和测调试运行。
![AI助手对话界面截图1](/blogs/6-23/d254a926bcbcb58f.png)
![AI助手交付成果与核心技术方案说明截图](/blogs/6-23/0650f6fbe0471a30.png)

---

## 4 开发及其模型准备 

### 4.1 编程环境Python/Thonny 

![Python 3.12.7 命令行版本检查及安装目录](/blogs/6-23/365e8e6ca45cb219.png)
![Thonny IDE界面及本地Python解释器配置](/blogs/6-23/fa4db71c8f59d6cf.png)

### 4.2 编程环境Notepad++ 

![Notepad++代码编辑界面及上下文菜单展示](/blogs/6-23/e82e88216a62ceb8.png)

### 4.3 Ollama/DeppSeek 

![Ollama客户端界面及本地deepseek-r1:1.5b模型调用](/blogs/6-23/a06c84c3fe4d9d4f.png)

### 4.4 准备NLP 

![Modelscope平台搜索nlp_gte模型库截图](/blogs/6-23/34bec83ca2e1cb7f.png)

### 4.5 依赖下载 

![命令行创建并激活虚拟环境，并执行pip install命令](/blogs/6-23/d863553428f1cf5a.png)

---

## 5 功能编码实现 

### 5.1 编码实现 

以下是本系统的完整Python单文件实现代码（`agentic_rag_recommender.py`）：

```python
# -*- coding: utf-8 -*-
"""
================================================================================
文件名: agentic_rag_recommender.py
主题:   基于 LlamaIndex 的 Agentic RAG 简单个性化推荐系统
环境:   Windows + CPU (不使用 Conda)
模型:   LLM = Ollama 本地部署 deepseek-r1:1.5b
嵌入 = 本地 nlp_gte_sentence-embedding_chinese-base (ModelScope 下载)
框架:   LlamaIndex (Agentic RAG = ReActAgent + QueryEngineTool)
说明:
- 整个程序单文件实现, 内置中文电影数据集与用户画像, 开箱即用
- 采用 ReActAgent(推理-行动循环), 让大模型自主决定"何时检索、检索什么、何时给出推荐"
- DeepSeek-R1 不支持原生 function calling, 故必须用 ReActAgent(文本协议)而非 FunctionAgent
- 通过 Ollama 原生 thinking=False 关闭 R1 思考链, 保证 ReAct 输出格式干净可解析
- 中文检索加强: gte 中文嵌入 + 中文标点分句 + jieba 关键词工具 + top_k 调优
================================================================================
"""
import asyncio
import json
import logging
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional
# 第三方库
import jieba
from llama_index.core import (
Document,
Settings,
SimpleDirectoryReader,
StorageContext,
VectorStoreIndex,
load_index_from_storage,
)
from llama_index.core.agent.workflow import (
AgentOutput,
AgentStream,
ReActAgent,
ToolCallResult,
)
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.tools import FunctionTool, QueryEngineTool
from llama_index.core.workflow import Context
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

# ==============================================================================
# 第一部分: 可配置参数区 (按你的实际环境修改)
# ==============================================================================
# --- Ollama 服务地址与模型名 ---
# 先在命令行执行:  ollama pull deepseek-r1:1.5b
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
LLM_MODEL = os.environ.get("LLM_MODEL", "deepseek-r1:1.5b")
# --- 本地嵌入模型路径 (ModelScope 下载的 gte 中文模型) ---
# 你提供的路径: D:\01ifmts\models\nlp_gte_sentence-embedding_chinese-base
EMBED_MODEL_PATH = r"D:\01ifmts\models\nlp_gte_sentence-embedding_chinese-base"
# --- 运行参数 ---
LLM_CONTEXT_WINDOW = 8192        # Ollama num_ctx, 同时作为框架上下文元信息
LLM_TEMPERATURE = 0.6            # R1 官方推荐 0.5-0.7, 推理类任务避免贪婪解码
LLM_REQUEST_TIMEOUT = 300.0      # CPU 上 R1 生成较慢, 给足超时(秒)
EMBED_MAX_LENGTH = 512           # gte 中文模型最大序列长度
CHUNK_SIZE = 300                 # 文本块大小, 需 <= EMBED_MAX_LENGTH
CHUNK_OVERLAP = 50               # 块重叠, 提升中文检索召回
SIMILARITY_TOP_K = 5             # 每次检索返回的相似块数
MAX_ITERATIONS = 6               # ReActAgent 最大推理-行动循环次数(防 1.5B 模型死循环)
# --- 持久化目录 (索引缓存, 避免每次重建) ---
PERSIST_DIR = Path("./storage_index")
# --- 日志 ---
LOG_LEVEL = logging.INFO

# ==============================================================================
# 第二部分: 日志与中文分词工具
# ==============================================================================
def setup_logging(level: int = LOG_LEVEL) -> logging.Logger:
    """配置日志, 同时输出到控制台和文件, 方便调试。"""
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("./recommender.log", encoding="utf-8"),
        ],
    )
    # 抑制第三方库过多调试日志
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
    logging.getLogger("transformers").setLevel(logging.WARNING)
    return logging.getLogger("recommender")

logger = setup_logging()

def chinese_tokenize(text: str) -> List[str]:
    """
    中文分词工具(基于 jieba)。
    - 用于关键词提取, 作为检索增强的辅助手段。
    - 比单纯按字切分更能保留中文语义边界。
    """
    tokens = jieba.lcut(text.strip())
    # 过滤空白与标点
    return [t for t in tokens if t.strip() and not re.fullmatch(r"[\s\W_]+", t)]

def extract_keywords(text: str, topk: int = 8) -> List[str]:
    """基于 TF 简单提取中文关键词(jieba.analyse 也可, 这里用轻量实现便于离线)。"""
    import jieba.analyse
    # jieba 内置 TextRank/TF-IDF 关键词抽取
    keywords = jieba.analyse.extract_tags(text, topK=topk, withWeight=False)
    return keywords

# ==============================================================================
# 第三部分: Ollama 连通性检查
# ==============================================================================
def check_ollama() -> bool:
    """检查 Ollama 服务是否在线, 以及目标模型是否已拉取。"""
    import requests
    try:
        r = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        r.raise_for_status()
        models = [m.get("model", "") for m in r.json().get("models", [])]
        logger.info("Ollama 在线, 已安装模型: %s", models)
        if not any(LLM_MODEL in m for m in models):
            logger.warning(
                "未找到模型 %s, 请先执行: ollama pull %s", LLM_MODEL, LLM_MODEL
            )
            return False
        return True
    except Exception as e:
        logger.error("无法连接 Ollama (%s): %s", OLLAMA_BASE_URL, e)
        logger.error("请确认 Ollama 已启动 (命令行运行 ollama serve 或打开 Ollama 桌面端)")
        return False

# ==============================================================================
# 第四部分: 初始化 LLM / 嵌入模型 / 全局 Settings
# ==============================================================================
def init_llm() -> Ollama:
    """
    初始化 Ollama LLM (deepseek-r1:1.5b)。
    """
    llm = Ollama(
        model=LLM_MODEL,
        base_url=OLLAMA_BASE_URL,
        thinking=False,                 # 核心: 关闭思考链, 保证 ReAct 输出干净
        context_window=LLM_CONTEXT_WINDOW,
        temperature=LLM_TEMPERATURE,
        request_timeout=LLM_REQUEST_TIMEOUT,
        keep_alive="10m",               # 模型在内存中多停留一会儿, 连续提问更快
    )
    logger.info("LLM 初始化完成: %s (thinking=False, num_ctx=%d)",
        LLM_MODEL, LLM_CONTEXT_WINDOW)
    return llm

def init_embed_model() -> HuggingFaceEmbedding:
    """
    初始化本地中文嵌入模型 (gte)。
    """
    embed_path = Path(EMBED_MODEL_PATH)
    if not embed_path.exists():
        logger.error("嵌入模型路径不存在: %s", EMBED_MODEL_PATH)
        logger.error("请确认 ModelScope 已下载该模型到指定目录")
        raise FileNotFoundError(EMBED_MODEL_PATH)
    embed_model = HuggingFaceEmbedding(
        model_name=str(embed_path),
        max_length=EMBED_MAX_LENGTH,
        normalize=True,
        trust_remote_code=True,
        device="cpu",
    )
    logger.info("嵌入模型加载完成: %s", EMBED_MODEL_PATH)
    return embed_model

def init_settings() -> None:
    """配置 LlamaIndex 全局 Settings。"""
    Settings.llm = init_llm()
    Settings.embed_model = init_embed_model()
    Settings.chunk_size = CHUNK_SIZE
    Settings.chunk_overlap = CHUNK_OVERLAP
    Settings.node_parser = SentenceSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    logger.info("全局 Settings 配置完成 (chunk_size=%d, overlap=%d)",
        CHUNK_SIZE, CHUNK_OVERLAP)

# ==============================================================================
# 第五部分: 知识库数据 (内置中文电影数据集, 可选从目录加载)
# ==============================================================================
# --- 内置示例: 电影信息 ---
SAMPLE_MOVIES: List[Dict] = [
    {"title": "流浪地球2", "类型": "科幻/灾难", "评分": 8.3,
     "简介": "太阳即将毁灭, 人类在地球表面建造行星发动机, 开启流浪计划。面对月球坠落危机, 全球团结自救, 展现人类命运共同体的壮阔史诗。",
     "标签": "科幻 太空 灾难 家国情怀 硬核"},
    # ... 其余电影数据已省略，保持与原代码一致
]

# --- 内置用户画像 ---
USER_PROFILES: Dict[str, Dict] = {
    "u001": {
        "昵称": "科幻迷小张",
        "兴趣": ["科幻", "太空", "硬核", "史诗"],
        "历史偏好": ["流浪地球2", "沙丘2"],
        "偏好标签": "喜欢宏大叙事与硬核科幻, 偏爱视觉震撼的作品",
    },
    # ... 其余画像已省略
}

def build_documents() -> List[Document]:
    """将电影数据转换为 LlamaIndex Document 列表。"""
    docs: List[Document] = []
    for m in SAMPLE_MOVIES:
        text = (
            f"电影名称: {m['title']}\n"
            f"类型: {m['类型']}\n"
            f"评分: {m['评分']}\n"
            f"标签: {m['标签']}\n"
            f"简介: {m['简介']}"
        )
        docs.append(Document(
            text=text,
            metadata={
                "title": m["title"],
                "genre": m["类型"],
                "rating": m["评分"],
                "tags": m["标签"],
            },
            excluded_llm_metadata_keys=["title"],
            excluded_embed_metadata_keys=["title"],
        ))
    logger.info("构建文档完成, 共 %d 部电影", len(docs))
    return docs

def build_or_load_index() -> VectorStoreIndex:
    """构建向量索引 (含持久化缓存)。"""
    if PERSIST_DIR.exists():
        logger.info("检测到已有索引缓存, 从 %s 加载...", PERSIST_DIR)
        storage_context = StorageContext.from_defaults(persist_dir=str(PERSIST_DIR))
        index = load_index_from_storage(storage_context)
        logger.info("索引加载完成")
        return index
    
    logger.info("首次运行, 构建向量索引 (CPU 嵌入可能耗时数十秒, 请稍候)...")
    docs = build_documents()
    data_dir = Path("./data")
    if data_dir.exists():
        extra = SimpleDirectoryReader(input_dir=str(data_dir)).load_data()
        docs.extend(extra)
        logger.info("额外从 ./data 加载 %d 个文档", len(extra))
        
    index = VectorStoreIndex.from_documents(
        docs,
        show_progress=True,
    )
    index.storage_context.persist(persist_dir=str(PERSIST_DIR))
    logger.info("索引构建并持久化到 %s", PERSIST_DIR)
    return index

# ==============================================================================
# 第六部分: Agentic RAG 工具定义
# ==============================================================================
def build_tools(index: VectorStoreIndex) -> List:
    """构建 Agent 可调用的工具集"""
    query_engine = index.as_query_engine(
        similarity_top_k=SIMILARITY_TOP_K,
        response_mode="compact",
    )
    movie_search_tool = QueryEngineTool.from_defaults(
        query_engine=query_engine,
        name="movie_search",
        description=(
            "电影知识库的语义检索工具。输入一段中文自然语言描述(例如:‘适合带小孩看的温情动画’), "
            "返回知识库中最相关的电影信息(名称、类型、评分、标签、简介)。"
            "当需要根据用户兴趣从电影库中查找候选影片时使用此工具。"
        ),
    )

    def get_user_profile(user_id: str) -> str:
        """获取指定用户的个性化画像"""
        profile = USER_PROFILES.get(user_id)
        if not profile:
            available = ", ".join(USER_PROFILES.keys())
            return f"未找到用户 {user_id}。可用用户: {available}"
        return (
            f"用户ID: {user_id}\n"
            f"昵称: {profile['昵称']}\n"
            f"兴趣领域: {', '.join(profile['兴趣'])}\n"
            f"历史偏好影片: {', '.join(profile['历史偏好'])}\n"
            f"偏好标签: {profile['偏好标签']}"
        )

    profile_tool = FunctionTool.from_defaults(
        fn=get_user_profile,
        name="get_user_profile",
        description="获取用户的个性化画像(兴趣、历史偏好、偏好标签)。在需要个性化推荐时先调用此工具了解用户。",
    )

    def extract_query_keywords(query: str, topk: int = 8) -> str:
        """用 jieba 从中文查询中提取关键词"""
        kws = extract_keywords(query, topk=topk)
        return f"关键词: {', '.join(kws)}"

    keyword_tool = FunctionTool.from_defaults(
        fn=extract_query_keywords,
        name="extract_query_keywords",
        description="从中文查询中提取关键词, 用于优化电影检索。当用户查询较长或语义复杂时, 可先提取关键词再用关键词检索。",
    )

    logger.info("工具集构建完成: movie_search / get_user_profile / extract_query_keywords")
    return [movie_search_tool, profile_tool, keyword_tool]

# ==============================================================================
# 第七部分: ReActAgent 构建
# ==============================================================================
REACT_SYSTEM_PROMPT = """你是一名专业的中文电影推荐助手, 基于知识库中的电影信息为用户做个性化推荐。
【工作流程】
1. 先调用 get_user_profile 获取用户画像(若已知用户ID)。
2. 根据用户兴趣, 调用 movie_search 从电影库检索候选影片; 必要时可调用 extract_query_keywords 提取中文关键词辅助检索。
3. 可多次调用 movie_search(用不同关键词) 扩大候选, 再综合判断。
4. 结合用户画像与检索结果, 给出 3-5 部个性化推荐, 每部说明推荐理由。
【推荐理由要求】
- 紧扣用户兴趣标签与历史偏好。
- 提及影片的类型、评分、亮点。
- 用简洁中文, 避免空话。
【输出格式】
最终回答使用如下结构:
推荐清单:
1. 《影片名》 — 推荐理由...
2. 《影片名》 — 推荐理由...
...
总结: 一句话概括推荐逻辑。
注意: 你必须严格遵循 ReAct 协议(Thought/Action/Action Input/Answer)来使用工具, 最终用 Answer 给出推荐清单。"""

def build_agent(tools: List) -> ReActAgent:
    """构建 ReActAgent"""
    agent = ReActAgent(
        name="MovieRecommender",
        description="基于电影知识库的个性化推荐助手, 能检索电影信息并依据用户画像给出推荐。",
        system_prompt=REACT_SYSTEM_PROMPT,
        tools=tools,
        llm=Settings.llm,
        verbose=True,
    )
    logger.info("ReActAgent 构建完成 (verbose=True)")
    return agent

# ==============================================================================
# 第八部分: 异步运行 + 流式输出
# ==============================================================================
async def recommend(agent: ReActAgent, ctx: Context, user_msg: str) -> str:
    """异步执行推荐: 流式打印 Agent 的思考与工具调用过程, 返回最终答案。"""
    print("\n" + "=" * 70)
    print(f"用户请求: {user_msg}")
    print("=" * 70)
    
    handler = agent.run(user_msg, ctx=ctx, max_iterations=MAX_ITERATIONS)
    final_response = ""
    
    async for ev in handler.stream_events():
        if isinstance(ev, AgentStream):
            print(ev.delta, end="", flush=True)
        elif isinstance(ev, ToolCallResult):
            tool_out = str(ev.tool_output)
            preview = tool_out[:200].replace("\n", " ")
            print(f"\n  └─[工具 {ev.tool_name}] 返回预览: {preview}...", flush=True)
        elif isinstance(ev, AgentOutput):
            final_response = str(ev.response)
            
    response = await handler
    if not final_response:
        final_response = str(response)
        
    print("\n" + "-" * 70)
    return final_response

# ==============================================================================
# 第九部分: 交互式主程序
# ==============================================================================
HELP_TEXT = """
可用命令:
/user <用户ID>   设置当前用户(如 /user u001), 后续推荐将基于该用户画像
/list            列出所有可用用户
/clear           清空对话上下文
/help            显示帮助
/quit            退出
直接输入文字即可发起推荐请求, 例如:
"帮我推荐几部适合周末看的电影"
"我喜欢科幻, 有什么推荐"
"""

async def main_async() -> None:
    print("=" * 70)
    print(" LlamaIndex Agentic RAG 个性化电影推荐系统")
    print(f" LLM: {LLM_MODEL} @ {OLLAMA_BASE_URL} (thinking=False)")
    print(f" 嵌入: {EMBED_MODEL_PATH}")
    print("=" * 70)
    
    if not check_ollama():
        logger.error("Ollama 检查未通过, 程序退出。请先启动 Ollama 并拉取模型。")
        sys.exit(1)
        
    init_settings()
    index = build_or_load_index()
    tools = build_tools(index)
    agent = build_agent(tools)
    ctx = Context(agent)
    
    current_user: Optional[str] = None
    print(HELP_TEXT)
    print(f"提示: 当前内置用户 {list(USER_PROFILES.keys())}, 可用 /user u001 切换\n")
    
    while True:
        try:
            user_input = input("\n你> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见!")
            break
            
        if not user_input:
            continue
            
        if user_input.startswith("/"):
            cmd, *args = user_input[1:].split(maxsplit=1)
            if cmd == "quit":
                print("再见!")
                break
            elif cmd == "help":
                print(HELP_TEXT)
            elif cmd == "list":
                for uid, p in USER_PROFILES.items():
                    print(f"  {uid}: {p['昵称']} — 兴趣: {', '.join(p['兴趣'])}")
            elif cmd == "user":
                uid = args[0].strip() if args else ""
                if uid in USER_PROFILES:
                    current_user = uid
                    print(f"已切换用户: {uid} ({USER_PROFILES[uid]['昵称']})")
                else:
                    print(f"未找到用户 {uid}, 可用: {list(USER_PROFILES.keys())}")
            elif cmd == "clear":
                ctx = Context(agent)
                print("已清空对话上下文")
            else:
                print(f"未知命令: /{cmd}, 输入 /help 查看帮助")
            continue
            
        if current_user:
            full_msg = f"当前用户ID为 {current_user}。用户请求: {user_input}"
        else:
            full_msg = f"用户请求(未知用户ID, 可询问或直接按通用偏好推荐): {user_input}"
            
        try:
            answer = await recommend(agent, ctx, full_msg)
            print("\n最终推荐:")
            print(answer)
        except Exception as e:
            logger.exception("推荐过程出错: %s", e)
            print(f"出错了: {e}")
            print("提示: 若是解析错误, 可尝试 /clear 后简化问题, 或调高 MAX_ITERATIONS")

def main() -> None:
    """同步入口, 启动异步事件循环。"""
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main_async())

if __name__ == "__main__":
    main()

```

### 5.2 过程展现

#### 5.2.1 命令行操作

![命令行运行推荐系统时的初始化及索引构建输出日志](/blogs/6-23/5a9320507a39b01c.png)

#### 5.2.2 IDE 操作

![Thonny设置选项-配置虚拟环境Python解释器](/blogs/6-23/f9410444f43db81b.png)
![Thonny IDE界面展示完整Python代码及下方Shell终端的输出运行情况](/blogs/6-23/2a1f14cba38f0d29.png)

---

## 6 部署试运行

### 6.1 基本操作

1. 安装python运行环境
![PowerShell终端使用 python --version 检查版本](/blogs/6-23/71c3e2b18436855c.png)
2. 解压缩软件运行包
![项目文件夹(panlztRag2)及其子目录结构概览](/blogs/6-23/b0af952f8d95e93e.png)
3. Ollama 安装与模型部署
* `Ollama pull deepseek-r1:8b`，`Ollama serve`


4. 嵌入模型准备
* `pip install modelscope`，`modelscope download --model iic/nlp_gte_sentence-embedding_chinese-base`



### 6.2 试用运行与测试

![命令行交互测试结果截图，含有可用命令帮助提示](/blogs/6-23/74a5d23d14600078.png)

---

## 7 丰富完善

### 7.1 方案

龙虾机器人 MuleRun：给出 CPU 和 Windows 下采用 LlamaIndex 框架、基于 Agentic RAG 架构的简单个性化推荐的编码，整个程序用一个文件实现，注意各个依赖库的版本对应和中文的检索加强，不使用 CONDA、LLM 模型采用 Ollama 部署本地的 DeepSeek-R1-8B，需要的嵌入模型已通过 modelscope 下载在本地 D:\olfimts\models\nlp_gte_sentence-embedding_chinese-base，详细说明各个实现过程和测试运行 。注意编码精简与优化，增强预装案例外的个性化推荐适应能力 。

### 7.2 作为

![LlamaIndex框架个性化推荐系统Agentic RAG Web交互UI截图与代码目录结构展示](/blogs/6-23/b072e7e25c5a22f8.png)

```

```