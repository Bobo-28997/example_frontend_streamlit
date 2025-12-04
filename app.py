import streamlit as st
from datetime import datetime

# 导入简化组件
try:
    from simple_component import simple_component
    component_loaded = True
except ImportError as e:
    st.error(f"❌ 组件加载失败: {str(e)}")
    component_loaded = False

st.set_page_config(page_title="组件测试", layout="wide")

st.title("🧪 简单组件测试")

if component_loaded:
    st.success("✅ 组件加载成功!")
    
    # 使用组件
    name_input = st.text_input("输入要问候的名字:", value="World")
    
    # 调用组件
    returned_value = simple_component(name=name_input, key="hello_component")
    
    # 显示从组件返回的值
    if returned_value:
        st.info(f"📨 从组件接收到消息: {returned_value}")
        st.json({
            "接收时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "消息内容": returned_value
        })
else:
    st.error("❌ 无法加载组件，请检查组件目录结构和代码。")
