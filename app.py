import streamlit as st
import streamlit.components.v1 as components
from streamlit_autorefresh import st_autorefresh

# 1. Configuração do Cockpit
st.set_page_config(page_title="TAV GLOBAL | PRO", layout="wide")

# Refresh para manter os sinais de IA atualizados
st_autorefresh(interval=60 * 1000, key="global_logic")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #000000; color: #FFFFFF; }
    .block-container { padding-top: 1rem !important; }
    
    /* ACENDENDO AS MÉTRICAS */
    div[data-testid="stMetric"] {
        background-color: #111111 !important;
        border: 1px solid #444 !important;
        padding: 15px !important;
        border-radius: 5px;
    }
    [data-testid="stMetricLabel"] { color: #00FFFF !important; font-weight: bold !important; }
    [data-testid="stMetricValue"] { color: #FFFFFF !important; font-weight: 900 !important; }

    /* BARRA DE BATALHA GLOBAL */
    .battle-container { width: 100%; background: #330000; height: 35px; border-radius: 5px; border: 1px solid #555; }
    .battle-fill { background: #00FF88; height: 100%; box-shadow: 0 0 15px #00FF88; border-radius: 4px 0 0 4px; }
    
    /* ESTILO DAS ABAS */
    .stTabs [data-baseweb="tab"] { font-size: 1.2rem; font-weight: bold; color: white; }
    .stTabs [aria-selected="true"] { color: #00FFFF !important; border-bottom-color: #00FFFF !important; }
    </style>
    """, unsafe_allow_html=True)

def get_tv_widget(symbol):
    return f"""
    <div style="height:600px;">
      <div id="tv_chart_{symbol}" style="height:100%;"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget({{
        "autosize": true, "symbol": "{symbol}", "interval": "15",
        "timezone": "Etc/UTC", "theme": "dark", "style": "1",
        "locale": "br", "toolbar_bg": "#f1f3f6", "enable_publishing": false,
        "hide_side_toolbar": false, "allow_symbol_change": true,
        "container_id": "tv_chart_{symbol}"
      }});
      </script>
    </div>
    """

st.title("🛡️ TAV GLOBAL | INTELLIGENCE")

tab1, tab2 = st.tabs(["🟡 XAU/USD (GOLD)", "₿ BTC/USD (BITCOIN)"])

# --- ABA DO OURO ---
with tab1:
    col_main, col_info = st.columns([3, 1])
    
    with col_main:
        components.html(get_tv_widget("OANDA:XAUUSD"), height=610)
        # Battle Bar logo abaixo do gráfico
        st.markdown("""
            <div class="battle-container"><div class="battle-fill" style="width: 72%;"></div></div>
            <div style="display: flex; justify-content: space-between; font-weight: 900; color: white;">
                <span style="color: #00FF88;">BUY PRESSURE 72%</span>
                <span style="color: #FF3333;">SELL PRESSURE 28%</span>
            </div>
            """, unsafe_allow_html=True)

    with col_info:
        st.metric("PREÇO ATUAL", "$ 2,034.50", "+0.45%")
        st.metric("SINAL IA", "STRONG BUY", "91.6%")
        st.divider()
        st.subheader("📋 CRITÉRIOS XAU")
        st.write("✅ **Tendência H1:** Alta")
        st.write("✅ **RSI:** 54 (Neutro)")
        st.write("✅ **Volume:** Acima da média")
        if st.button("🚀 EXECUTAR OURO", use_container_width=True):
            st.toast("Ordem simulada enviada!")

# --- ABA DO BITCOIN ---
with tab2:
    col_main, col_info = st.columns([3, 1])
    
    with col_main:
        components.html(get_tv_widget("BINANCE:BTCUSDT"), height=610)
        st.markdown("""
            <div class="battle-container"><div class="battle-fill" style="width: 65%;"></div></div>
            <div style="display: flex; justify-content: space-between; font-weight: 900; color: white;">
                <span style="color: #00FF88;">BUY PRESSURE 65%</span>
                <span style="color: #FF3333;">SELL PRESSURE 35%</span>
            </div>
            """, unsafe_allow_html=True)

    with col_info:
        st.metric("BITCOIN", "$ 52,140", "+2.15%")
        st.metric("DOMINÂNCIA", "52.8%", "ALTA")
        st.divider()
        st.subheader("📋 CRITÉRIOS BTC")
        st.write("✅ **Suporte:** $ 51,200")
        st.write("⚠️ **Resistência:** $ 53,000")
        st.write("✅ **Funding Rate:** Positivo")
        st.button("🎯 ALERTA BTC", use_container_width=True)
