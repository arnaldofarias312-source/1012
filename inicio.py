import streamlit as st

# ========== CONFIGURACIÓN ==========
st.set_page_config(
    page_title="Para mi amor",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Ocultar menú y selector de tema
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display: none;}
    [data-testid="collapsedControl"] {display: none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# CSS romántico (sin verde)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff0f5 0%, #ffe0e7 100%);
    }
    h1, h2, h3, p, label, .stMarkdown {
        color: #b0306e !important;
    }
    .stTextInput > div > div > input {
        background-color: white;
        border: 2px solid #ff85a1;
        border-radius: 40px;
        padding: 10px 20px;
        font-size: 15px;
        color: #b0306e;
    }
    .stButton > button {
        background: linear-gradient(135deg, #ff5e7e, #ff2e63);
        color: white;
        border: none;
        border-radius: 40px;
        padding: 8px 16px;
        font-weight: bold;
        transition: 0.2s;
        width: 100%;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        background: #ff2e63;
    }
    .welcome {
        background: #ffeef2;
        border-left: 6px solid #ff2e63;
        padding: 12px;
        border-radius: 20px;
        text-align: center;
        font-weight: bold;
        margin: 20px 0;
    }
    .footer {
        background: rgba(255,255,240,0.6);
        border-radius: 30px;
        padding: 15px;
        text-align: center;
        margin-top: 40px;
    }
    hr {
        border-color: #ffb7c5;
    }
    </style>
""", unsafe_allow_html=True)

# ========== ESTADO ==========
if "auth" not in st.session_state:
    st.session_state.auth = False

# ========== VERIFICACIÓN ==========
def check_credenciales(nombre, apellido):
    return nombre.strip().lower() == "meriyeins" and apellido.strip().lower() == "fernandez"

# ========== LOGIN ==========
if not st.session_state.auth:
    st.markdown("<h1 style='text-align: center;'>💝 Para el amor de mi vida 💝</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.container():
            nombre = st.text_input("💕 NOMBRE", placeholder="Tu nombre", key="nom")
            apellido = st.text_input("💕 APELLIDO", placeholder="Tu apellido", key="ape")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("✨ Ingresar al corazón ✨", use_container_width=True):
                if check_credenciales(nombre, apellido):
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.markdown("<p style='background: #ffe4ec; padding: 10px; border-radius: 20px; text-align: center; color:#d81b4c;'>❌ Solo el amor de mi vida puede entrar ❌</p>", unsafe_allow_html=True)
                    # ❌ Sin globos aquí
    
    st.markdown("""
        <div style='text-align: center; margin-top: 30px;'>
            <p>💖 Esperando a mi persona especial 💖</p>
            <p style='font-size: 0.9rem;'>✨ Solo para Meriyeins Fernandez ✨</p>
        </div>
    """, unsafe_allow_html=True)

# ========== CONTENIDO PRINCIPAL ==========
else:
    st.markdown("<h1 style='text-align: center;'>✨ Para ti, Mi Amor ✨</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold;'>💖 Cada día a tu lado es un regalo del cielo 💖</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='welcome'>🌸 ¡Bienvenida Meriyeins! Todo esto es solo para ti 🌸</div>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center;'>📱 Toca cualquier tarjeta para un mensaje especial</h3>", unsafe_allow_html=True)
    
    # Tarjetas usando st.popover (cierre automático al hacer clic fuera)
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    cards = [
        (col1, "💕", "Te Amo", "Meriyeins, te amo más de lo que las palabras pueden expresar. Eres mi sol, mi luna y todas mis estrellas. Cada latido de mi corazón lleva tu nombre. 💖"),
        (col2, "💖", "Mi Felicidad", "Gracias por hacerme tan feliz. Tu sonrisa ilumina mis días más oscuros y tu amor transforma mi mundo en un lugar mágico. Eres mi razón de sonreír cada día. 😊"),
        (col3, "🏡", "Nuestra Familia", "No puedo esperar para construir una familia contigo. Sueño con nuestros hijos, nuestro hogar lleno de risas y cada aventura que viviremos juntos. Tú serás la mejor mamá del mundo. 👨‍👩‍👧‍👦"),
        (col4, "💑", "Para Siempre", "Eres mi presente y mi futuro. Quiero envejecer a tu lado, ver cómo el tiempo pasa mientras nuestro amor se hace más fuerte cada día. Contigo quiero vivir hasta el último de mis días. 💍")
    ]
    
    for col, emoji, titulo, mensaje in cards:
        with col:
            # Botón que abre un popover
            with st.popover(f"{emoji} {titulo}", use_container_width=True):
                st.markdown(f"<div style='text-align: center; font-size: 1.1rem;'>{mensaje}</div>", unsafe_allow_html=True)
                st.caption("💖 Toca fuera para cerrar 💖")
    
    # Mensajes rápidos (toasts)
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>💝 Mensajes para ti 💝</h3>", unsafe_allow_html=True)
    
    msgs_pequenos = [
        "🌹 Eres el sueño que nunca quiero despertar",
        "🌟 Contigo cada día es San Valentín",
        "💫 Tu amor es mi lugar favorito",
        "🎵 Mi corazón canta tu nombre",
        "🌺 Dueña de mis pensamientos",
        "⭐ Te eligiría una y mil veces"
    ]
    
    cols = st.columns(3)
    for i, msg in enumerate(msgs_pequenos):
        with cols[i % 3]:
            if st.button(msg, key=f"quick_{i}", use_container_width=True):
                st.toast(f"✨ {msg} ✨", icon="💖")
    
    # Footer
    st.markdown("""
        <div class='footer'>
            💘 Hecho con todo mi amor para ti, Meriyeins 💘<br>
            Eres mi razón de ser, mi alegría y mi todo.<br>
            <span style='font-size: 1.2rem;'>💖 Te amo más de lo que imaginas 💖</span>
        </div>
    """, unsafe_allow_html=True)

# ========== CORAZONES FLOTANTES ==========
st.markdown("""
    <script>
    function flotarCorazon() {
        const corazon = document.createElement('div');
        corazon.innerHTML = '💖';
        corazon.style.position = 'fixed';
        corazon.style.left = Math.random() * 100 + '%';
        corazon.style.bottom = '-20px';
        corazon.style.fontSize = (Math.random() * 20 + 15) + 'px';
        corazon.style.opacity = Math.random() * 0.5 + 0.3;
        corazon.style.pointerEvents = 'none';
        corazon.style.zIndex = '998';
        corazon.style.animation = 'subirCorazon ' + (Math.random() * 3 + 3) + 's linear';
        document.body.appendChild(corazon);
        setTimeout(() => corazon.remove(), 5000);
    }
    if (!document.querySelector('#estiloCorazon')) {
        const estilo = document.createElement('style');
        estilo.id = 'estiloCorazon';
        estilo.textContent = `
            @keyframes subirCorazon {
                0% { transform: translateY(0) rotate(0deg); opacity: 0.7; }
                100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
            }
        `;
        document.head.appendChild(estilo);
    }
    setInterval(flotarCorazon, 1800);
    </script>
""", unsafe_allow_html=True)