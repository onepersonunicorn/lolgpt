# LoLGPT MCP — League of Legends Mock Match Simulator

⚔️ **"Who would win — you or your friend?"**

LoLGPT(롤지피티) is a remote MCP server that turns real League of Legends match
history into entertainment. Give it two Riot IDs and it simulates a full mock
match with a phase-by-phase broadcast; give it one and it profiles your
playstyle like a personality test.

Powered by live Riot Games data (last 10 games: KDA, damage, win rate) via the
[1tier.xyz](https://1tier.xyz) backend. Supports 9 languages.

## Tools

| Tool | What it does |
|---|---|
| `league_of_legends_summoner_vs_match` | Fetches both summoners' recent stats and generates a 9-phase Summoner's Rift mock match with a winner. Params: `uidA/tagA/uidB/tagB`, `lang` |
| `analyze_summoner_playstyle` | Personality-style play type, signature champion, and champions that fit or clash with your style. Params: `uid/tag`, `lang` |
| `get_mock_match_win_rankings` | Global leaderboard of accumulated mock-match wins. Params: `top` (1-20) |

Languages: `EN, 한국어, 繁體中文, 簡體中文, 日本語, ESPAÑOL, বাংলা, ਪੰਜਾਬੀ, Tiếng Việt`

**Example prompts**

> "Hide on bush#KR1이랑 Zeus#KR1 모의 경기 돌려줘"
> "내 계정 GamerTag#NA1 플레이 스타일 분석해줘"
> "롤지피티 모의전 승리 랭킹 보여줘"

## Run locally

```bash
pip install -r requirements.txt

# stdio (Claude Desktop 등 로컬 클라이언트)
python main.py

# Streamable HTTP — PORT 설정 시 활성화
PORT=8000 python main.py
# → MCP endpoint: http://localhost:8000/mcp
# → health check:  http://localhost:8000/health (GET / 도 200 응답)
```

MCP Inspector로 점검: `npx @modelcontextprotocol/inspector` → Streamable HTTP →
`http://localhost:8000/mcp`

## Deploy — PlayMCP in KC (Git 소스 빌드)

이 저장소는 KC 요건에 맞춰져 있습니다: 루트 `Dockerfile`이 **8000 포트에서
Streamable HTTP로 listen**하고(`ENV PORT=8000`), `GET /`·`GET /health`가 200을
반환합니다. stateless(no session)라 재시작·스케일링에 안전합니다.

1. https://playmcp.kakaocloud.io → **+ 새 MCP 서버 등록 → Git 소스 빌드**
2. 입력값
   - Git URL: `https://github.com/onepersonunicorn/lolgpt`
   - 브랜치: `main` · Dockerfile 경로: `Dockerfile` · PAT: 비움(public)
   - 환경변수: 불필요 (선택: `LOL_API_URL`, 기본 `https://1tier.xyz`)
   - 컨테이너 포트: `8000` (기본값)
3. Status **Active** 확인 → 상세의 **Endpoint URL** 복사 → PlayMCP 콘솔 등록에 사용

> 과거 Failed 원인: 이전 Dockerfile(Smithery 생성)이 stdio 전용이라 컨테이너가
> 포트를 열지 않았음. 현재 Dockerfile로 해결됨.

Render 등 다른 PaaS도 동일하게 동작합니다(PaaS가 `PORT`를 주입).

## PlayMCP 등록 정보 (복사용)

**서비스 설명 (국문)**

> ⚔️ 친구와 나, 누가 이길까? — 롤지피티(LoLGPT)
>
> 실제 라이엇 전적 데이터(최근 10경기 KDA·딜량·승률)로 두 소환사의 가상 대결을
> 9단계 실황 중계처럼 시뮬레이션합니다. 소환사명 두 개면 "밴픽부터 넥서스까지"
> 승부가 갈리고, 하나면 내 플레이 성향(플레이 타입 · 인생 챔피언 · 나와 맞는/
> 상극인 챔피언)을 성격 테스트처럼 분석해 줍니다.
>
> 이런 대화에서 호출됩니다:
> · "페이커랑 내 계정으로 모의 경기 돌려줘"
> · "내 소환사명 ○○○#KR1 플레이 스타일 분석해줘"
> · "모의전 승리 랭킹 1위가 누구야?"
>
> 결과는 짧은 마크다운 요약으로 반환되어 대화 흐름을 끊지 않으며, 9개 언어를
> 지원합니다. 전적 조회를 넘어 "전적으로 노는" 새로운 경험을 제공합니다.

**Service description (EN)**

> Turn match history into entertainment. LoLGPT(롤지피티) simulates a mock
> League of Legends match between any two summoners using their real last-10-
> games stats (KDA, damage, win rate), narrated phase by phase — or profiles a
> single summoner's playstyle with a signature champion and champion
> recommendations. Ask "run a mock match between me and Faker" and get a
> winner. 9 languages, concise markdown output, stateless remote MCP.

## Disclaimer

Mock match simulations are for entertainment purposes only. League of Legends
is a trademark of Riot Games, Inc. This project is not endorsed by Riot Games.

MIT License
