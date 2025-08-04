import streamlit as st
st.cache_data.clear()  # for Streamlit v1.18+
import os
import asyncio
import streamlit as st
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Gemini API setup
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="gemini-2.0-flash"
)

# Agents
Arif_Ali = Agent(
    name="Agent of Arif Ali ",
    instructions="""
You are an assistant with specific knowledge about Mr. Arif Ali.
You know:
Digita Marketing services provides a wide range of professional services including Artificial Intelligence, Web Development, SEO, Digital Marketing, Mobile Application Development, Graphic Designing, Domain & Hosting, and Software Solutions like HMS.
The company is led by CEO Arif Ali.
contact: 0311-3656644
qualification : Graduate
Living : Mr Arif Ali Living in DHA karachi
Office Address: Plot A 724,Tariq Road Karachi.
Only answer questions about Mr Arif Ali or related personal info.
""",
    model=model,
    handoff_description="personal info or identity of Arif Ali"
)

Digital_marketing = Agent(
    name="Digital Marketing",
    instructions="""
You are an assistant with specific knowledge about Digital Marketing.
You know:
Digital Marketing provides a wide range of professional services including Artificial Intelligence, Web Development, SEO, Digital Marketing, Mobile Application Development, Graphic Designing, Domain & Hosting, and Software Solutions like HMS.
The company is led by CEO Arif Ali.
contact: 0311-3656644
qualification : Graduate
Living : Mr Arif Ali Living in DHA karachi
Office Address: Plot A 724,Tariq Road Karachi.


Major services, Time Duration and Pricing:
  {
    "S. No": 1,
    "service_name": "Artificial intelligence",
    "completion_time": "3 months",
    "rate_charges": 500000
  },
  {
    "S. No": 2,
    "service_name": "Web Development or website",
    "completion_time": "1 month",
    "rate_charges": 80000
  },
  {
    "S. No": 3,
    "service_name": "SEO",
    "completion_time": "3 months",
    "rate_charges": 120000
  },
  {
    "S. No": 4,
    "service_name": "Digital marketing",
    "completion_time": "2 months",
    "rate_charges": 25000
  },
  {
    "S. No": 5,
    "service_name": "Mobile Application",
    "completion_time": "2 months",
    "rate_charges": 250000
  },
  {
    "S. No": 6,
    "service_name": "Graphic designing",
    "completion_time": "1 months",
    "rate_charges": 20000
  },
  {
    "S. No": 7,
    "service_name": "Domain And Hosting",
    "completion_time": "10 days",
    "rate_charges": 15000
  },
  {
    "S. No": 8,
    "service_name": "Software solution",
    "completion_time": "1.5 months",
    "rate_charges": 200000
  },
  {
    "S. No": 9,
    "service_name": "HMS etc",
    "completion_time": "20 days",
    "rate_charges": 15000
  }




Only answer questions about Digital MArketing or related staff info.
""",
    model=model,
    handoff_description="Digital MArketing question or concept"
)


Price = Agent(
    name="Price",
    instructions="""
You are an assistant with specific knowledge about Price.
You know:
Digital MArketing provides a wide range of professional services including Artificial Intelligence, Web Development, SEO, Digital Marketing, Mobile Application Development, Graphic Designing, Domain & Hosting, and Software Solutions like HMS.
Major services, Time Duration and Pricing:
  {
    "S. No": 1,
    "service_name": "Artificial intelligence",
    "completion_time": "3 months",
    "rate_charges": 500000
  },
  {
    "S. No": 2,
    "service_name": "Web Development or website",
    "completion_time": "1 month",
    "rate_charges": 80000
  },
  {
    "S. No": 3,
    "service_name": "SEO",
    "completion_time": "3 months",
    "rate_charges": 120000
  },
  {
    "S. No": 4,
    "service_name": "Digital marketing",
    "completion_time": "2 months",
    "rate_charges": 25000
  },
  {
    "S. No": 5,
    "service_name": "Mobile Application",
    "completion_time": "2 months",
    "rate_charges": 250000
  },
  {
    "S. No": 6,
    "service_name": "Graphic designing",
    "completion_time": "1 months",
    "rate_charges": 20000
  },
  {
    "S. No": 7,
    "service_name": "Domain And Hosting",
    "completion_time": "10 days",
    "rate_charges": 15000
  },
  {
    "S. No": 8,
    "service_name": "Software solution",
    "completion_time": "1.5 months",
    "rate_charges": 200000
  },
  {
    "S. No": 9,
    "service_name": "HMS etc",
    "completion_time": "20 days",
    "rate_charges": 15000
  }




Only answer questions about Price or related info.
""",
    model=model,
    handoff_description="Price question or concept"
)



Duration = Agent(
    name="Duration",
    instructions="""
You are an assistant with specific knowledge about Duration.
You know:
Digital MArketing provides a wide range of professional services including Artificial Intelligence, Web Development, SEO, Digital Marketing, Mobile Application Development, Graphic Designing, Domain & Hosting, and Software Solutions like HMS.
Major services, Time Duration and Pricing:
  {
    "S. No": 1,
    "service_name": "Artificial intelligence",
    "completion_time": "3 months",
    "rate_charges": 500000
  },
  {
    "S. No": 2,
    "service_name": "Web Development or website",
    "completion_time": "1 month",
    "rate_charges": 80000
  },
  {
    "S. No": 3,
    "service_name": "SEO",
    "completion_time": "3 months",
    "rate_charges": 120000
  },
  {
    "S. No": 4,
    "service_name": "Digital marketing",
    "completion_time": "2 months",
    "rate_charges": 25000
  },
  {
    "S. No": 5,
    "service_name": "Mobile Application",
    "completion_time": "2 months",
    "rate_charges": 250000
  },
  {
    "S. No": 6,
    "service_name": "Graphic designing",
    "completion_time": "1 months",
    "rate_charges": 20000
  },
  {
    "S. No": 7,
    "service_name": "Domain And Hosting",
    "completion_time": "10 days",
    "rate_charges": 15000
  },
  {
    "S. No": 8,
    "service_name": "Software solution",
    "completion_time": "1.5 months",
    "rate_charges": 200000
  },
  {
    "S. No": 9,
    "service_name": "HMS etc",
    "completion_time": "20 days",
    "rate_charges": 15000
  }




Only answer questions about Duration or related staff info.
""",
    model=model,
    handoff_description="Duration question or concept"
)

MainAgent = Agent(
    name="Gernal Assistant",
    instructions="""
You are an Gernal assistant expert.
If the question is about Arif Ali, Digital Marketing, Duration and Price  hand it off to the right agent.
""",
    model=model,
    handoffs=[ Arif_Ali, Digital_marketing, Price, Duration]
)


async def get_agent_reply(query):
    result = await Runner.run(MainAgent, query)
    return result.final_output, result.last_agent.name

# Streamlit config
st.set_page_config(page_title="Multi-Agent Chat", page_icon="🤖", layout="centered")


# 💅 Custom styling for dark background and red label/button

st.markdown("""
    <style>
    body, .stApp {
        background-color: #0a0f1f;
        color: #e6e6e6;
        font-size: 18px;
    }
    h1 {
        color: #ff4b4b;
        font-weight: bold;
    }
    label[data-testid="stTextInputLabel"] {
        color: #ff4b4b !important;
        font-weight: bold;
        font-size: 18px;
    }
    .stTextInput > div > div > input {
        background-color: #1c2333;
        color: #ffffff;
        border: 1px solid #ff4b4b;
        border-radius: 8px;
        padding: 10px;
    }.stButton > button {
    background-color: #ff4b4b;
    color: black !important;
    font-weight: bold;
    padding: 0.5em 1em;
    border-radius: 8px;
    border: none;
    font-size: 18px;
    transition: all 0.3s ease;
}
.stButton > button:hover {
    background-color: #e63946;
    color: white !important;
}

    .chat-box {
        background-color: #1a1e2b;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        font-size: 18px;
    }
    </style>
""", 
unsafe_allow_html=True)

# App Title
st.markdown("<h1>🤖 AI Assistant for Arif Ali Khan </h1>", unsafe_allow_html=True)


# Chat session state
if "chat" not in st.session_state:
    st.session_state.chat = []

# Input

with st.form("chat_form", clear_on_submit=True):
    st.markdown("<label style='color: red; font-size: 20px; font-weight: bold;'> Your Query like this:</label>", unsafe_allow_html=True)
    st.markdown("<label style='color: ; font-size: 20px; '>Q1: who is ceo of digital marketing services??</label>", unsafe_allow_html=True)
    st.markdown("<label style='color: ; font-size: 20px; '>Q2: Which services does the digital marketing service provide??</label>", unsafe_allow_html=True)
    st.markdown("<label style='color: ; font-size: 20px; '>Q3: I want to get a website made, how long will it take???</label>", unsafe_allow_html=True)
    st.markdown("<label style='color: ; font-size: 20px; '>Q4: What will be the cost of getting a website developed????</label>", unsafe_allow_html=True)
    st.markdown("<label style='color: ; font-size: 20px; '>Q5: Give me contact number of Arif Ali?????</label>", unsafe_allow_html=True)
    st.markdown("<label style='color: red; font-size: 20px; '>💬 Your Query:</label>", unsafe_allow_html=True)
    user_input = st.text_input(label="", placeholder="Type your question here...")
    submitted = st.form_submit_button("🚀 Ask")


if submitted and user_input:
    with st.spinner("Thinking..."):
        final_output, last_agent_name = asyncio.run(get_agent_reply(user_input))
        st.session_state.chat.insert(0, ("🤖 Response", f"""{final_output } """))
        st.session_state.chat.insert(0, ("🧑 You", user_input))

# Chat history
for role, msg in st.session_state.chat:
    color = "#293042" if role == "🧑 You" else "#162032"
    st.markdown(f"<div class='chat-box' style='background:{color}'><b>{role}</b>: {msg}</div>", unsafe_allow_html=True)
