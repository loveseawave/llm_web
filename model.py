"""
这个python文件的目的是定义一个函数，函数的目标是返回ai的回复
"""
import os

from langchain_community.llms import Ollama
from langchain.chains import ConversationChain

from settings import Settings


def model(content, model, memory):
    """定义目标函数
    参数列表含义如下：
    use_model: 函数需要使用什么模型
    content: 传递给模型的上一句话
    """
    settings = Settings()

    os.system(f"ollama pull {model}")

    llm = Ollama(
        model=model,
        base_url=settings.url)

    chain = ConversationChain(llm=llm, memory=memory)

    return chain.invoke({'input': content})["response"]

# memory = ConversationBufferMemory(return_messages=True)
# memory.chat_memory.add_ai_message("牛顿提出了哪三条运动定律？")
# print(model("我的上一个问题是什么？", "llama2", memory))
