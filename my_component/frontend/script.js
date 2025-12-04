// 获取 DOM 元素
const statusSpan = document.getElementById("connection-status");
const statusDot = document.getElementById("status-dot");
const nameSpan = document.getElementById("username");
const sendBtn = document.getElementById("send-btn");
const logArea = document.getElementById("log-area");
const pingBtn = document.getElementById("ping-btn");

// 辅助日志函数
function log(msg) {
    const time = new Date().toLocaleTimeString();
    logArea.textContent = `[${time}] ${msg}`;
    console.log(`[Component] ${msg}`);
}

// 核心渲染函数
function onRender(event) {
    // 1. 获取 Python 传来的参数
    const { name } = event.detail.args;
    
    // 2. 更新界面
    nameSpan.textContent = name || "Anonymous";
    
    // 3. 更新状态
    statusSpan.textContent = "已连接 (Python -> JS OK)";
    statusDot.classList.add("connected");
    sendBtn.disabled = false;

    // 4. 调整高度 (防止 iframe 塌陷)
    Streamlit.setFrameHeight();
}

// 发送数据函数
function sendData() {
    const timestamp = new Date().toISOString();
    const data = {
        action: "click",
        payload: `Clicked at ${timestamp}`,
        browserInfo: navigator.userAgent
    };
    
    log("正在发送数据到 Python...");
    try {
        Streamlit.setComponentValue(data);
        log("数据已发送!");
    } catch (e) {
        log("发送失败: " + e.message);
        statusDot.classList.add("error");
    }
}

// 绑定事件
sendBtn.onclick = sendData;

pingBtn.onclick = function() {
    log("Ping!");
    // 强制刷新高度，有时能唤醒 Streamlit
    Streamlit.setFrameHeight();
};

// 【关键步骤】
// 1. 挂载 Render 监听器
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender);

// 2. 通知 Streamlit 组件已准备就绪
try {
    Streamlit.setComponentReady();
    // 设置一个初始高度，防止第一次渲染时高度为0不可见
    Streamlit.setFrameHeight(200);
    log("组件已初始化 (Waiting for Render event...)");
} catch (e) {
    log("初始化失败: " + e.message);
}
