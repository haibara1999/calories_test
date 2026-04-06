import streamlit as st
import pandas as pd
import plotly.express as px
import os
import json
from google import genai
from PIL import Image

# 1. 页面基础设置
st.set_page_config(page_title="AI 营养师 | 热量估算工具", page_icon="🥗", layout="centered")

# 2. 初始化 Gemini 客户端
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.error("⚠️ 未检测到 API Key，请确保已在终端环境中配置 GEMINI_API_KEY。")
    st.stop()
client = genai.Client(api_key=api_key)

# 3. 网站标题与说明
st.title("📸 AI 减脂营养师")
st.markdown("上传你的餐食照片，AI 将为你精准估算总热量，并拆解营养成分比例。")

# 4. 图片上传组件
uploaded_file = st.file_uploader("请选择一张食物图片上传...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # 修复警告：使用 width="stretch" 代替 use_container_width=True
    st.image(image, caption="上传的餐食照片", width="stretch")
    
    if st.button("🔍 开始智能估算热量", type="primary"):
        with st.spinner("AI 正在飞速计算中，请稍候..."):
            
            prompt = """
            你是一个专业的临床营养师。请分析这张食物图片，并严格按照以下 JSON 格式输出结果，不要包含任何其他说明文字或 Markdown 标记：
            {
              "total_kcal": 450,
              "items": [
                {"name": "食物名称A", "weight_estimate_g": 100, "kcal": 110}
              ],
              "macros_percentage": {"protein": 20, "carbs": 50, "fat": 25, "fiber": 5}
            }
            """
            
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[prompt, image]
                )
                
                raw_text = response.text.strip()
                if raw_text.startswith("```json"):
                    raw_text = raw_text[7:]
                if raw_text.endswith("```"):
                    raw_text = raw_text[:-3]
                raw_text = raw_text.strip()
                
                data = json.loads(raw_text)
                
                st.success("计算完成！以下是详细报告：")
                
                st.subheader("🔥 总热量估算")
                st.metric(label="Total Calories", value=f"{data['total_kcal']} kcal")
                st.divider()
                
                st.subheader("📋 食物热量明细")
                df_items = pd.DataFrame(data['items'])
                df_items.columns = ["食物名称", "估算重量 (克)", "估算热量 (kcal)"]
                # 修复警告
                st.dataframe(df_items, width="stretch", hide_index=True)
                st.divider()
                
                st.subheader("📊 宏量营养素占比")
                macros = data['macros_percentage']
                df_macros = pd.DataFrame({
                    "营养素": ["蛋白质 (Protein)", "碳水化合物 (Carbs)", "脂肪 (Fat)", "膳食纤维 (Fiber)"],
                    "占比 (%)": [macros['protein'], macros['carbs'], macros['fat'], macros['fiber']]
                })
                
                fig = px.pie(df_macros, names="营养素", values="占比 (%)", hole=0.4, 
                             color_discrete_sequence=px.colors.qualitative.Pastel)
                # plotly_chart 通常不需要额外宽度参数即可自适应
                st.plotly_chart(fig)

            except Exception as e:
                st.error(f"❌ 分析过程中出现错误：{e}")
                st.info("提示：请检查终端是否正确开启了全局网络代理。")