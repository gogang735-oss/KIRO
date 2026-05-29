import json
review = {
  "name": "FxPro",
  "slug": "fxpro",
  "type": "forex",
  "founded_year": 2006,
  "headquarters": "London, United Kingdom",
  "website_url": "https://www.fxpro.com",
  "logo_url": "",
  "description": "FxPro is a London-headquartered NDD broker founded in 2006, regulated by FCA, CySEC, FSCA, and SCB, offering 2,100+ instruments via MT4, MT5, cTrader, and its proprietary FxPro Edge platform to clients in 170+ countries.",
  "regulation": ["FCA (UK)", "CySEC (Cyprus)", "FSCA (South Africa)", "SCB (Bahamas)"],
  "license_number": "509956",
  "min_deposit": "$100",
  "leverage": "1:30",
  "avg_spread": "0.0 pips (Raw+) / 1.2 pips (Standard)",
  "score": 7.8,
  "stars": 3.9
}
with open('/projects/sandbox/KIRO/FXPRO-REVIEW-2026.json', 'w') as f:
    json.dump(review, f, indent=2)
print("base written")
