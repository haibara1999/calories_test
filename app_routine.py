"""
夏日室内专属训练计划 —— Streamlit 外壳
真正的页面在同目录的 routine.html（自定义 HTML/CSS/SVG/JS）。
本文件只负责：设置页面、隐藏 Streamlit 默认 UI、整页嵌入 routine.html。
部署：把 app_routine.py 与 routine.html 一起推到 GitHub 仓库即可。
"""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="夏日室内专属计划",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 隐藏 Streamlit 默认顶栏/菜单/页脚，并清除页面留白，让自定义页面铺满
st.markdown(
    """
    <style>
      #MainMenu, footer {visibility: hidden;}
      [data-testid="stHeader"] {display: none;}
      [data-testid="stToolbar"] {display: none;}
      .stApp {background: #FCF8F0;}
      .block-container,
      [data-testid="stAppViewBlockContainer"],
      [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        max-width: 100% !important;
      }
      [data-testid="stVerticalBlock"] {gap: 0 !important;}
      iframe {display: block; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "routine.html"
html = html_path.read_text(encoding="utf-8")

# 整页嵌入；高度给足，内部自适应滚动
components.html(html, height=1000, scrolling=True)
