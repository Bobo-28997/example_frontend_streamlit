import os
import streamlit.components.v1 as components

# 获取组件目录的绝对路径
_component_dir = os.path.dirname(os.path.abspath(__file__))

# 声明组件
_component_func = components.declare_component(
    "simple_component",
    path=_component_dir
)

def simple_component(name="World", key=None):
    """创建一个简单的Hello World组件"""
    component_value = _component_func(name=name, key=key, default=None)
    return component_value
