import streamlit as st

# 1. 页面基础设置：设置标题、图标和布局（必须放在最开头）
st.set_page_config(page_title="PhD | 专属增肌日程表", page_icon="🏋️", layout="centered")

# 2. 网站主标题与核心阶段目标
st.title("🏋️ PhD | 增肌期分化训练日程")
st.markdown("""
**🎯 核心目标：身体重组** 体重稳定在 **61kg - 62kg** 区间，**维持肌肉、降低脂肪**。

**💡 执行原则：**
- **离心控制：** 下放过程（如俯卧撑下去、引体向上下来）要**慢**，是增肌的关键。
- **营养窗口：** 训练后 **30分钟内** 务必补充蛋白质。
- **休息守护：** 严格执行 **13:00-14:00** 的 20-30min 午睡習慣。
""")
st.divider()

# 3. 创建早晚两个大标签页（Tabs），模拟思维导图的分支
tab_morning, tab_evening = st.tabs(["☀️ 晨间：推力与核心 (室内+户外)", "🌙 晚间：拉力与下肢 (室内+户外)"])

# --- ☀️ 晨间方案 ---
with tab_morning:
    st.header("☀️ 晨间：强化胸、肩、三头")
    st.info("总耗时：**约 25分钟**。先室内抗阻，后户外HIIT。")
    st.divider()

    # 3.1 热身（折叠卡片，默认不展示详情）
    with st.expander("步骤 1：室内热身与激活 (3min)", expanded=False):
        st.markdown("""
        - **肩绕环与手臂外旋**
        - **猫式伸展 (Cat-Cow)**
        - **动态侧板支撑**
        """)

    # 3.2 核心抗阻（粗体数字展示组数/次数/休息）
    st.subheader("步骤 2：室内抗阻训练 (12min)")
    col_m1, col_m2, col_m3 = st.columns(3)
    
    with col_m1:
        st.error("**钻石俯卧撑**")
        st.markdown("**3 组**, 组间休息 **45s**，每组做到**接近力竭**。")

    with col_m2:
        st.error("**下斜俯卧撑**")
        st.markdown("**3 组**, 双脚踩在凳/床沿。")

    with col_m3:
        st.error("**动态平板支撑**")
        st.markdown("**3 组**, 每组 **1 分钟**。")
    
    st.divider()

    # 3.3 户外收尾
    st.subheader("步骤 3：户外收尾 HIIT 跳绳 (10min)")
    st.warning("""
    - **总量：500 - 600 个**
    - **模式：** 分 **3 组**，每组 **150-200 个**。
    - **组间穿插：** 30秒的“空气拳”或原地小跑。
    """)


# --- 🌙 晚间方案 ---
with tab_evening:
    st.header("🌙 晚间：强化背部、二头、下肢")
    st.info("总耗时：**约 25分钟**。利用人体最大肌群（腿部）促进激素合成。")
    st.divider()

    # 3.1 激活
    with st.expander("步骤 1：室内下肢激活 (3min)", expanded=False):
        st.markdown("""
        - **自重深蹲** (慢速 15 次)
        - **侧向滑步**
        """)

    # 3.2 核心抗阻
    st.subheader("步骤 2：室内抗阻训练 (12min)")
    col_e1, col_e2, col_e3 = st.columns(3)
    
    with col_e1:
        st.success("**保加利亚剪蹲**")
        st.markdown("**3 组**, 每侧 **12 次**。单腿下蹲神技，重点对准股四头肌和平衡。")

    with col_e2:
        st.success("**慢速引体向上**")
        st.markdown("**3 组**, 执行 **“3-1-3”** 法则（3秒拉起，1秒停顿，3秒慢放）。")

    with col_e3:
        st.success("**原地爬行** (Inchworm)")
        st.markdown("**3 组**，双手走到最远后返回。")
    
    st.divider()

    # 3.3 户外收尾
    st.subheader("步骤 3：户外收尾 HIIT 跳绳 (10min)")
    st.warning("""
    - **总量：500 - 600 个**
    - **模式：间歇冲刺**。
    - **执行：** 快跳 **30秒** (极致频率)，休息 **30秒**，循环 **6-8 次**。
    """)