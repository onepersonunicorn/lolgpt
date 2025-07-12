import os
import sys
import argparse
import json
import requests
from datetime import datetime
from mcp.server.fastmcp import FastMCP

parser = argparse.ArgumentParser(description="League of Legends Mock Match MCP Server")
parser.add_argument("--debug", action="store_true", help="Enable debug mode")
args = parser.parse_args()

mcp = FastMCP("lolgpt")

# API base URL
LOL_API_URL = os.getenv("LOL_API_URL", "https://1tier.xyz")

@mcp.tool()
async def league_of_legends_summoner_vs_match(
    uidA: str, 
    tagA: str, 
    uidB: str, 
    tagB: str, 
    lang: str = "EN"
) -> str:
    """
    Simulate a League of Legends mock match between two summoners.
    
    Args:
        uidA: Riot ID of the first summoner
        tagA: Tag of the first summoner
        uidB: Riot ID of the second summoner
        tagB: Tag of the second summoner
        lang: Language for the simulation (EN, 한국어, 繁體中文, 日本語, ESPAÑOL, বাংলা, ਪੰਜਾਬੀ)
    
    Returns:
        Detailed match simulation with summoner statistics and match progression
    """
    try:
        # Make POST request to the API
        response = requests.post(
            f"{LOL_API_URL}/vs4",
            data={
                'uidA': uidA,
                'tagA': tagA,
                'uidB': uidB,
                'tagB': tagB,
                'lang': lang
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            summoners = data.get('summoners', {})
            
            # Format the response for better readability
            result = f"""
🎮 **League of Legends Mock Match Simulation**
════════════════════════════════════════════

**📊 Summoner A ({uidA}#{tagA}) - Last 10 Games Statistics:**
• Average Kills: {summoners.get('avg_kills', 'N/A')}
• Average Assists: {summoners.get('avg_assists', 'N/A')}
• Average Deaths: {summoners.get('avg_deaths', 'N/A')}
• Average KDA: {summoners.get('avg_kda', 'N/A')}
• Average Damage Dealt: {summoners.get('avg_deal', 'N/A')}
• Win Rate: {summoners.get('win_rate', 'N/A')}%

**📊 Summoner B ({uidB}#{tagB}) - Last 10 Games Statistics:**
• Average Kills: {summoners.get('avg_kills_b', 'N/A')}
• Average Assists: {summoners.get('avg_assists_b', 'N/A')}
• Average Deaths: {summoners.get('avg_deaths_b', 'N/A')}
• Average KDA: {summoners.get('avg_kda_b', 'N/A')}
• Average Damage Dealt: {summoners.get('avg_deal_b', 'N/A')}
• Win Rate: {summoners.get('win_rate_b', 'N/A')}%

**🎯 Mock Match Simulation - Summoner's Rift:**
════════════════════════════════════════════

**Phase 1:** {summoners.get('p1', 'Loading...')}

**Phase 2:** {summoners.get('p2', 'Loading...')}

**Phase 4:** {summoners.get('p4', 'Loading...')}

**Phase 5:** {summoners.get('p5', 'Loading...')}

**Phase 6:** {summoners.get('p6', 'Loading...')}

**Phase 7:** {summoners.get('p7', 'Loading...')}

**Phase 8:** {summoners.get('p8', 'Loading...')}

**Phase 9:** {summoners.get('p9', 'Loading...')}

**Phase 10:** {summoners.get('p10', 'Loading...')}

"""
            return result
        else:
            return f"Error: Failed to fetch match simulation (Status: {response.status_code})"
            
    except requests.exceptions.RequestException as e:
        return f"Error: Failed to connect to League of Legends API - {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def lol_summoner_mock_battle(
    summoner1_id: str, 
    summoner1_tag: str, 
    summoner2_id: str, 
    summoner2_tag: str, 
    language: str = "ENGLISH"
) -> str:
    """
    Create a League of Legends mock battle simulation between two summoners.
    
    Args:
        summoner1_id: First summoner's Riot ID
        summoner1_tag: First summoner's tag
        summoner2_id: Second summoner's Riot ID
        summoner2_tag: Second summoner's tag
        language: Simulation language (ENGLISH, 한국어, etc.)
    
    Returns:
        Complete battle simulation with stats and match progression
    """
                return await league_of_legends_mock_match(
        summoner1_id, summoner1_tag, summoner2_id, summoner2_tag, language
    )

@mcp.tool()
async def league_summoner_comparison(
    player1_riot_id: str, 
    player1_tag: str, 
    player2_riot_id: str, 
    player2_tag: str, 
    output_language: str = "EN"
) -> str:
    """
    Compare two League of Legends summoners and simulate their matchup.
    
    Args:
        player1_riot_id: First player's Riot ID
        player1_tag: First player's tag
        player2_riot_id: Second player's Riot ID  
        player2_tag: Second player's tag
        output_language: Language for output (EN, 한국어, 繁體中文, 日本語, ESPAÑOL, বাংলা, ਪੰਜਾਬੀ)
    
    Returns:
        Detailed comparison and mock match simulation
    """
    return await league_of_legends_summoner_vs_match(
        player1_riot_id, player1_tag, player2_riot_id, player2_tag, output_language
    )

@mcp.tool()
async def summoners_rift_simulation(
    riot_id_a: str, 
    tag_a: str, 
    riot_id_b: str, 
    tag_b: str, 
    sim_language: str = "EN"
) -> str:
    """
    Run a Summoner's Rift simulation between two League of Legends players.
    
    Args:
        riot_id_a: Riot ID of first summoner
        tag_a: Tag of first summoner
        riot_id_b: Riot ID of second summoner
        tag_b: Tag of second summoner
        sim_language: Language for simulation text (EN, 한국어, 繁體中文, 日本語, ESPAÑOL, বাংলা, ਪੰਜਾਬੀ)
    
    Returns:
        Full Summoner's Rift match simulation with phase-by-phase breakdown
    """
    return await league_of_legends_summoner_vs_match(
        riot_id_a, tag_a, riot_id_b, tag_b, sim_language
    )

@mcp.tool()
async def lol_player_vs_player_match(
    first_summoner_id: str, 
    first_summoner_tag: str, 
    second_summoner_id: str, 
    second_summoner_tag: str, 
    match_language: str = "EN"
) -> str:
    """
    Generate a League of Legends player vs player match simulation.
    
    Args:
        first_summoner_id: First summoner's Riot ID
        first_summoner_tag: First summoner's tag
        second_summoner_id: Second summoner's Riot ID
        second_summoner_tag: Second summoner's tag
        match_language: Language for match narration (EN, 한국어, 繁體中文, 日本語, ESPAÑOL, বাংলা, ਪੰਜਾਬੀ)
    
    Returns:
        Complete PvP match simulation with statistics and battle progression
    """
    return await league_of_legends_summoner_vs_match(
        first_summoner_id, first_summoner_tag, second_summoner_id, second_summoner_tag, match_language
    )

@mcp.tool()
async def league_match_predictor(
    summoner_a_id: str, 
    summoner_a_tag: str, 
    summoner_b_id: str, 
    summoner_b_tag: str, 
    prediction_language: str = "ENGLISH"
) -> str:
    """
    Predict the outcome of a League of Legends match between two summoners.
    
    Args:
        summoner_a_id: First summoner's Riot ID
        summoner_a_tag: First summoner's tag
        summoner_b_id: Second summoner's Riot ID
        summoner_b_tag: Second summoner's tag
        prediction_language: Language for prediction output
    
    Returns:
        Match prediction with detailed analysis and simulation
    """
    return await league_of_legends_summoner_vs_match(
        summoner_a_id, summoner_a_tag, summoner_b_id, summoner_b_tag, prediction_language
    )

if __name__ == "__main__":
    mcp.run()