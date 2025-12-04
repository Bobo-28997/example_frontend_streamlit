import streamlit as st
import time
from my_component import robust_component

st.set_page_config(page_title="组件修复方案", layout="wide")

st.title("🛠️ 全本地化组件测试")
st.markdown("""
此版本使用了 **分离式结构** 和 **本地 JS 库**。
这通常能解决 Community Cloud 上的通信阻断问题。
""")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Python 输入端")
    name_input = st.text_input("请输入名字 (即时传给组件):", value="Streamlit User")
    
    # 增加一个重置 Key，强制组件重新挂载
    if st.button("♻️ 强制重载组件"):
        st.session_state['reset_key'] = time.time()
    
    component_key = f"comp_{st.session_state.get('reset_key', 'init')}"

with col2:
    st.subheader("2. 组件显示区域")
    # 调用组件
    returned_value = robust_component(name=name_input, key=component_key)

st.divider()

st.subheader("3. Python 接收端 (后端反馈)")
if returned_value:
    st.success("📡 成功接收到前端数据!")
    st.json(returned_value)
else:
    st.info("⏳ 等待组件发送数据...")

# 调试信息
st.markdown("---")
st.caption("Debug Info: 如果上方组件区域为空白，请检查浏览器控制台 (F12) 是否有 '404 Not Found' 错误。")
