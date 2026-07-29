"""Premium dark-glassmorphic UI system for ZingyByte AI — styles, animations, layout."""

import streamlit as st


def inject_premium_styles() -> None:
    """Injects the full ZingyByte design-system CSS into the Streamlit page."""
    font_size = st.session_state.get("ui_font_size", 15)

    st.markdown(
        f"""
        <style>
        /* ════════════════════════════════════════════════════════════
           FONTS
        ════════════════════════════════════════════════════════════ */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Sora:wght@600;700;800&display=swap');

        /* ════════════════════════════════════════════════════════════
           DESIGN TOKENS
        ════════════════════════════════════════════════════════════ */
        :root {{
            --brand-primary  : #FF4B4B;
            --brand-secondary: #FF8533;
            --brand-gold     : #FFB347;
            --bg-deep        : #09090C;
            --bg-card        : rgba(255,255,255,0.018);
            --bg-card-hover  : rgba(255,75,75,0.06);
            --border-subtle  : rgba(255,255,255,0.055);
            --border-brand   : rgba(255,75,75,0.22);
            --text-primary   : #F0F0F5;
            --text-secondary : #8A8A9A;
            --text-muted     : #4A4A5A;
            --green-glow     : #4ADE80;
            --radius-sm      : 10px;
            --radius-md      : 14px;
            --radius-lg      : 18px;
            --radius-xl      : 24px;
            --ease-spring    : cubic-bezier(0.34, 1.56, 0.64, 1);
            --ease-smooth    : cubic-bezier(0.22, 1, 0.36, 1);
            --ease-out       : cubic-bezier(0.4, 0, 0.2, 1);
            --transition-fast: 0.18s;
            --transition-base: 0.28s;
            --transition-slow: 0.45s;
        }}

        /* ════════════════════════════════════════════════════════════
           KEYFRAMES
        ════════════════════════════════════════════════════════════ */
        @keyframes fadeUp {{
            from {{ opacity:0; transform:translateY(18px); }}
            to   {{ opacity:1; transform:translateY(0);    }}
        }}
        @keyframes fadeIn {{
            from {{ opacity:0; }}
            to   {{ opacity:1; }}
        }}
        @keyframes scaleIn {{
            from {{ opacity:0; transform:scale(0.94); }}
            to   {{ opacity:1; transform:scale(1);    }}
        }}
        @keyframes slideInLeft {{
            from {{ opacity:0; transform:translateX(-16px); }}
            to   {{ opacity:1; transform:translateX(0);     }}
        }}
        @keyframes shimmer {{
            0%   {{ background-position:-600px 0; }}
            100% {{ background-position: 600px 0; }}
        }}
        @keyframes gradientPan {{
            0%,100% {{ background-position:0%   50%; }}
            50%      {{ background-position:100% 50%; }}
        }}
        @keyframes blink {{
            0%,100% {{ opacity:1; }}
            50%      {{ opacity:0; }}
        }}
        @keyframes pulseDot {{
            0%,100% {{ opacity:1;   transform:scale(1);    }}
            50%      {{ opacity:0.5; transform:scale(0.85); }}
        }}
        @keyframes floatY {{
            0%,100% {{ transform:translateY(0);   }}
            50%      {{ transform:translateY(-8px); }}
        }}
        @keyframes spinOrbit {{
            from {{ transform:rotate(0deg);   }}
            to   {{ transform:rotate(360deg); }}
        }}
        @keyframes badgePop {{
            from {{ opacity:0; transform:translateX(-8px) scale(0.88); }}
            to   {{ opacity:1; transform:translateX(0)   scale(1);    }}
        }}
        @keyframes ripple {{
            0%   {{ box-shadow:0 0 0 0   rgba(255,75,75,0.22); }}
            100% {{ box-shadow:0 0 0 14px rgba(255,75,75,0);   }}
        }}
        /* Floating food item drift paths */
        @keyframes drift1 {{
            0%,100% {{ transform: translate(0px, 0px)   rotate(0deg)   scale(1);    }}
            25%      {{ transform: translate(12px,-18px) rotate(8deg)   scale(1.04); }}
            50%      {{ transform: translate(6px, -32px) rotate(-4deg)  scale(0.97); }}
            75%      {{ transform: translate(-8px,-14px) rotate(10deg)  scale(1.02); }}
        }}
        @keyframes drift2 {{
            0%,100% {{ transform: translate(0px,   0px) rotate(0deg)   scale(1);    }}
            30%      {{ transform: translate(-14px,-20px) rotate(-9deg)  scale(1.05); }}
            60%      {{ transform: translate(8px, -28px) rotate(5deg)   scale(0.96); }}
            80%      {{ transform: translate(-5px,-10px)  rotate(-3deg)  scale(1.03); }}
        }}
        @keyframes drift3 {{
            0%,100% {{ transform: translate(0px,  0px) rotate(0deg)  scale(1);    }}
            20%      {{ transform: translate(16px,-10px) rotate(12deg) scale(1.04); }}
            55%      {{ transform: translate(-10px,-25px) rotate(-6deg) scale(0.98); }}
            80%      {{ transform: translate(5px, -8px) rotate(8deg)  scale(1.02); }}
        }}
        @keyframes drift4 {{
            0%,100% {{ transform: translate(0px, 0px)  rotate(0deg)  scale(1);    }}
            35%      {{ transform: translate(-18px,-15px) rotate(-10deg) scale(1.06); }}
            65%      {{ transform: translate(10px,-22px) rotate(7deg)   scale(0.95); }}
        }}
        @keyframes drift5 {{
            0%,100% {{ transform: translate(0px, 0px) rotate(0deg) scale(1);    }}
            40%      {{ transform: translate(20px,-18px) rotate(-14deg) scale(1.05); }}
            70%      {{ transform: translate(-6px,-30px) rotate(6deg) scale(0.97); }}
        }}
        @keyframes hoverGlow {{
            0%,100% {{ filter: drop-shadow(0 0 8px rgba(255,133,51,0.4)); }}
            50%      {{ filter: drop-shadow(0 0 20px rgba(255,75,75,0.7)); }}
        }}

        /* ════════════════════════════════════════════════════════════
           BASE / RESET
        ════════════════════════════════════════════════════════════ */
        html, body {{
            background: var(--bg-deep) !important;
            scroll-behavior: smooth;
        }}

        /* ════════════════════════════════════════════════════════════
           FLOATING FOOD BACKGROUND LAYER
        ════════════════════════════════════════════════════════════ */
        .zb-food-bg {{
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 0;
            overflow: hidden;
        }}

        .zb-food-item {{
            position: absolute;
            font-size: 3.4rem;
            opacity: 0.045;
            transition: opacity 0.6s ease, filter 0.6s ease, transform 0.4s ease;
            user-select: none;
            will-change: transform;
            filter: drop-shadow(0 0 0px transparent);
        }}

        /* Each item gets a unique drift animation + delay */
        .zb-food-item:nth-child(1)  {{ top:  6%; left:  4%; animation: drift1 9s  ease-in-out infinite;         }}
        .zb-food-item:nth-child(2)  {{ top: 12%; right: 6%; animation: drift2 11s ease-in-out infinite 1.2s;   }}
        .zb-food-item:nth-child(3)  {{ top: 35%; left:  2%; animation: drift3 13s ease-in-out infinite 2.5s;   }}
        .zb-food-item:nth-child(4)  {{ top: 55%; right: 3%; animation: drift4 10s ease-in-out infinite 0.8s;   }}
        .zb-food-item:nth-child(5)  {{ top: 72%; left:  5%; animation: drift5 12s ease-in-out infinite 3.2s;   }}
        .zb-food-item:nth-child(6)  {{ top: 85%; right: 7%; animation: drift1 14s ease-in-out infinite 1.8s;   }}
        .zb-food-item:nth-child(7)  {{ top: 22%; left: 48%; animation: drift2 10s ease-in-out infinite 4.0s;   }}
        .zb-food-item:nth-child(8)  {{ top: 60%; left: 44%; animation: drift3  8s ease-in-out infinite 0.5s;   }}
        .zb-food-item:nth-child(9)  {{ top: 40%; right:48%; animation: drift4 15s ease-in-out infinite 2.0s;   }}
        .zb-food-item:nth-child(10) {{ top: 90%; left: 30%; animation: drift5 11s ease-in-out infinite 3.8s;   }}
        .zb-food-item:nth-child(11) {{ top:  3%; left: 60%; animation: drift1 13s ease-in-out infinite 1.0s;   }}
        .zb-food-item:nth-child(12) {{ top: 78%; right:40%; animation: drift2  9s ease-in-out infinite 2.8s;   }}

        /* On hover anywhere over the page, food items softly glow */
        body:hover .zb-food-item {{
            opacity: 0.10;
        }}

        .zb-food-item:hover {{
            opacity: 0.55 !important;
            filter: drop-shadow(0 0 18px rgba(255,133,51,0.65)) !important;
            transform: scale(1.35) !important;
            transition: opacity 0.25s ease, filter 0.25s ease, transform 0.25s var(--ease-spring) !important;
            z-index: 1;
            pointer-events: all !important;
            animation: hoverGlow 1.2s ease-in-out infinite !important;
        }}

        html, body, .stMarkdown, p, li, td, th {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            font-size: {font_size}px;
            line-height: 1.70;
            color: var(--text-primary);
            -webkit-font-smoothing: antialiased;
        }}
        
        .stMarkdown p, .stMarkdown li {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
            font-size: {font_size}px !important;
        }}

        h1, h2, h3, h4, h5, h6 {{
            font-family: 'Sora', sans-serif !important;
            letter-spacing: -0.035em;
            line-height: 1.2 !important;
        }}

        a {{ color: var(--brand-secondary); text-decoration: none; }}
        a:hover {{ color: var(--brand-gold); }}

        /* ════════════════════════════════════════════════════════════
           SCROLLBAR
        ════════════════════════════════════════════════════════════ */
        ::-webkit-scrollbar       {{ width:5px; height:5px; }}
        ::-webkit-scrollbar-track {{ background:transparent; }}
        ::-webkit-scrollbar-thumb {{
            background: rgba(255,75,75,0.28);
            border-radius:99px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: rgba(255,75,75,0.5);
        }}

        /* ════════════════════════════════════════════════════════════
           STREAMLIT CHROME — hide junk
        ════════════════════════════════════════════════════════════ */
        #MainMenu, footer, header {{ visibility:hidden !important; }}

        /* ════════════════════════════════════════════════════════════
           SIDEBAR
        ════════════════════════════════════════════════════════════ */
        [data-testid="stSidebar"] {{
            background: linear-gradient(175deg,
                rgba(11,11,15,0.98) 0%,
                rgba(6,6,9,1) 100%) !important;
            backdrop-filter: blur(32px) saturate(1.5) !important;
            border-right: 1px solid rgba(255,255,255,0.038) !important;
            padding-top: 0 !important;
        }}

        [data-testid="stSidebar"] > div:first-child {{
            padding-top: 1.4rem;
        }}

        /* ════════════════════════════════════════════════════════════
           SIDEBAR BRAND BLOCK
        ════════════════════════════════════════════════════════════ */
        .zb-sidebar-brand {{
            animation: slideInLeft var(--transition-slow) var(--ease-smooth) both;
        }}

        .zb-logo-row {{
            display: flex;
            align-items: center;
            gap: 11px;
            margin-bottom: 6px;
        }}

        .zb-logo-icon {{
            width: 38px; height: 38px;
            background: linear-gradient(135deg, var(--brand-primary) 0%, var(--brand-secondary) 100%);
            border-radius: var(--radius-md);
            display: flex; align-items: center; justify-content: center;
            font-size: 1.22rem;
            box-shadow: 0 4px 16px rgba(255,75,75,0.35);
            animation: ripple 2.4s ease-out infinite;
            flex-shrink: 0;
        }}

        .zb-logo-text {{
            display: flex; flex-direction: column; gap: 1px;
        }}

        .zb-logo-text strong {{
            font-family: 'Sora', sans-serif !important;
            font-size: 1.08rem !important;
            font-weight: 800 !important;
            background: linear-gradient(135deg, #FF4B4B 0%, #FF8533 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.1 !important;
            letter-spacing: -0.04em;
        }}

        .zb-logo-text span {{
            font-size: 0.68rem !important;
            color: var(--text-muted);
            font-weight: 500 !important;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }}

        /* Status pill */
        .zb-status-pill {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 0.70rem !important;
            color: var(--green-glow);
            font-weight: 600 !important;
            padding: 4px 10px;
            background: rgba(74,222,128,0.08);
            border: 1px solid rgba(74,222,128,0.16);
            border-radius: 99px;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }}

        .zb-status-pill::before {{
            content: '';
            width: 6px; height: 6px;
            background: var(--green-glow);
            border-radius: 50%;
            animation: pulseDot 1.8s ease-in-out infinite;
            flex-shrink: 0;
        }}

        /* ════════════════════════════════════════════════════════════
           SIDEBAR SECTION LABELS
        ════════════════════════════════════════════════════════════ */
        .zb-section-label {{
            font-size: 0.65rem !important;
            font-weight: 700 !important;
            color: var(--text-muted) !important;
            letter-spacing: 0.09em;
            text-transform: uppercase;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 7px;
        }}

        .zb-section-label::after {{
            content: '';
            flex: 1;
            height: 1px;
            background: var(--border-subtle);
            border-radius: 99px;
        }}

        /* ════════════════════════════════════════════════════════════
           SIDEBAR CONTEXT SUMMARY
        ════════════════════════════════════════════════════════════ */
        .zb-context-card {{
            background: linear-gradient(135deg,
                rgba(255,133,51,0.07) 0%,
                rgba(255,75,75,0.04) 100%);
            border: 1px solid rgba(255,133,51,0.16);
            border-radius: var(--radius-md);
            padding: 13px 15px;
            animation: scaleIn var(--transition-slow) var(--ease-smooth) both;
        }}

        .zb-context-label {{
            font-size: 0.65rem !important;
            font-weight: 700 !important;
            color: var(--brand-secondary);
            letter-spacing: 0.07em;
            text-transform: uppercase;
            display: block;
            margin-bottom: 7px;
        }}

        .zb-context-text {{
            font-size: 0.78rem !important;
            color: #B0B0C2 !important;
            line-height: 1.55 !important;
        }}

        /* ════════════════════════════════════════════════════════════
           SIDEBAR STAT TILES
        ════════════════════════════════════════════════════════════ */
        .zb-stat-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            margin-bottom: 4px;
        }}

        .zb-stat-tile {{
            background: rgba(255,255,255,0.025);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-sm);
            padding: 11px 12px;
            transition: background var(--transition-fast) var(--ease-out),
                        border-color var(--transition-fast) var(--ease-out);
            cursor: default;
        }}

        .zb-stat-tile:hover {{
            background: rgba(255,75,75,0.05);
            border-color: rgba(255,75,75,0.18);
        }}

        .zb-stat-value {{
            font-family: 'Sora', sans-serif !important;
            font-size: 1.18rem !important;
            font-weight: 700 !important;
            color: var(--text-primary) !important;
            line-height: 1 !important;
            display: block;
            margin-bottom: 4px;
        }}

        .zb-stat-label {{
            font-size: 0.66rem !important;
            color: var(--text-muted) !important;
            font-weight: 500 !important;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }}

        /* ════════════════════════════════════════════════════════════
           SIDEBAR QUICK TIPS
        ════════════════════════════════════════════════════════════ */
        .zb-tips {{
            display: flex;
            flex-direction: column;
            gap: 7px;
        }}

        .zb-tip-row {{
            display: flex;
            align-items: flex-start;
            gap: 8px;
            font-size: 0.76rem !important;
            color: var(--text-muted) !important;
            line-height: 1.45 !important;
            padding: 7px 9px;
            background: rgba(255,255,255,0.014);
            border-radius: var(--radius-sm);
            border: 1px solid rgba(255,255,255,0.03);
            transition: background var(--transition-fast) var(--ease-out);
        }}

        .zb-tip-row:hover {{
            background: rgba(255,255,255,0.028);
        }}

        .zb-tip-icon {{
            flex-shrink: 0;
            margin-top: 1px;
        }}

        .zb-tip-row b {{
            color: var(--brand-secondary) !important;
            font-weight: 600 !important;
        }}

        /* ════════════════════════════════════════════════════════════
           SIDEBAR BUTTONS
        ════════════════════════════════════════════════════════════ */
        .stButton > button {{
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.82rem !important;
            border-radius: var(--radius-sm) !important;
            transition:
                transform    var(--transition-fast) var(--ease-spring),
                box-shadow   var(--transition-fast) var(--ease-out),
                background   var(--transition-fast) var(--ease-out) !important;
        }}

        .stButton > button:hover {{
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 22px rgba(255,75,75,0.2) !important;
        }}

        .stButton > button:active {{
            transform: translateY(0) scale(0.98) !important;
        }}

        /* ════════════════════════════════════════════════════════════
           MAIN AREA — TOP STATUS BAR
        ════════════════════════════════════════════════════════════ */
        .zb-topbar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 9px 16px;
            background: rgba(255,255,255,0.016);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-lg);
            margin-bottom: 22px;
            animation: fadeIn var(--transition-slow) var(--ease-smooth) both;
            min-height: 44px;
        }}

        .zb-topbar-left {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .zb-topbar-icon {{
            font-size: 1.1rem;
            line-height: 1;
        }}

        .zb-topbar-name {{
            font-family: 'Sora', sans-serif !important;
            font-size: 0.88rem !important;
            font-weight: 700 !important;
            color: var(--text-primary) !important;
            letter-spacing: -0.02em;
        }}

        .zb-topbar-sep {{
            color: var(--text-muted);
            font-size: 0.75rem !important;
            font-weight: 300 !important;
        }}

        .zb-topbar-sub {{
            font-size: 0.78rem !important;
            font-weight: 400 !important;
            color: var(--text-secondary) !important;
        }}

        .zb-topbar-right {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-shrink: 0;
        }}

        /* Generic neutral chip */
        .zb-chip {{
            display: inline-flex;
            align-items: center;
            gap: 5px;
            font-size: 0.70rem !important;
            font-weight: 600 !important;
            color: var(--text-muted);
            background: rgba(255,255,255,0.03);
            border: 1px solid var(--border-subtle);
            padding: 4px 10px;
            border-radius: 99px;
            letter-spacing: 0.02em;
            white-space: nowrap;
        }}

        /* Model chip — orange accent */
        .zb-chip-model {{
            display: inline-flex;
            align-items: center;
            gap: 5px;
            font-size: 0.70rem !important;
            font-weight: 700 !important;
            color: var(--brand-secondary);
            background: rgba(255,133,51,0.08);
            border: 1px solid rgba(255,133,51,0.20);
            padding: 4px 10px;
            border-radius: 99px;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            white-space: nowrap;
        }}

        /* Live indicator chip — green */
        .zb-chip-live {{
            display: inline-flex;
            align-items: center;
            gap: 5px;
            font-size: 0.70rem !important;
            font-weight: 700 !important;
            color: var(--green-glow);
            background: rgba(74,222,128,0.07);
            border: 1px solid rgba(74,222,128,0.18);
            padding: 4px 10px;
            border-radius: 99px;
            letter-spacing: 0.04em;
            white-space: nowrap;
            animation: pulseDot 2s ease-in-out infinite;
        }}

        /* ════════════════════════════════════════════════════════════
           HERO / EMPTY STATE
        ════════════════════════════════════════════════════════════ */
        .zb-hero {{
            text-align: center;
            padding: 20px 0 10px;
        }}

        .zb-hero-icon {{
            font-size: 7.5rem;
            display: block;
            animation: floatY 3.8s ease-in-out infinite;
            margin-bottom: 18px;
            filter: drop-shadow(0 12px 40px rgba(255,75,75,0.5));
            transition: transform 0.3s var(--ease-spring), filter 0.3s ease;
            cursor: default;
        }}

        .zb-hero-icon:hover {{
            transform: scale(1.12) rotate(-5deg);
            filter: drop-shadow(0 16px 60px rgba(255,133,51,0.7));
        }}

        .zb-hero-title {{
            font-family: 'Sora', sans-serif !important;
            font-size: 3.1rem !important;
            font-weight: 800 !important;
            background: linear-gradient(135deg, #FF4B4B 0%, #FF8533 55%, #FFB347 100%);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation:
                gradientPan 5s ease infinite,
                fadeUp 0.65s var(--ease-smooth) both;
            letter-spacing: -0.06em;
            line-height: 1.05 !important;
            margin-bottom: 10px;
        }}

        .zb-hero-sub {{
            font-size: 1.0rem !important;
            color: var(--text-secondary);
            font-weight: 400 !important;
            animation: fadeUp 0.7s 0.1s var(--ease-smooth) both;
            margin-bottom: 22px;
            line-height: 1.55 !important;
        }}

        .zb-hero-badge-wrap {{
            display: flex;
            justify-content: center;
            margin-bottom: 36px;
        }}

        .zb-hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255,75,75,0.07);
            border: 1px solid rgba(255,75,75,0.16);
            border-radius: 99px;
            padding: 7px 18px;
            font-size: 0.80rem !important;
            color: var(--brand-secondary);
            font-weight: 600 !important;
            letter-spacing: 0.03em;
            animation: fadeUp 0.7s 0.2s var(--ease-smooth) both;
        }}

        .zb-hero-badge::before {{
            content: '';
            width: 7px; height: 7px;
            background: var(--green-glow);
            border-radius: 50%;
            animation: pulseDot 1.8s ease-in-out infinite;
        }}

        /* ════════════════════════════════════════════════════════════
           WELCOME SECTION — First-time user greeting
        ════════════════════════════════════════════════════════════ */
        .zb-welcome {{
            text-align: center;
            padding: 6px 0 14px;
            animation: fadeUp 0.6s var(--ease-smooth) both;
        }}
        .zb-welcome-title {{
            font-family: 'Sora', sans-serif !important;
            font-size: 1.5rem !important;
            font-weight: 700 !important;
            color: var(--text-primary) !important;
            margin-bottom: 4px;
            letter-spacing: -0.03em;
            line-height: 1.2;
        }}
        .zb-welcome-sub {{
            font-size: 0.92rem !important;
            color: var(--text-secondary) !important;
            margin-bottom: 12px;
            font-weight: 400 !important;
        }}
        .zb-welcome-items {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 4px 20px;
            max-width: 620px;
            margin: 0 auto 12px;
        }}
        .zb-welcome-item {{
            font-size: 0.85rem !important;
            color: var(--text-secondary) !important;
            line-height: 1.5;
            flex: 0 0 auto;
        }}
        .zb-welcome-tagline {{
            font-size: 0.9rem !important;
            color: var(--brand-secondary) !important;
            font-weight: 600 !important;
            margin-top: 2px;
        }}

        /* Prompt grid section label */
        .zb-grid-label {{
            text-align: center;
            font-size: 0.72rem !important;
            font-weight: 700 !important;
            color: var(--text-muted);
            letter-spacing: 0.09em;
            text-transform: uppercase;
            margin-bottom: 16px;
            animation: fadeIn 0.8s 0.3s both;
        }}

        /* ════════════════════════════════════════════════════════════
           SUGGESTION CARDS
        ════════════════════════════════════════════════════════════ */
        .zb-card {{
            background: linear-gradient(145deg,
                rgba(255,255,255,0.03) 0%,
                rgba(255,255,255,0.012) 100%);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-lg);
            padding: 18px 20px;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            transition:
                transform        var(--transition-base) var(--ease-spring),
                box-shadow       var(--transition-base) var(--ease-out),
                border-color     var(--transition-base) var(--ease-out),
                background       var(--transition-base) var(--ease-out);
            margin-bottom: 12px;
        }}

        /* Shimmer sweep */
        .zb-card::before {{
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(
                105deg,
                transparent 30%,
                rgba(255,255,255,0.055) 50%,
                transparent 70%
            );
            transform: translateX(-100%);
            transition: transform 0.55s var(--ease-out);
        }}

        .zb-card:hover::before  {{ transform: translateX(100%); }}

        .zb-card:hover {{
            background: linear-gradient(145deg,
                rgba(255,75,75,0.08) 0%,
                rgba(255,133,51,0.04) 100%);
            border-color: var(--border-brand);
            transform: translateY(-4px) scale(1.015);
            box-shadow:
                0 14px 44px rgba(255,75,75,0.14),
                0 1px 0 rgba(255,255,255,0.06) inset;
        }}

        .zb-card-emoji {{
            font-size: 1.6rem;
            display: block;
            margin-bottom: 8px;
            filter: drop-shadow(0 2px 6px rgba(255,75,75,0.3));
        }}

        .zb-card-title {{
            font-family: 'Sora', sans-serif !important;
            font-size: 0.92rem !important;
            font-weight: 700 !important;
            color: var(--text-primary) !important;
            display: block;
            margin-bottom: 5px;
            letter-spacing: -0.02em;
        }}

        .zb-card-desc {{
            font-size: 0.80rem !important;
            color: var(--text-secondary) !important;
            line-height: 1.45 !important;
            display: block;
        }}

        /* Staggered entrance */
        .zb-card {{ animation: fadeUp 0.5s var(--ease-smooth) both; }}
        .zb-card:nth-child(1) {{ animation-delay: 0.10s; }}
        .zb-card:nth-child(2) {{ animation-delay: 0.18s; }}
        .zb-card:nth-child(3) {{ animation-delay: 0.26s; }}
        .zb-card:nth-child(4) {{ animation-delay: 0.34s; }}

        /* ════════════════════════════════════════════════════════════
           CHAT MESSAGES — Premium unified styling
        ════════════════════════════════════════════════════════════ */

        .stChatMessage {{
            background: linear-gradient(145deg,
                rgba(255,255,255,0.03) 0%,
                rgba(255,255,255,0.008) 100%) !important;
            border: 1px solid var(--border-subtle) !important;
            border-radius: var(--radius-lg) !important;
            padding: 1.1rem 1.4rem !important;
            margin-bottom: 1rem !important;
            box-shadow:
                0 8px 40px rgba(0,0,0,0.22),
                0 1px 0 rgba(255,255,255,0.03) inset !important;
            backdrop-filter: blur(14px) !important;
            animation: fadeUp 0.38s var(--ease-smooth) both;
            transition:
                box-shadow   var(--transition-base) var(--ease-out),
                border-color var(--transition-base) var(--ease-out) !important;
        }}
        .stChatMessage:hover {{
            border-color: rgba(255,255,255,0.08) !important;
            box-shadow:
                0 14px 52px rgba(0,0,0,0.28),
                0 1px 0 rgba(255,255,255,0.05) inset !important;
        }}

        /* Streaming cursor */
        .zb-cursor {{
            display: inline-block;
            width: 2px;
            height: 1em;
            background: var(--brand-secondary);
            border-radius: 2px;
            margin-left: 2px;
            vertical-align: middle;
            animation: blink 0.7s step-end infinite;
        }}

        /* Metric badges */
        .zb-bubble-metrics {{
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            margin-top: 10px;
            padding-top: 10px;
            border-top: 1px solid rgba(255,255,255,0.06);
        }}

        /* Badge row (used during streaming) */
        .zb-badge-row {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: 8px;
        }}

        /* ════════════════════════════════════════════════════════════
           METRIC BADGES
        ════════════════════════════════════════════════════════════ */
        .zb-badge-row {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: 10px;
        }}

        .zb-badge {{
            display: inline-flex;
            align-items: center;
            gap: 5px;
            padding: 4px 10px;
            border-radius: 8px;
            font-size: 0.70rem !important;
            font-weight: 600 !important;
            background: rgba(255,75,75,0.06);
            border: 1px solid rgba(255,75,75,0.12);
            color: var(--brand-secondary);
            letter-spacing: 0.025em;
            animation: badgePop 0.32s var(--ease-spring) both;
            transition:
                background   var(--transition-fast) var(--ease-out),
                border-color var(--transition-fast) var(--ease-out),
                transform    var(--transition-fast) var(--ease-spring);
        }}

        .zb-badge:hover {{
            background: rgba(255,75,75,0.12);
            border-color: rgba(255,75,75,0.26);
            transform: translateY(-2px);
        }}

        /* Streaming shimmer variant */
        .zb-badge.streaming {{
            background: linear-gradient(
                90deg,
                rgba(255,75,75,0.07)  0%,
                rgba(255,133,51,0.15) 50%,
                rgba(255,75,75,0.07)  100%
            );
            background-size: 600px 100%;
            animation: shimmer 1.5s linear infinite;
            border-color: rgba(255,133,51,0.28);
            color: #FFB347;
        }}

        /* ════════════════════════════════════════════════════════════
           CHAT INPUT
        ════════════════════════════════════════════════════════════ */
        [data-testid="stChatInput"] textarea {{
            font-family: 'Inter', sans-serif !important;
            font-size: {font_size}px !important;
            border-radius: var(--radius-lg) !important;
        }}

        [data-testid="stChatInputContainer"] {{
            border-radius: var(--radius-xl) !important;
            border: 1px solid rgba(255,255,255,0.07) !important;
            background: rgba(255,255,255,0.022) !important;
            backdrop-filter: blur(12px) !important;
            transition: border-color var(--transition-base) var(--ease-out),
                        box-shadow   var(--transition-base) var(--ease-out) !important;
        }}

        [data-testid="stChatInputContainer"]:focus-within {{
            border-color: rgba(255,133,51,0.38) !important;
            box-shadow: 0 0 0 3px rgba(255,133,51,0.09) !important;
        }}

        /* ════════════════════════════════════════════════════════════
           DIVIDERS
        ════════════════════════════════════════════════════════════ */
        hr {{
            border: none !important;
            height: 1px !important;
            background: linear-gradient(90deg,
                transparent, var(--border-subtle), transparent) !important;
            margin: 14px 0 !important;
        }}

        /* ════════════════════════════════════════════════════════════
           SELECTBOX / SLIDER — sidebar controls
        ════════════════════════════════════════════════════════════ */
        [data-testid="stSelectbox"] > div,
        [data-testid="stSlider"] > div {{
            font-size: 0.82rem !important;
        }}

        /* ════════════════════════════════════════════════════════════
           DOWNLOAD BUTTON
        ════════════════════════════════════════════════════════════ */
        [data-testid="stDownloadButton"] button {{
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.82rem !important;
            border-radius: var(--radius-sm) !important;
            transition:
                transform  var(--transition-fast) var(--ease-spring),
                box-shadow var(--transition-fast) var(--ease-out) !important;
        }}

        [data-testid="stDownloadButton"] button:hover {{
            transform: translateY(-2px) !important;
        }}

        /* ════════════════════════════════════════════════════════════
           SPINNER
        ════════════════════════════════════════════════════════════ */
        [data-testid="stSpinner"] {{
            font-family: 'Inter', sans-serif !important;
            color: var(--text-secondary) !important;
        }}

        /* ════════════════════════════════════════════════════════════
           DESKTOP & LAPTOP RESPONSIVENESS
        ════════════════════════════════════════════════════════════ */
        /* Large desktop (1920px+) */
        @media (min-width: 1920px) {{
            .block-container {{
                max-width: 1100px !important;
                margin: 0 auto !important;
                padding-left: 2rem !important;
                padding-right: 2rem !important;
                padding-top: 1rem !important;
            }}
            .stChatMessage {{
                max-width: 75% !important;
            }}
            .zb-hero-title {{
                font-size: 3.6rem !important;
            }}
            .zb-hero-icon {{
                font-size: 8.5rem;
            }}
            .zb-hero-sub {{
                font-size: 1.1rem !important;
            }}
        }}
        /* Desktop (1440px–1919px) */
        @media (min-width: 1440px) and (max-width: 1919px) {{
            .block-container {{
                max-width: 1000px !important;
                margin: 0 auto !important;
                padding-left: 1.5rem !important;
                padding-right: 1.5rem !important;
            }}
            .stChatMessage {{
                max-width: 78% !important;
            }}
        }}
        /* Small desktop / Laptop (1280px–1439px) */
        @media (min-width: 1280px) and (max-width: 1439px) {{
            .block-container {{
                max-width: 920px !important;
                margin: 0 auto !important;
                padding-left: 1.2rem !important;
                padding-right: 1.2rem !important;
            }}
            .stChatMessage {{
                max-width: 82% !important;
            }}
        }}
        /* Sidebar width + hero spacing on desktop */
        @media (min-width: 1280px) {{
            [data-testid="stSidebar"] {{
                width: 310px !important;
            }}
            .zb-hero {{
                padding: 30px 0 16px;
            }}
        }}

        /* ════════════════════════════════════════════════════════════
           MOBILE RESPONSIVENESS
        ════════════════════════════════════════════════════════════ */
        @media (max-width: 768px) {{
            html {{
                -webkit-text-size-adjust: 100%;
            }}

            /* ── General layout ─────────────────────────── */
            .block-container {{
                padding-left: 0.75rem !important;
                padding-right: 0.75rem !important;
                padding-top: 0.5rem !important;
            }}

            /* Ensure sidebar toggle button (▶) is visible and tappable */
            [data-testid="collapsedControl"] {{
                color: var(--text-secondary) !important;
                background: rgba(255,255,255,0.04) !important;
                border: 1px solid var(--border-subtle) !important;
                border-radius: 0 10px 10px 0 !important;
                min-width: 44px !important;
                min-height: 48px !important;
                font-size: 1.2rem !important;
                z-index: 999 !important;
            }}
            [data-testid="collapsedControl"]:hover {{
                background: rgba(255,133,51,0.15) !important;
                border-color: var(--border-brand) !important;
                color: var(--brand-secondary) !important;
            }}

            /* Sidebar overlay on mobile — full width drawer */
            [data-testid="stSidebar"] {{
                width: 100vw !important;
                max-width: 100vw !important;
                padding: 0 1rem !important;
            }}

            /* Force 2-column grids to single column */
            [data-testid="column"] {{
                min-width: 100% !important;
                flex: 0 0 100% !important;
                max-width: 100% !important;
                padding-left: 0 !important;
                padding-right: 0 !important;
            }}

            /* ── Top bar ────────────────────────────────── */
            .zb-topbar {{
                flex-wrap: wrap;
                gap: 6px;
                padding: 10px 12px;
                min-height: auto;
                margin-bottom: 14px;
                margin-left: 6px;
                margin-right: 6px;
            }}
            .zb-topbar-left {{
                gap: 6px;
            }}
            .zb-topbar-right {{
                flex-wrap: wrap;
                gap: 6px;
                width: 100%;
            }}
            .zb-topbar-icon {{
                font-size: 1rem;
            }}
            .zb-topbar-name {{
                font-size: 0.8rem !important;
            }}
            .zb-topbar-sep {{
                display: none;
            }}
            .zb-topbar-sub {{
                display: none;
            }}
            .zb-chip, .zb-chip-model, .zb-chip-live {{
                font-size: 0.7rem !important;
                padding: 6px 12px !important;
                min-height: 36px;
            }}

            /* ── Welcome section ────────────────────────── */
            .zb-welcome-title {{
                font-size: 1.25rem !important;
                line-height: 1.3 !important;
            }}
            .zb-welcome-sub {{
                font-size: 0.85rem !important;
                line-height: 1.5 !important;
            }}
            .zb-welcome-items {{
                gap: 4px 14px;
            }}
            .zb-welcome-item {{
                font-size: 0.8rem !important;
                line-height: 1.5 !important;
            }}
            .zb-welcome-tagline {{
                font-size: 0.85rem !important;
            }}

            /* ── Hero / empty state ─────────────────────── */
            .zb-hero {{
                padding: 8px 0 0;
            }}
            .zb-hero-title {{
                font-size: 1.8rem !important;
                line-height: 1.15 !important;
            }}
            .zb-hero-icon {{
                font-size: 4rem;
                margin-bottom: 10px;
            }}
            .zb-hero-sub {{
                font-size: 0.85rem !important;
                line-height: 1.5 !important;
                padding: 0 4px;
                margin-bottom: 16px;
            }}
            .zb-hero-badge-wrap {{
                margin-bottom: 24px;
            }}
            .zb-hero-badge {{
                font-size: 0.7rem !important;
                padding: 7px 16px;
                white-space: nowrap;
                min-height: 36px;
            }}

            /* ── Suggestion cards ───────────────────────── */
            .zb-card {{
                padding: 14px 16px;
                margin-bottom: 10px;
                border-radius: var(--radius-md);
            }}
            .zb-card-emoji {{
                font-size: 1.3rem;
                margin-bottom: 6px;
            }}
            .zb-card-title {{
                font-size: 0.85rem !important;
                line-height: 1.3 !important;
            }}
            .zb-card-desc {{
                font-size: 0.75rem !important;
                line-height: 1.45 !important;
            }}
            .stButton > button {{
                min-height: 44px !important;
                font-size: 0.8rem !important;
            }}

            /* ── Chat bubbles ───────────────────────────── */
            .stChatMessage {{
                padding: 1rem 1.2rem !important;
                margin-bottom: 0.8rem !important;
                border-radius: var(--radius-md) !important;
                line-height: 1.6 !important;
                word-wrap: break-word !important;
                overflow-wrap: break-word !important;
            }}
            .stChatMessage p {{
                line-height: 1.6 !important;
                margin-bottom: 0.5rem;
            }}

            /* ── Metric badges inside bubbles ───────────── */
            .zb-bubble-metrics {{
                gap: 5px;
                margin-top: 8px;
                padding-top: 8px;
            }}
            .zb-badge {{
                font-size: 0.62rem !important;
                padding: 4px 8px;
                min-height: 28px;
            }}

            /* ── Sidebar ────────────────────────────────── */
            .zb-sidebar-brand {{
                padding-top: 0.6rem;
            }}
            .zb-logo-icon {{
                width: 32px;
                height: 32px;
                font-size: 1.05rem;
            }}
            .zb-logo-text strong {{
                font-size: 0.95rem !important;
            }}
            .zb-logo-text span {{
                font-size: 0.65rem !important;
            }}
            .zb-section-label {{
                font-size: 0.68rem !important;
                margin-bottom: 10px;
            }}
            .zb-conv-item {{
                padding: 10px 12px;
            }}
            .zb-conv-title-text {{
                font-size: 0.82rem !important;
            }}
            .zb-conv-meta {{
                font-size: 0.65rem !important;
            }}
            .zb-conv-group-label {{
                font-size: 0.62rem !important;
                padding: 8px 0 4px;
            }}
            .zb-no-convs {{
                font-size: 0.76rem !important;
                padding: 14px 0;
            }}
            .zb-tip-row {{
                padding: 10px 12px;
                min-height: 44px;
                font-size: 0.76rem !important;
                line-height: 1.4 !important;
            }}
            .stButton > button {{
                min-height: 44px !important;
            }}
            [data-testid="stSelectbox"] > div,
            [data-testid="stSlider"] > div {{
                font-size: 0.85rem !important;
                min-height: 44px !important;
            }}

            /* ── Chat input ─────────────────────────────── */
            [data-testid="stChatInput"] textarea {{
                font-size: 0.95rem !important;
                min-height: 48px !important;
                line-height: 1.5 !important;
            }}
            [data-testid="stChatInputContainer"] {{
                position: sticky !important;
                bottom: 0 !important;
                background: rgba(9,9,12,0.98) !important;
                backdrop-filter: blur(16px) !important;
                z-index: 100 !important;
                padding: 10px 6px !important;
                margin-bottom: 0 !important;
                border-top: 1px solid var(--border-subtle) !important;
            }}

            /* ── Floating food — subtle on mobile ───────── */
            .zb-food-item {{
                opacity: 0.025 !important;
                font-size: 2.2rem !important;
            }}
            body:hover .zb-food-item {{
                opacity: 0.04 !important;
            }}

            /* ── Dividers ───────────────────────────────── */
            hr {{
                margin: 12px 0 !important;
            }}
        }}

        /* Medium-small devices (480px and below) */
        @media (max-width: 480px) {{
            .block-container {{
                padding-left: 0.6rem !important;
                padding-right: 0.6rem !important;
            }}
            .zb-welcome-title {{
                font-size: 1.1rem !important;
            }}
            .zb-welcome-sub {{
                font-size: 0.78rem !important;
            }}
            .zb-welcome-items {{
                flex-direction: column;
                align-items: center;
                gap: 2px;
            }}
            .zb-welcome-item {{
                font-size: 0.75rem !important;
            }}
            .zb-welcome-tagline {{
                font-size: 0.78rem !important;
            }}
            .zb-sidebar-brand {{
                padding-top: 0.4rem;
            }}
            .zb-logo-icon {{
                width: 30px;
                height: 30px;
                font-size: 0.9rem;
            }}
            .zb-logo-text strong {{
                font-size: 0.85rem !important;
            }}
            .zb-logo-text span {{
                font-size: 0.6rem !important;
            }}
            .stChatMessage {{
                padding: 0.85rem 1rem !important;
                margin-bottom: 0.7rem !important;
            }}
            [data-testid="stChatInputContainer"] {{
                padding: 8px 4px !important;
            }}
            .zb-hero-badge {{
                white-space: normal;
            }}
        }}

        /* Extra small devices (400px and below) */
        @media (max-width: 400px) {{
            .block-container {{
                padding-left: 0.5rem !important;
                padding-right: 0.5rem !important;
                padding-top: 0.3rem !important;
            }}
            .zb-hero {{
                padding: 4px 0 0;
            }}
            .zb-hero-title {{
                font-size: 1.4rem !important;
            }}
            .zb-hero-icon {{
                font-size: 3rem;
                margin-bottom: 6px;
            }}
            .zb-hero-sub {{
                font-size: 0.75rem !important;
                margin-bottom: 12px;
            }}
            .zb-hero-badge {{
                font-size: 0.6rem !important;
                padding: 5px 12px;
                min-height: 32px;
            }}
            .zb-hero-badge-wrap {{
                margin-bottom: 18px;
            }}
            .zb-grid-label {{
                font-size: 0.65rem !important;
                margin-bottom: 10px;
            }}
            .zb-chip, .zb-chip-model, .zb-chip-live {{
                font-size: 0.6rem !important;
                padding: 5px 10px !important;
                min-height: 30px;
            }}
            .zb-card {{
                padding: 12px 14px;
                margin-bottom: 8px;
            }}
            .zb-card-title {{
                font-size: 0.78rem !important;
            }}
            .zb-card-desc {{
                font-size: 0.68rem !important;
            }}
            .stChatMessage {{
                padding: 0.75rem 0.9rem !important;
                margin-bottom: 0.6rem !important;
            }}
            .zb-badge {{
                font-size: 0.55rem !important;
                padding: 3px 7px;
                min-height: 24px;
            }}
            .stButton > button {{
                min-height: 40px !important;
                font-size: 0.75rem !important;
            }}
            .zb-tip-row {{
                font-size: 0.7rem !important;
                padding: 8px 10px;
                min-height: 38px;
            }}
            .zb-conv-title-text {{
                font-size: 0.78rem !important;
            }}
            [data-testid="stChatInput"] textarea {{
                font-size: 0.9rem !important;
                min-height: 44px !important;
            }}
        }}

        /* Very small devices (320px) */
        @media (max-width: 360px) {{
            .block-container {{
                padding-left: 0.35rem !important;
                padding-right: 0.35rem !important;
            }}
            .zb-hero-title {{
                font-size: 1.2rem !important;
            }}
            .zb-hero-icon {{
                font-size: 2.5rem;
            }}
            .zb-hero-sub {{
                font-size: 0.7rem !important;
            }}
            .zb-card {{
                padding: 10px 10px;
            }}
            .zb-card-title {{
                font-size: 0.72rem !important;
            }}
            .zb-card-desc {{
                font-size: 0.62rem !important;
            }}
            .stChatMessage {{
                padding: 0.65rem 0.8rem !important;
            }}
            .zb-section-label {{
                font-size: 0.62rem !important;
            }}
            .zb-tip-row {{
                font-size: 0.65rem !important;
                padding: 6px 8px;
                min-height: 36px;
            }}
            .stButton > button {{
                min-height: 38px !important;
                font-size: 0.7rem !important;
            }}
            [data-testid="stChatInput"] textarea {{
                font-size: 0.85rem !important;
                min-height: 40px !important;
            }}
            [data-testid="stChatInputContainer"] {{
                padding: 6px 3px !important;
            }}
            .zb-topbar {{
                padding: 8px 8px;
            }}
        }}

        /* ════════════════════════════════════════════════════════════
           CONVERSATION HISTORY — Sidebar list
        ════════════════════════════════════════════════════════════ */
        .zb-conv-search {{
            width: 100%;
            padding: 8px 12px;
            background: rgba(255,255,255,0.03);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-sm);
            color: var(--text-primary);
            font-family: 'Inter', sans-serif;
            font-size: 0.78rem;
            outline: none;
            transition: border-color var(--transition-base) var(--ease-out);
            box-sizing: border-box;
            margin-bottom: 6px;
        }}
        .zb-conv-search:focus {{
            border-color: rgba(255,133,51,0.38);
            box-shadow: 0 0 0 3px rgba(255,133,51,0.09);
        }}
        .zb-conv-search::placeholder {{
            color: var(--text-muted);
        }}
        .zb-conv-group-label {{
            font-size: 0.60rem !important;
            font-weight: 700 !important;
            color: var(--text-muted) !important;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            padding: 6px 0 4px;
            display: block;
        }}
        .zb-conv-item {{
            display: block;
            width: 100%;
            padding: 8px 10px;
            margin-bottom: 2px;
            background: rgba(255,255,255,0.014);
            border: 1px solid rgba(255,255,255,0.03);
            border-radius: var(--radius-sm);
            cursor: pointer;
            transition: background var(--transition-fast) var(--ease-out),
                        border-color var(--transition-fast) var(--ease-out);
            text-align: left;
            font-family: 'Inter', sans-serif;
            color: var(--text-secondary);
            font-size: 0.76rem !important;
        }}
        .zb-conv-item:hover {{
            background: rgba(255,75,75,0.05);
            border-color: rgba(255,75,75,0.12);
        }}
        .zb-conv-item.active {{
            background: rgba(255,75,75,0.07);
            border-color: var(--border-brand);
        }}
        .zb-conv-title-text {{
            font-weight: 600;
            color: var(--text-primary);
            font-size: 0.78rem !important;
            display: block;
            margin-bottom: 2px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        .zb-conv-meta {{
            font-size: 0.62rem !important;
            color: var(--text-muted);
            display: flex;
            gap: 8px;
        }}
        .zb-conv-actions {{
            display: flex;
            gap: 4px;
            margin-top: 3px;
        }}
        .zb-conv-action-btn {{
            background: none;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            font-size: 0.65rem;
            padding: 1px 4px;
            border-radius: 4px;
            transition: color var(--transition-fast) var(--ease-out);
            font-family: 'Inter', sans-serif;
        }}
        .zb-conv-action-btn:hover {{
            color: var(--brand-secondary);
        }}
        .zb-conv-rename-input {{
            width: 100%;
            padding: 4px 8px;
            background: rgba(255,255,255,0.04);
            border: 1px solid var(--border-brand);
            border-radius: 6px;
            color: var(--text-primary);
            font-family: 'Inter', sans-serif;
            font-size: 0.76rem;
            outline: none;
            box-sizing: border-box;
        }}
        .zb-no-convs {{
            font-size: 0.72rem !important;
            color: var(--text-muted);
            text-align: center;
            padding: 12px 0;
        }}

        /* ════════════════════════════════════════════════════════════
           FOLLOW-UP QUESTIONS
        ════════════════════════════════════════════════════════════ */
        .zb-followup-section {{
            margin-top: 6px;
            padding-top: 8px;
            border-top: 1px solid rgba(255,255,255,0.05);
        }}
        .zb-followup-label {{
            font-size: 0.68rem !important;
            color: var(--text-muted);
            font-weight: 600;
            letter-spacing: 0.04em;
            text-transform: uppercase;
            margin-bottom: 5px;
            display: block;
        }}
        .zb-followup-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4px;
        }}
        .zb-followup-btn {{
            font-family: 'Inter', sans-serif;
            font-size: 0.72rem !important;
            font-weight: 500 !important;
            padding: 5px 8px;
            background: rgba(255,255,255,0.025);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-sm);
            color: var(--text-secondary) !important;
            cursor: pointer;
            text-align: left;
            transition: background var(--transition-fast) var(--ease-out),
                        border-color var(--transition-fast) var(--ease-out),
                        color var(--transition-fast) var(--ease-out);
            line-height: 1.3;
        }}
        .zb-followup-btn:hover {{
            background: rgba(255,133,51,0.08);
            border-color: rgba(255,133,51,0.22);
            color: var(--brand-secondary) !important;
        }}

        /* ════════════════════════════════════════════════════════════
           CHAT ACTIONS — Copy, Regenerate
        ════════════════════════════════════════════════════════════ */
        .zb-chat-actions {{
            display: flex;
            gap: 4px;
            margin-top: 4px;
            opacity: 0;
            transition: opacity var(--transition-fast) var(--ease-out);
        }}
        .stChatMessage:hover .zb-chat-actions {{
            opacity: 1;
        }}
        .zb-chat-action-btn {{
            display: inline-flex;
            align-items: center;
            gap: 3px;
            padding: 3px 8px;
            font-size: 0.65rem !important;
            font-weight: 500 !important;
            color: var(--text-muted);
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 6px;
            cursor: pointer;
            font-family: 'Inter', sans-serif;
            transition: background var(--transition-fast) var(--ease-out),
                        color var(--transition-fast) var(--ease-out),
                        border-color var(--transition-fast) var(--ease-out);
        }}
        .zb-chat-action-btn:hover {{
            color: var(--brand-secondary);
            background: rgba(255,133,51,0.06);
            border-color: rgba(255,133,51,0.16);
        }}
        .zb-chat-action-btn.copied {{
            color: var(--green-glow);
            border-color: rgba(74,222,128,0.2);
            background: rgba(74,222,128,0.06);
        }}

        /* ════════════════════════════════════════════════════════════
           STATISTICS — Sidebar
        ════════════════════════════════════════════════════════════ */
        .zb-stat-detail-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4px;
        }}
        .zb-stat-detail-item {{
            padding: 6px 8px;
            background: rgba(255,255,255,0.014);
            border: 1px solid rgba(255,255,255,0.03);
            border-radius: 6px;
        }}
        .zb-stat-detail-value {{
            font-family: 'Sora', sans-serif;
            font-size: 0.95rem !important;
            font-weight: 700 !important;
            color: var(--text-primary);
            display: block;
            line-height: 1.1;
        }}
        .zb-stat-detail-label {{
            font-size: 0.58rem !important;
            color: var(--text-muted);
            font-weight: 500;
            letter-spacing: 0.03em;
            text-transform: uppercase;
        }}

        /* ════════════════════════════════════════════════════════════
           KEYBOARD SHORTCUT HINT
        ════════════════════════════════════════════════════════════ */
        .zb-kbd-hint {{
            font-size: 0.60rem !important;
            color: var(--text-muted);
            text-align: center;
            padding: 4px 0;
            letter-spacing: 0.02em;
        }}
        .zb-kbd-hint kbd {{
            display: inline-block;
            padding: 1px 5px;
            font-size: 0.58rem;
            font-family: 'Inter', monospace;
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 4px;
            color: var(--text-secondary);
        }}

        /* Responsive: single column + always-visible actions on mobile */
        @media (max-width: 768px) {{
            .zb-followup-grid {{
                grid-template-columns: 1fr;
            }}
            .zb-followup-btn {{
                min-height: 44px;
                font-size: 0.76rem !important;
                padding: 8px 10px;
                line-height: 1.4;
            }}
            .zb-chat-actions {{
                opacity: 1;
            }}
            .zb-chat-action-btn {{
                min-height: 36px;
                padding: 6px 10px;
                font-size: 0.7rem !important;
            }}
            [data-testid="stSidebar"] > div:first-child {{
                padding-bottom: 80px !important;
            }}
        }}
        @media (max-width: 480px) {{
            .zb-followup-grid {{
                grid-template-columns: 1fr;
            }}
            .zb-followup-btn {{
                min-height: 42px;
                font-size: 0.72rem !important;
                padding: 6px 10px;
            }}
            .zb-chat-actions {{
                opacity: 1;
            }}
            .zb-chat-action-btn {{
                min-height: 34px;
                padding: 5px 8px;
                font-size: 0.65rem !important;
            }}
        }}
        </style>

        <script>
        function zbScrollToBottom() {{
            window.scrollTo({{ top: document.body.scrollHeight, behavior: 'smooth' }});
            var main = document.querySelector('section.main');
            if (main) main.scrollTop = main.scrollHeight;
        }}
        document.addEventListener('DOMContentLoaded', function() {{
            setTimeout(zbScrollToBottom, 80);
            setTimeout(zbScrollToBottom, 400);
        }});
        var zbObserver = new MutationObserver(zbScrollToBottom);
        document.addEventListener('DOMContentLoaded', function() {{
            var target = document.querySelector('section.main') || document.body;
            zbObserver.observe(target, {{ childList: true, subtree: true, characterData: true }});
        }});
        </script>
        """,
        unsafe_allow_html=True
    )
