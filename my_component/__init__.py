import os
import streamlit.components.v1 as components

# 指向当前目录 (因为 index.html 就在 __init__.py 旁边)
_component_dir = os.path.dirname(os.path.abspath(__file__))

_component_func = components.declare_component(
    "robust_component",
    path=_component_dir
)

def robust_component(name="World", key=None):
    return _component_func(name=name, key=key, default=None)
