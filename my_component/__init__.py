import os
import streamlit.components.v1 as components

# 指向新的 frontend 目录
_component_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend")

# 声明组件
_component_func = components.declare_component(
    "robust_component",
    path=_component_dir
)

def robust_component(name="World", key=None):
    """
    一个更稳健的组件，支持本地 JS 库和握手检测
    """
    # 调用组件函数
    component_value = _component_func(name=name, key=key, default=None)
    return component_value
