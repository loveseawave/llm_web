"""这个python文件的1目的是通过streamlit库来制作一个前端"""
import os

from langchain.memory import ConversationBufferMemory # 导入记忆类
import streamlit as st # 导入前端库streamlit

from model import model

if "memory" not in st.session_state:
    # 通过streamlit库的session_state实现记忆等关键参数不会归零
    st.session_state["content"] = [{"role": "ai", "message": "我是你的ai助手，请多指教！"}]
    st.session_state["memory"] = ConversationBufferMemory(return_message=True)

st.title("ollama开源模型对话")

# 让用户输入使用模型，并自动安装模型
use_model = st.text_input("请输入使用的ollama模型")
st.markdown("[模型查阅请见ollama官网](https://ollama.fan/)")

# 安装模型
pull_model = st.button(f"安装{use_model}模型")
st.session_state["use_model"] = use_model

if pull_model:
    with st.spinner("模块安装中"):
        os.system(f"ollama pull {use_model}")

# 遍历st.session_state，将其展示在屏幕上
for message in st.session_state["content"]:
    st.chat_message(message["role"]).write(message["message"])

prompt = st.chat_input()

if prompt and use_model:
    st.session_state["content"].append({"role": "human",
                                        "message": prompt})
    st.chat_message("human").write(prompt)
    with st.spinner("AI正在思考中，请稍后再拨~"):
        try:
            # 调用函数，完成ai对话
            response = model(content=prompt, model=use_model, memory=st.session_state["memory"])
        except:
            # model()函数有很多地方可能会库错，所以统一捕获异常
            st.info("raise unknown error!")
            st.stop()

    # 当ai返回消息后，构建字典，存入st.session_state，展示在页面上
    msg = {"role": "ai", "message": response}
    st.session_state["content"].append(msg)
    st.chat_message("ai").write(response)

elif not use_model:
    # 当用户没有输入模型时
    st.info("you must type a model!")
    st.stop()

else:
    # 当用户没有输入消息时
    st.info("you must type a message for model!")
    st.stop()
