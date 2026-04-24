# Polity5 - Processed Dataset

**Source:** Polity5 Project, Center for Systemic Peace
**Original file:** `p5v2018.xls` (dataset version 2018)
**Reference:** Marshall, Monty G. (2020). *POLITY5: Political Regime Characteristics and Transitions, 1800–2018. Dataset Users' Manual.* Center for Systemic Peace.

## Coverage

| | |
|---|---|
| Years | 1776–2018 (2019–2020 available for the United States only) |
| Countries | 195 unique polities (including historical/defunct states) |
| Observations | 17,574 country-years |

## Standardized Authority Codes

Several variables use special numeric codes instead of regular scores when normal coding is not applicable:

| Code | Label | Meaning |
|------|-------|---------|
| `-66` | Interruption | Foreign occupation or short-lived federation; old polity terminated |
| `-77` | Interregnum | Complete collapse of central authority (state failure / anarchy) |
| `-88` | Transition | New institutions being planned/enacted; authority patterns in flux |

`polity2` converts these to usable numeric values (see below) and should be preferred for quantitative analysis.

## Fields

### Identifiers

| Column | Type | Description |
|--------|------|-------------|
| `ccode` | int | **COW Numeric Country Code.** Three-digit code from the Correlates of War (COW) interstate system. Use this to merge with other COW datasets (MID, CINC, etc.). |
| `scode` | str | **COW Alpha Country Code.** Three-letter abbreviation from the COW system (e.g. `USA`, `RUS`). |
| `iso3c` | str | **ISO 3166-1 alpha-3 code.** Added during processing for easier merging with non-COW datasets. `null` for historical or defunct states (e.g. USSR, Prussia, Yugoslavia). |
| `country` | str | **Country name.** Standardized name as used in Polity5. |
| `year` | int | **Year coded.** Codes reflect the regime in place on **31 December** of that year. |

### Composite Democracy / Autocracy Indices

| Column | Range | Description |
|--------|-------|-------------|
| `polity2` | −10 to +10 | **Revised Combined Polity Score.** The primary summary measure. Computed as `democ − autoc`, with standardized authority codes converted: −66 → missing; −77 → 0; −88 → prorated linearly across the transition span. **Use this column for regression and time-series analysis.** Regimes are conventionally classified as: full democracy (+6 to +10), partial democracy/anocracy (−5 to +5), autocracy (−10 to −6). |
| `democ` | 0–10 (or −66/−77/−88) | **Institutionalized Democracy index.** Additive score derived from executive recruitment competitiveness (`exrec`), executive constraints (`exconst`), and political competition (`polcomp`). Higher = more democratic. |
| `autoc` | 0–10 (or −66/−77/−88) | **Institutionalized Autocracy index.** Additive score derived from the same component variables with different weights. Higher = more autocratic. Note: `democ` and `autoc` are not mutually exclusive - a regime can score on both (anocracy). |

### Concept Variables (Authority Typologies)

These are composite re-codings of the underlying component variables that capture authority typologies as discrete categories.

#### `exrec` - Executive Recruitment Concept
Range: 1–8 (or −66/−77/−88)

Synthesizes how the chief executive comes to power (`xrreg`, `xrcomp`, `xropen`) into eight ordered categories:

| Value | Label | Description |
|-------|-------|-------------|
| 1 | Ascription | Succession by hereditary birthright |
| 2 | Ascription + Designation | Hereditary ruler plus a court-designated chief minister |
| 3 | Designation | Informal competition within the political elite |
| 4 | Self-Selection | Seizure of power (coup, revolution) |
| 5 | Gradual Transition from Self-Selection | Post-coup transitional arrangements toward regularized succession |
| 6 | Ascription + Election | Hereditary ruler plus an elected chief minister |
| 7 | Transitional or Restricted Election | Elections with significant restrictions or incumbent advantages |
| 8 | Competitive Election | Open competitive elections; power transfers follow electoral results |

#### `exconst` - Executive Constraints Concept
Range: 1–7 (or −66/−77/−88)

Extent to which accountability groups (legislature, ruling party, military, judiciary) institutionally constrain the chief executive's decision-making:

| Value | Label |
|-------|-------|
| 1 | Unlimited authority |
| 2 | Intermediate |
| 3 | Slight to moderate limitations |
| 4 | Intermediate |
| 5 | Substantial limitations |
| 6 | Intermediate |
| 7 | Executive parity or subordination |

#### `polcomp` - Political Competition Concept
Range: 1–10 (or −66/−77/−88)

Synthesizes the regulation (`parreg`) and competitiveness (`parcomp`) of political participation into ten ordered categories:

| Value | Label | Description |
|-------|-------|-------------|
| 1 | Suppressed | No organized competition; totalitarian/despotic control |
| 2 | Restricted | Some competition but major groups/types systematically excluded |
| 3 | Imposed Transition (loosening) | Restrictions being relaxed under elite direction |
| 4 | Uninstitutionalized | Fluid, no enduring national organizations; personality-based |
| 5 | Gradual Transition from Uninstitutionalized | Nascent, ad hoc party structures emerging |
| 6 | Factional/Restricted | Parochial factions compete with systematic exclusions |
| 7 | Factional | Ethnic/parochial factions compete; particularist agendas dominate |
| 8 | Electoral Transition: Persistent Conflict | Moving toward competitive elections but with significant coercion |
| 9 | Electoral Transition: Limited Conflict | Moving toward competitive elections with minor coercion |
| 10 | Institutionalized Electoral | Stable secular parties; regular voluntary transfers of power |

### Regime Transition Variables

Populated only in years when a regime change occurs; blank otherwise.

| Column | Type | Description |
|--------|------|-------------|
| `d5` | 0/1 | **Regime Transition Completed.** `1` marks the final year of a regime change (whether single-year or spanning multiple years). Use this flag to isolate transition events. |
| `sf` | 0/1 | **State Failure.** `1` in every year the polity is in complete collapse of central authority (interregnum, −77) or has undergone state disintegration. |
| `regtrans` | int | **Regime Transition Category.** Classifies the nature of the change when `d5=1`. Also carries the special codes −66, 96, 97, 98, 99 (see below). |

**`regtrans` values:**

| Value | Label |
|-------|-------|
| +3 | Major Democratic Transition - ≥6-point increase in `polity`, crossing into partial or full democracy |
| +2 | Minor Democratic Transition - 3–5-point increase crossing a regime boundary |
| +1 | Positive Regime Change - ≥3-point increase without a regime-type shift |
| 0 | Little or No Change |
| −1 | Negative Regime Change - 3–5-point decrease |
| −2 | Adverse Regime Transition - ≥6-point decrease, or interregnum (−77) |
| −77 | State Failure - complete collapse of central political authority |
| −66 | Interruption - foreign occupation or short-lived federation |
| 96 | State Disintegration - territorial breakup producing successor states |
| 97 | State Transformation - borders substantially changed; authority regime continuous |
| 98 | State Demise - voluntary dissolution or absorption into another state |
| 99 | State Creation - year of independence or formation |
