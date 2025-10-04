import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        
        * {
            font-family: 'Poppins', sans-serif !important;
        }
        
        .stApp {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        }
        
        .main .block-container {
            background: transparent;
            padding-top: 2rem;
        }
        
        section[data-testid="stSidebar"],
        [data-testid="stHeader"] {
            background: transparent;
        }
        
        .main, .main p, .main span, .main div {
            color: #e0e0e0;
        }
        
        .main h1, .main h2, .main h3, .main h4, .main h5, .main h6 {
            color: #ffffff;
        }
        
        .main .element-container p {
            color: #e0e0e0;
        }
        
        .stAlert * {
            color: #ffffff !important;
        }
        
        .main-header {
            font-size: 3.5rem;
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            margin-bottom: 1rem;
            animation: fadeIn 1s ease-in, float 3s ease-in-out infinite;
            letter-spacing: -1px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5), 0 0 20px rgba(255,255,255,0.3);
            background: linear-gradient(135deg, #ff6b6b 0%, #ffa500 50%, #ffd700 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        @keyframes shimmer {
            0% { background-position: -1000px 0; }
            100% { background-position: 1000px 0; }
        }
        
        .stButton>button {
            width: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-weight: 600;
            border-radius: 12px;
            padding: 0.75rem 1.5rem;
            border: none;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            font-size: 1rem;
            letter-spacing: 0.5px;
            position: relative;
            overflow: hidden;
        }
        
        .stButton>button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.5s;
        }
        
        .stButton>button:hover::before {
            left: 100%;
        }
        
        .stButton>button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
        }
        
        .stButton>button:active {
            transform: translateY(-1px);
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        }
        
        .success-box {
            padding: 1rem;
            border-radius: 10px;
            background-color: #d4edda;
            border-left: 5px solid #28a745;
            margin: 1rem 0;
            animation: slideIn 0.5s ease-out;
        }
        
        .info-box {
            padding: 1rem;
            border-radius: 10px;
            background-color: #d1ecf1;
            border-left: 5px solid #17a2b8;
            margin: 1rem 0;
        }
        
        .error-box {
            padding: 1rem;
            border-radius: 10px;
            background-color: #f8d7da;
            border-left: 5px solid #dc3545;
            margin: 1rem 0;
        }
        
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        [data-testid="stMetricValue"] {
            font-size: 2rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        [data-testid="stMetricLabel"] {
            font-size: 0.9rem;
            font-weight: 500;
            color: #6c757d;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        div[data-testid="stMetricDelta"] {
            font-size: 0.85rem;
        }
        
        [data-testid="metric-container"] {
            background: linear-gradient(135deg, #1e293b 0%, #2d3748 100%);
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            border: 1px solid rgba(102, 126, 234, 0.3);
            transition: all 0.3s ease;
        }
        
        [data-testid="metric-container"]:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
            border-color: rgba(102, 126, 234, 0.6);
        }
        
        .streamlit-expanderHeader {
            background: linear-gradient(135deg, #1e293b 0%, #2d3748 100%);
            border-radius: 12px;
            font-weight: 600;
            font-size: 1.1rem;
            padding: 1rem 1.5rem;
            border: 2px solid #2d3748;
            transition: all 0.3s ease;
            color: #e0e0e0;
        }
        
        .streamlit-expanderHeader:hover {
            border-color: #667eea;
            background: linear-gradient(135deg, #2d3748 0%, #374151 100%);
        }
        
        details[open] .streamlit-expanderHeader {
            border-bottom-left-radius: 0;
            border-bottom-right-radius: 0;
            border-color: #667eea;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        
        .streamlit-expanderContent {
            border: 2px solid #667eea;
            border-top: none;
            border-bottom-left-radius: 12px;
            border-bottom-right-radius: 12px;
            padding: 1.5rem;
            background: #1a1a2e;
            color: #e0e0e0;
        }
        
        .dataframe {
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            background: #1e293b;
        }
        
        .dataframe thead tr th {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            font-weight: 600;
            padding: 12px;
        }
        
        .dataframe tbody tr {
            background-color: #1e293b;
            color: #e0e0e0;
        }
        
        .dataframe tbody tr:hover {
            background-color: #2d3748;
        }
        
        .dataframe tbody td {
            color: #e0e0e0;
            border-color: #2d3748;
        }
        
        [data-testid="stDataFrame"] {
            background: #1e293b;
            border-radius: 12px;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background: transparent;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 55px;
            border-radius: 12px 12px 0 0;
            padding: 12px 24px;
            font-weight: 600;
            font-size: 1rem;
            background: #1e293b;
            border: 2px solid #2d3748;
            border-bottom: none;
            transition: all 0.3s ease;
            color: #b0b0b0;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background: #2d3748;
            border-color: #667eea;
            color: #e0e0e0;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white !important;
            border-color: #667eea;
            box-shadow: 0 -4px 15px rgba(102, 126, 234, 0.5);
        }
        
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            box-shadow: 4px 0 25px rgba(0,0,0,0.5);
            border-right: 1px solid rgba(102, 126, 234, 0.3);
        }
        
        [data-testid="stSidebar"] > div:first-child {
            padding: 2rem 1.5rem;
        }
        
        [data-testid="stSidebar"] * {
            color: #e0e0e0 !important;
        }
        
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            color: #ffffff !important;
        }
        
        [data-testid="stSidebar"] label {
            color: #b0b0b0 !important;
        }
        
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            border-radius: 10px;
            border: 2px solid #2d3748;
            background: #1e293b;
            color: #e0e0e0;
            transition: all 0.3s ease;
            padding: 0.75rem 1rem;
            font-size: 0.95rem;
        }
        
        .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
            border-color: #667eea;
            background: #2d3748;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.25);
            outline: none;
        }
        
        .stTextInput>div>div>input:hover, .stTextArea>div>div>textarea:hover {
            border-color: #667eea;
            background: #2d3748;
        }
        
        .stSelectbox>div>div, .stMultiSelect>div>div {
            border-radius: 10px;
            border: 2px solid #2d3748;
            background: #1e293b;
            transition: all 0.3s ease;
        }
        
        .stSelectbox>div>div:hover, .stMultiSelect>div>div:hover {
            border-color: #667eea;
            background: #2d3748;
        }
        
        .stNumberInput>div>div>input {
            border-radius: 10px;
            border: 2px solid #2d3748;
            background: #1e293b;
            color: #e0e0e0;
            transition: all 0.3s ease;
        }
        
        .stNumberInput>div>div>input:focus {
            border-color: #667eea;
            background: #2d3748;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.25);
        }
        
        .stCheckbox {
            padding: 0.5rem 0;
        }
        
        .stAlert {
            border-radius: 12px;
            border: none;
            padding: 1rem 1.5rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            animation: slideIn 0.5s ease;
        }
        
        div[data-baseweb="notification"][kind="info"] {
            background: linear-gradient(135deg, #17a2b8 0%, #138496 100%);
            border-left: 5px solid #0dcaf0;
        }
        
        div[data-baseweb="notification"][kind="success"] {
            background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
            border-left: 5px solid #0f5132;
        }
        
        div[data-baseweb="notification"][kind="warning"] {
            background: linear-gradient(135deg, #ffc107 0%, #ff9800 100%);
            border-left: 5px solid #ff6b00;
        }
        
        div[data-baseweb="notification"][kind="error"] {
            background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);
            border-left: 5px solid #a71d2a;
        }
        
        code {
            background: linear-gradient(135deg, #2d3748 0%, #374151 100%);
            padding: 3px 8px;
            border-radius: 6px;
            color: #667eea;
            font-family: 'Courier New', monospace;
            font-weight: 500;
            border: 1px solid #4a5568;
        }
        
        pre {
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid #2d3748;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            color: #e0e0e0;
        }
        
        pre code {
            color: #e0e0e0;
            background: transparent;
            border: none;
        }
        
        a {
            color: #8b9bff;
            text-decoration: none;
            transition: all 0.3s ease;
            font-weight: 500;
            position: relative;
        }
        
        a::after {
            content: '';
            position: absolute;
            width: 0;
            height: 2px;
            bottom: -2px;
            left: 0;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            transition: width 0.3s ease;
        }
        
        a:hover::after {
            width: 100%;
        }
        
        a:hover {
            color: #a8b5ff;
        }
        
        hr {
            margin: 2rem 0;
            border: none;
            height: 2px;
            background: linear-gradient(90deg, transparent, #667eea, transparent);
        }
        
        .stDownloadButton>button {
            background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
            color: white;
            font-weight: 600;
            border-radius: 10px;
            padding: 0.75rem 1.5rem;
            border: none;
            box-shadow: 0 4px 15px rgba(40, 167, 69, 0.3);
            transition: all 0.3s ease;
        }
        
        .stDownloadButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(40, 167, 69, 0.4);
        }
        
        .stSpinner > div {
            border-color: #667eea !important;
        }
        
        .footer {
            text-align: center;
            color: #6c757d;
            padding: 2.5rem 0;
            margin-top: 3rem;
            border-top: 3px solid transparent;
            border-image: linear-gradient(90deg, transparent, #667eea, transparent) 1;
        }
        
        ::-webkit-scrollbar {
            width: 12px;
            height: 12px;
        }
        
        ::-webkit-scrollbar-track {
            background: #1a1a2e;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #764ba2 0%, #f093fb 100%);
        }
        
        .element-container {
            animation: fadeIn 0.6s ease-in;
        }
        
        [data-baseweb="tooltip"] {
            background: linear-gradient(135deg, #2d3436 0%, #1e272e 100%);
            border-radius: 8px;
            padding: 0.5rem 1rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }
        </style>
    """, unsafe_allow_html=True)
