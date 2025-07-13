import os
import sys
import argparse
import json
import requests
from datetime import datetime
import asyncio
import logging
from mcp.server.fastmcp import FastMCP

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description="League of Legends Mock Match MCP Server")
parser.add_argument("--debug", action="store_true", help="Enable debug mode")
args = parser.parse_args()

if args.debug:
    logging.getLogger().setLevel(logging.DEBUG)

mcp = FastMCP("lolgpt")

# API base URL
LOL_API_URL = os.getenv("LOL_API_URL", "https://1tier.xyz")

logger.info(f"Starting LoL Mock Match MCP Server with API URL: {LOL_API_URL}")

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

if __name__ == "__main__":
    try:
        logger.info("Starting LoL Mock Match MCP Server...")
        mcp.run()
    except Exception as e:
        logger.error(f"Failed to start MCP server: {e}")
        sys.exit(1)