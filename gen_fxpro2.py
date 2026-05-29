import json
with open('/projects/sandbox/KIRO/FXPRO-REVIEW-2026.json') as f:
    r = json.load(f)
r.update({
  "account_types": [
    {"name": "Standard", "min_deposit": "$100", "spread_pips": "1.2 avg EUR/USD", "commission_per_lot_rt": "$0", "all_in_cost_eurusd": "$12.00", "leverage": "1:30 (FCA/CySEC) / 1:500 (SCB)", "source": "broker-stated"},
    {"name": "Raw+ (Raw Spread)", "min_deposit": "$100", "spread_pips": "0.0 avg EUR/USD", "commission_per_lot_rt": "$7.00", "all_in_cost_eurusd": "$7.00", "leverage": "1:30 (FCA/CySEC) / 1:500 (SCB)", "source": "broker-stated"},
    {"name": "cTrader", "min_deposit": "$100", "spread_pips": "0.2 avg EUR/USD", "commission_per_lot_rt": "$7.00 ($35 per million)", "all_in_cost_eurusd": "$9.00", "leverage": "1:30 (FCA/CySEC) / 1:500 (SCB)", "source": "broker-stated"},
    {"name": "Islamic (Swap-Free)", "min_deposit": "$100", "spread_pips": "1.2 avg EUR/USD", "commission_per_lot_rt": "$0", "all_in_cost_eurusd": "$12.00", "leverage": "1:30 / 1:500", "source": "broker-stated"}
  ],
  "platforms": ["MetaTrader 4", "MetaTrader 5", "cTrader", "FxPro Edge (Proprietary Web/Mobile)", "FxPro Mobile App"],
  "payment_methods": ["Visa", "Mastercard", "Wire Transfer", "Skrill", "Neteller", "PayPal"],
  "payment_method_details": [
    {"method": "Visa/Mastercard", "min": "$100", "processing": "Instant", "fee": "$0"},
    {"method": "Wire Transfer", "min": "$100", "processing": "1-3 business days", "fee": "$0"},
    {"method": "Skrill/Neteller", "min": "$100", "processing": "Instant", "fee": "$0"},
    {"method": "PayPal", "min": "$100", "processing": "Instant", "fee": "$0"}
  ],
  "pros": [
    "FCA and CySEC regulated with London headquarters — strong Tier-1 oversight",
    "Raw+ account offers 0.0 pips EUR/USD + $3.50 per side — genuinely competitive ECN pricing",
    "cTrader available alongside MT4 and MT5 — rare triple-platform offering",
    "NDD execution with sub-12ms speeds — excellent for scalpers and algo traders",
    "2,100+ instruments across forex, shares, indices, commodities, crypto, and futures CFDs",
    "Zero fees on deposits and withdrawals across all methods"
  ],
  "cons": [
    "Standard account spreads of 1.2 pips EUR/USD are wider than many competitors",
    "$15/month inactivity fee after 6 months of no trading — more aggressive than some",
    "Does not accept US, Iran, or Canadian residents",
    "Education resources are limited compared to AvaTrade or IG",
    "75% retail loss rate — above the industry average of ~72%",
    "VIP account requires $50,000 minimum deposit — out of reach for most retail traders"
  ]
})
with open('/projects/sandbox/KIRO/FXPRO-REVIEW-2026.json', 'w') as f:
    json.dump(r, f, indent=2)
print("part2 done")
