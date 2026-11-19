# -------------------------------------------------
# Market size & growth calculations (illustrative)
# -------------------------------------------------
us_apparel_market_2024 = 350_000_000_000          # $350 B
sustainable_share_2024 = 0.06                    # 6 %
sustainable_market_2024 = us_apparel_market_2024 * sustainable_share_2024

cagr_sustainable = 0.10                          # 10 % CAGR
years = 5                                        # 2024‑2029
sustainable_market_2029 = sustainable_market_2024 * (1 + cagr_sustainable) ** years

print(f"Sustainable apparel market 2024: ${sustainable_market_2024/1e9:.1f}B")
print(f"Projected 2029 (10% CAGR): ${sustainable_market_2029/1e9:.1f}B")