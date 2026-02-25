import streamlit as st
import streamlit.components.v1 as components

# Configuração de Página "Cinema"
st.set_page_config(page_title="TAV GLOBAL | XAU BTC", layout="wide")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    .block-container { padding: 0rem !important; }
    /* Estilo dos Títulos */
    .crypto-title { color: #f7931a; font-weight: 900; font-size: 25px; margin-left: 20px; }
    .gold-title { color: #d4af37; font-weight: 900; font-size: 25px; margin-left: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Função para injetar o gráfico do TradingView
def get_tv_widget(symbol):
    return f"""
    <div style="height:92vh; width:100%;">
      <div id="tv_chart_{symbol}" style="height:100%; width:100%;"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget({{
        "autosize": true,
        "symbol": "{symbol}",
        "interval": "15",
        "timezone": "Etc/UTC",
        "theme": "dark",
        "style": "1",
        "locale": "br",
        "toolbar_bg": "#f1f3f6",
        "enable_publishing": false,
        "withdateranges": true,
        "hide_side_toolbar": false,
        "allow_symbol_change": true,
        "details": true,
        "hotlist": true,
        "calendar": true,
        "container_id": "tv_chart_{symbol}"
      }});
      </script>
    </div>
    """

# Interface em Abas para troca rápida
tab1, tab2 = st.tabs(["🟡 XAU/USD (OURO)", "₿ BTC/USD (BITCOIN)"])

with tab1:
    st.markdown('<p class="gold-title">GOLD / DOLLAR INDEX</p>', unsafe_allow_html=True)
    components.html(get_tv_widget("OANDA:XAUUSD"), height=800)

with tab2:
    st.markdown('<p class="crypto-title">BITCOIN / TETHER</p>', unsafe_allow_html=True)
    components.html(get_tv_widget("BINANCE:BTCUSDT"), height=800)
