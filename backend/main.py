from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from parser import extract_profile

from recommender import recommend_schemes

from models import UserProfile, ChatRequest
from groq_service import get_scheme_recommendation

app=FastAPI()

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


@app.post("/recommend")
def recommend(chat: ChatRequest):

    profile_dict = extract_profile(chat.message)

    profile = UserProfile(**profile_dict)

    matched = recommend_schemes(profile)

    ai_result = get_scheme_recommendation(profile_dict, matched)

    return {
    "profile": profile_dict,
    "matched_schemes": matched,
    "ai_response": ai_result
}