import os
import sys
import argparse
import logging

import requests
from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations
from starlette.requests import Request
from starlette.responses import JSONResponse

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description="LoLGPT MCP Server")
parser.add_argument("--debug", action="store_true", help="Enable debug mode")
args, _ = parser.parse_known_args()

if args.debug:
    logging.getLogger().setLevel(logging.DEBUG)

# Base URL of the LoLGPT backend API. Endpoint paths (/vs4, /sm4) are
# appended per tool, so this must NOT include an endpoint path.
LOL_API_URL = os.getenv("LOL_API_URL", "https://1tier.xyz").rstrip("/")
if LOL_API_URL.endswith("/vs4"):
    # Older configs (smithery.yaml, mcp.json) pointed straight at /vs4
    LOL_API_URL = LOL_API_URL[: -len("/vs4")]

# Render (and most PaaS) inject PORT; presence of PORT/RENDER selects the
# Streamable HTTP transport, otherwise stdio is kept for local clients.
PORT = int(os.getenv("PORT", "8000"))

mcp = FastMCP(
    "lolgpt",
    host="0.0.0.0",
    port=PORT,
    stateless_http=True,
    json_response=True,
)

REQUEST_TIMEOUT = 25

SUPPORTED_LANGS = "EN, 한국어, 繁體中文, 簡體中文, 日本語, ESPAÑOL, বাংলা, ਪੰਜਾਬੀ, Tiếng Việt"


@mcp.custom_route("/health", methods=["GET"])
async def health(request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok", "service": "lolgpt-mcp"})


@mcp.custom_route("/", methods=["GET"])
async def root(request: Request) -> JSONResponse:
    # 일부 플랫폼(PlayMCP in KC 등)은 컨테이너 포트의 GET / 로 헬스체크한다
    return JSONResponse({"status": "ok", "service": "lolgpt-mcp", "mcp": "/mcp"})


@mcp.tool(
    annotations=ToolAnnotations(
        title="LoL Summoner VS Mock Match",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=False,
        openWorldHint=True,
    )
)
async def league_of_legends_summoner_vs_match(
    uidA: str,
    tagA: str,
    uidB: str,
    tagB: str,
    lang: str = "EN",
) -> str:
    """Simulates a mock League of Legends match between two summoners from LoLGPT(롤지피티).

    Fetches each summoner's average stats from their last 10 games via the
    Riot Games API (kills, deaths, assists, KDA, damage, win rate) and
    generates a phase-by-phase Summoner's Rift match narrative.

    Args:
        uidA: Riot ID of the first summoner (e.g. "Hide on bush")
        tagA: Tagline of the first summoner, without "#" (e.g. "KR1")
        uidB: Riot ID of the second summoner
        tagB: Tagline of the second summoner, without "#"
        lang: Output language. One of: EN, 한국어, 繁體中文, 簡體中文, 日本語,
            ESPAÑOL, বাংলা, ਪੰਜਾਬੀ, Tiếng Việt

    Returns:
        Markdown summary with both summoners' recent stats and a 9-phase
        mock match progression.
    """
    try:
        response = requests.post(
            f"{LOL_API_URL}/vs4",
            data={
                "uidA": uidA,
                "tagA": tagA,
                "uidB": uidB,
                "tagB": tagB,
                "lang": lang,
            },
            timeout=REQUEST_TIMEOUT,
        )

        if response.status_code != 200:
            return (
                f"Error: LoLGPT API returned status {response.status_code}. "
                "Check that both Riot IDs and taglines are correct."
            )

        s = response.json().get("summoners", {})

        stats_a = (
            f"**{uidA}#{tagA}** (last 10 games): "
            f"{s.get('avg_kills', '?')}/{s.get('avg_deaths', '?')}/{s.get('avg_assists', '?')} "
            f"(K/D/A), KDA {s.get('avg_kda', '?')}, "
            f"avg damage {s.get('avg_deal', '?')}, win rate {s.get('win_rate', '?')}%"
        )
        stats_b = (
            f"**{uidB}#{tagB}** (last 10 games): "
            f"{s.get('avg_kills_b', '?')}/{s.get('avg_deaths_b', '?')}/{s.get('avg_assists_b', '?')} "
            f"(K/D/A), KDA {s.get('avg_kda_b', '?')}, "
            f"avg damage {s.get('avg_deal_b', '?')}, win rate {s.get('win_rate_b', '?')}%"
        )

        phases = []
        for i in (1, 2, 4, 5, 6, 7, 8, 9, 10):
            phase = s.get(f"p{i}")
            if phase:
                phases.append(f"{len(phases) + 1}. {phase}")

        return (
            "## LoL Mock Match Simulation\n\n"
            f"{stats_a}\n\n{stats_b}\n\n"
            "### Match Progression\n"
            + "\n".join(phases)
        )

    except requests.exceptions.Timeout:
        return "Error: LoLGPT API request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"Error: Failed to connect to LoLGPT API - {e}"
    except Exception as e:
        return f"Error: {e}"


@mcp.tool(
    annotations=ToolAnnotations(
        title="LoL Summoner Playstyle Analysis",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=False,
        openWorldHint=True,
    )
)
async def analyze_summoner_playstyle(
    uid: str,
    tag: str,
    lang: str = "EN",
) -> str:
    """Analyzes a League of Legends summoner's playstyle from LoLGPT(롤지피티).

    Based on the summoner's recent match history, returns a personality-style
    play type, a short description, the summoner's signature champion, and
    champions that suit or clash with their style.

    Args:
        uid: Riot ID of the summoner (e.g. "Hide on bush")
        tag: Tagline of the summoner, without "#" (e.g. "KR1")
        lang: Output language. One of: EN, 한국어, 繁體中文, 簡體中文, 日本語,
            ESPAÑOL, বাংলা, ਪੰਜਾਬੀ, Tiếng Việt

    Returns:
        Markdown summary of the summoner's play type, signature champion,
        and recommended/avoid champions.
    """
    try:
        response = requests.post(
            f"{LOL_API_URL}/sm4",
            data={"uidA": uid, "tagA": tag, "lang": lang},
            timeout=REQUEST_TIMEOUT,
        )

        if response.status_code != 200:
            return (
                f"Error: LoLGPT API returned status {response.status_code}. "
                "Check that the Riot ID and tagline are correct."
            )

        s = response.json().get("summoners", {})

        return (
            f"## Playstyle Analysis: {uid}#{tag}\n\n"
            f"- **Play type:** {s.get('mbti', '?')}\n"
            f"- **Profile:** {s.get('desc', '?')}\n"
            f"- **Signature champion:** {s.get('champ', '?')}\n"
            f"- **Fits your style:** {s.get('gcham', '?')} — {s.get('good', '?')}\n"
            f"- **Clashes with your style:** {s.get('bcham', '?')} — {s.get('bad', '?')}"
        )

    except requests.exceptions.Timeout:
        return "Error: LoLGPT API request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"Error: Failed to connect to LoLGPT API - {e}"
    except Exception as e:
        return f"Error: {e}"


def main() -> None:
    try:
        if os.getenv("PORT") or os.getenv("RENDER"):
            logger.info(
                f"Starting LoLGPT MCP Server (Streamable HTTP) on 0.0.0.0:{PORT} "
                f"with API URL: {LOL_API_URL}"
            )
            mcp.run(transport="streamable-http")
        else:
            logger.info(f"Starting LoLGPT MCP Server (stdio) with API URL: {LOL_API_URL}")
            mcp.run()
    except Exception as e:
        logger.error(f"Failed to start MCP server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
