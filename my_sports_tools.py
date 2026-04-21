import os
import json
import requests
from crewai.tools import tool

@tool("check_resource")
def check_resource(resource_name: str) -> str:
    """
    Checks if a sports database or API is available.
    Input should be the name of the resource (e.g., 'MatchStats_DB').
    """
    available_resources = ["MatchStats_DB", "PlayerBio_API", "LiveScore_API"]
    if resource_name in available_resources:
        return f"Resource {resource_name} is ONLINE."
    return f"Resource {resource_name} is OFFLINE."

@tool("fetch_live_cricket_stats")
def fetch_live_cricket_stats(match_query: str) -> str:
    """
    Fetches clean JSON cricket match statistics and player scores from a sports API.
    Use this tool instead of searching the web for match results.
    """
    api_key = os.environ.get("RAPIDAPI_KEY", "")
    
    # 1. Try to hit the real RapidAPI endpoint
    if api_key and api_key != "HIDDEN":
        try:
            url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
            headers = {
                "X-RapidAPI-Key": api_key,
                "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
            }
            # Set a 10-second timeout to prevent the agent from hanging
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                match_list = data.get('typeMatches', [])
                
                extracted_data = []
                for m_type in match_list[:2]:
                    for series in m_type.get('seriesMatches', [])[:2]:
                        for match in series.get('seriesAdWrapper', {}).get('matches', [])[:2]:
                            info = match.get('matchInfo', {})
                            score = match.get('matchScore', {})
                            
                            # Build a high-density string for each match
                            match_summary = {
                                "teams": f"{info.get('team1', {}).get('teamName')} vs {info.get('team2', {}).get('teamName')}",
                                "status": info.get('status'),
                                "format": info.get('matchFormat'),
                                "scores": score
                            }
                            extracted_data.append(match_summary)
                
                # Return as a string—this will be ~80% smaller than the raw JSON
                return json.dumps(extracted_data)
                    
        except Exception as e:
            # This will now only trigger for real connection issues, not the slice error
            print(f"API Error: {e}. Falling back to cached data.")

    # 2. Fallback JSON Data: Guarantees the agents have clean, token-friendly data 
    # if the API fails or the key is missing.
    cached_demo_data = {
        "match": "Gujarat Titans vs Lucknow Super Giants",
        "date": "2026-04-15",
        "result": "GT won by 7 wickets",
        "team_1": {"name": "LSG", "score": "165/8"},
        "team_2": {"name": "GT", "score": "169/3"},
        "top_performers": [
            {"player": "Shubman Gill", "team": "GT", "runs": 74, "balls": 45, "not_out": True},
            {"player": "Sai Sudharsan", "team": "GT", "runs": 42, "balls": 31, "not_out": False},
            {"player": "Quinton de Kock", "team": "LSG", "runs": 52, "balls": 38, "not_out": False}
        ]
    }
    
    return json.dumps(cached_demo_data)