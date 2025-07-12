from setuptools import setup

setup(
    name="lolgpt",
    version="1.0.0",
    description="AI-powered League of Legends professional esports match predictor and summoner analysis tool. Predict outcomes for T1, Faker, Zeus, and other pro players with advanced statistical modeling.",
    author="lolGPT Team",
    author_email="faker@1tier.xyz",
    url="https://github.com/onepersonunicorn/lolgpt",
    py_modules=["main"],
    install_requires=[
        "fastmcp>=0.1.0",
        "requests>=2.28.0",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "lolgpt=main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.12",
    ],
    keywords = ["mcp", "league-of-legends", "lol", "summoner", "mock-match", "simulation", "esports", "gaming", "riot-games", "summoners-rift", "prediction", "pvp", "comparison", "professional-gaming", "t1", "faker", "zeus", "lck", "lcs", "worlds", "msi", "pro-player", "esports-analytics", "competitive-lol", "team-analysis", "player-stats", "tournament-prediction"],
)