# A Causal Analysis of the Relationship between Democracies, Civil Liberties, and Women's Rights under the Law

## About

This project uses historical panel data to investigate whether changes in a country's level of democracy and civil liberties causally precede improvements in women's legal rights, or whether the relationship runs in the opposite direction - or both.

The primary analytical tool is Granger causality testing applied country-by-country across a 48-year panel (1971–2018, 174 countries). Democracy and civil liberties variables from Polity5 and V-Dem are tested as predictors of women's legal rights from the World Bank's Women, Business and the Law (WBL) dataset, and the reverse direction is tested as well. The asymmetry between the two directions provides evidence about the likely causal ordering.

This project is motivated in part by Behr et al. (2024), *Empowering Change* (World Bank Policy Research Working Paper 10788), which establishes correlational evidence that democracy and civil society are associated with legal gender equality but explicitly stops short of causal claims. See [`references/`](references/README.md).

---

## Abstract

This study applies data science and causal analysis methods to understand if improvements in democracy and civil liberties drive women's legal rights, or the relationship runs the other way. By bringing together computational methods and social science theory, this work exemplifies the kind of interdisciplinary collaboration between social and computational science.

Using panel data from 174 countries over 48 years (1971–2018), we combine Granger causality testing and Panel Fixed Effects regression to assess the direction and strength of this relationship while controlling for stable country characteristics such as legal tradition and colonial history. The analysis integrates four large international datasets that cover democracy, civil participation, legal gender equality, and religious composition.

Results show that democracy and civil liberties changes precede improvements in women's legal rights significantly. Women's parliamentary representation becomes the strongest predictor, with a special impact on marriage law and parenthood rights. The pattern holds across regions and religious contexts. Analysis shows that not only democracy is important, also freedom of association and the participation of civil society organizations contributes to the increase in women's rights legal adoption.

---

## Sources

| Dataset | Coverage | Use in this project |
|---------|----------|---------------------|
| [Polity5](datasets/README.md#political-regime-characteristics-and-transitions-18002018) | 195 polities, 1776–2018 | Democracy/autocracy scores (treatment) |
| [V-Dem v16](datasets/README.md#v-dem-dataset) | 202 polities, 1789–2025 | Fine-grained democracy, civil liberties, and women's empowerment indices |
| [World Bank WBL](datasets/README.md#women-business-and-the-law-10-data-for-19712024) | 190 economies, 1971–2024 | Legal rights for women across 8 areas (outcome) |
| [Pew Research Center RDI](datasets/README.md#religious-composition-by-country-2010-2050) | 230 countries, 2010 snapshot | Religious composition and fractionalization (control) |

Raw datasets and their full documentation: [`datasets/`](datasets/README.md)

Processed/cleaned versions: [`processed-datasets/`](processed-datasets/)

---

## Integrated Democracy–Women's Rights Panel

**File:** `processed-datasets/merged/democracy_wbl_rdi.csv`

**8,561 rows × 101 columns** - 174 countries, years 1971–2018.

This is the main analytical dataset, produced by merging Polity5, V-Dem, WBL, and the Pew RDI into a single country-year panel. The merge key is `curr_iso3` - the ISO 3166-1 alpha-3 code of the current (or principal successor) state.

### Country Continuity: Handling Dissolutions, Unifications, and Secessions

ISO 3166-1 only assigns codes to currently existing countries, while Polity5 and V-Dem track historical and now-defunct polities. To produce a consistent panel, historical entities were mapped to a current ISO3 as follows:

**Unifications** - the unified successor's post-unification series is replicated once per predecessor, each replica carrying that predecessor's ccode. Combined with the predecessor's own pre-unification data, every predecessor gets a complete continuous series - with `curr_iso3` set to the successor for all rows:

| Predecessors | Unified state | Year |
|---|---|---|
| Germany East + Germany West | Germany (DEU) | 1990 |
| Vietnam North + South Vietnam | Vietnam (VNM) | 1976 |
| Yemen North + Yemen South | Yemen (YEM) | 1990 |

**Dissolutions** - the predecessor's full historical series is replicated once per successor, each replica labeled with that successor's ISO3. This gives every successor a complete series that includes the predecessor's pre-dissolution observations followed by its own post-independence observations:

| Historical polity | Successors (each gets a full replicated series) |
|---|---|
| USSR | Russia (RUS), + 14 independent republics |
| Yugoslavia | Serbia (SRB), Slovenia (SVN), Croatia (HRV), Bosnia (BIH), Macedonia (MKD), Montenegro (MNE) |
| Czechoslovakia | Czech Republic (CZE), Slovakia (SVK) |
| Serbia and Montenegro | Serbia (SRB), Montenegro (MNE) |

As a result, a time series for (for example) Serbia covers Yugoslavia's pre-dissolution observations and Serbia's post-independence observations as a single continuous series under `curr_iso3 = SRB`.

### Identifiers

| Field | Description | Range / Values |
|---|---|---|
| `ts_id` | Unique time-series ID in format `{ccode}_{ISO3}` | string |
| `orig_ccode` | Original Polity5 numeric country code | 2–950 |
| `orig_country` | Country name as it appears in the original Polity5 dataset | string |
| `country` | Canonical country name | string |
| `curr_iso3` | Current ISO 3166-1 alpha-3 country code (merge key) | 174 unique codes |
| `curr_country` | Current country name matching `curr_iso3` | string |
| `year` | Year of observation | 1971–2018 |

---

### Polity5 Variables (`p_` prefix)

Democracy/autocracy scores from the [Polity5 project](https://www.systemicpeace.org/polityproject.html).

> **Special codes:** Several Polity5 fields use the values −88 (transition/interregnum period - no coherent authority), −77 (interruption - foreign interruption of governance), and −66 (periods of interregnum) as missing-data indicators rather than numeric scores. These should be treated as NaN in analysis. `p_regtrans` uses 99 for interregnum and −77/−66 for interruption/interregnum codes.

| Field | Description | Range / Values |
|---|---|---|
| `p_polity2` | Combined Polity score (democracy minus autocracy) | −10 (full autocracy) to +10 (full democracy) |
| `p_democ` | Institutionalized democracy score | 0–10 (−88 = special code) |
| `p_autoc` | Institutionalized autocracy score | 0–10 (−88 = special code) |
| `p_exrec` | Executive recruitment concept score | 1–8 (−88 = special code) |
| `p_exconst` | Executive constraints (decision-making) score | 1–7 (−88 = special code) |
| `p_polcomp` | Political competition/participation score | 0–10 (−88 = special code) |
| `p_d5` | Flag: observation uses a Polity special code (interruption, interregnum, or transition) | 1 (when flagged), else null |
| `p_sf` | State failure indicator | 1 (when flagged), else null |
| `p_regtrans` | Regime transition type | 0–3, −2, 99, −77 (special codes) |

---

### V-Dem Variables (`v_` prefix)

Continuous indices from the [V-Dem project](https://www.v-dem.net/).

#### Core Democracy Indices

All indices below are on a **0–1 scale** (higher = more democratic / more constrained / more equal). Observed ranges in this dataset are shown.

| Field | Description | Observed Range |
|---|---|---|
| `v_v2x_polyarchy` | Electoral democracy index | 0.009–0.922 |
| `v_v2x_libdem` | Liberal democracy index | 0.005–0.896 |
| `v_v2x_partipdem` | Participatory democracy index | 0.006–0.808 |
| `v_v2x_delibdem` | Deliberative democracy index | 0.004–0.887 |
| `v_v2x_egaldem` | Egalitarian democracy index | 0.013–0.885 |
| `v_v2x_cspart` | Civil society participation index | 0.014–0.987 |
| `v_v2x_frassoc_thick` | Freedom of association index | 0.015–0.950 |
| `v_v2x_freexp_altinf` | Freedom of expression and alternative information index | 0.009–0.988 |
| `v_v2x_suffr` | Share of population with suffrage rights | 0–1 |
| `v_v2xlg_legcon` | Legislative constraints on the executive | 0.020–0.987 |
| `v_v2x_jucon` | Judicial constraints on the executive | 0.004–0.991 |
| `v_v2x_corr` | Political corruption index (higher = more corrupt) | 0.002–0.970 |
| `v_v2x_rule` | Rule of law index | 0.008–0.998 |
| `v_v2xeg_eqprotec` | Equal protection index | 0.005–0.986 |
| `v_v2xeg_eqaccess` | Equal access index | 0.014–0.981 |
| `v_v2xeg_eqdr` | Equal distribution of resources index | 0.016–0.986 |

#### Gender-Specific Indices

Indices marked **0–1** follow the standard V-Dem scale. Indices marked **z-score** are latent variable estimates on an interval scale centered near 0 - higher values indicate better conditions for women, lower values indicate worse.

| Field | Description | Scale | Observed Range |
|---|---|---|---|
| `v_v2x_gender` | Women's political empowerment index | 0–1 | 0.040–0.961 |
| `v_v2x_gencl` | Women's civil liberties index | 0–1 | 0.000–0.981 |
| `v_v2x_gencs` | Women's civil society participation index | 0–1 | 0.008–0.933 |
| `v_v2x_genpp` | Women's political participation index | 0–1 | 0.050–1.000 |
| `v_v2xpe_exlgender` | Political exclusion by gender (higher = more exclusion) | 0–1 | 0.014–0.988 |
| `v_v2lgfemleg` | Percentage of female legislators | % | 0–63.8% |
| `v_v2mefemjrn` | Percentage of female journalists | % | 0.5–67% |
| `v_v2cldmovew` | Freedom of domestic movement for women | z-score | −4.65 to +2.71 |
| `v_v2clslavef` | Freedom from forced labor for women | z-score | −4.22 to +3.01 |
| `v_v2clprptyw` | Property rights for women | z-score | −3.82 to +3.29 |
| `v_v2cldiscw` | Freedom from discrimination for women | z-score | −3.54 to +3.47 |
| `v_v2pepwrgen` | Power distributed by gender | z-score | −2.82 to +3.57 |
| `v_v2peapsgen` | Approval of political system by gender | z-score | −2.80 to +3.15 |
| `v_v2peasjgen` | Access to state justice by gender | z-score | −2.98 to +3.50 |
| `v_v2peasbgen` | Access to basic services by gender | z-score | −2.41 to +3.52 |
| `v_v2csgender` | Civil society women's participation | z-score | −3.22 to +2.66 |

---

### World Bank WBL Variables

From the [Women, Business and the Law](https://wbl.worldbank.org/) dataset. Binary fields are `True`/`False`; composite scores are 0–100.

#### Classification

| Field | Description | Values |
|---|---|---|
| `Region` | World Bank region | East Asia & Pacific, Europe & Central Asia, High income: OECD, Latin America & Caribbean, Middle East & North Africa, South Asia, Sub-Saharan Africa |
| `Income Group` | World Bank income group | High income, Upper middle income, Lower middle income, Low income, Not classified |

#### Composite Scores (0–100)

Each sub-index is the average of its constituent binary indicators × 100. Higher = more legal equality.

| Field | Description | Observed Range |
|---|---|---|
| `wbl_index` | Overall WBL index - average of the 8 sub-indices below | 17.5–100 |
| `mobility` | Mobility sub-index | 0–100 |
| `workplace` | Workplace sub-index | 0–100 |
| `pay` | Pay sub-index | 0–100 |
| `marriage` | Marriage sub-index | 0–100 |
| `parenthood` | Parenthood sub-index | 0–100 |
| `entrepreneurship` | Entrepreneurship sub-index | 0–100 |
| `assets` | Assets sub-index | 0–100 |
| `pension` | Pension sub-index | 0–100 |

#### Mobility

| Field | Description | Values |
|---|---|---|
| `woman_choose_residence` | Woman can choose where to live in the same way as a man | True / False |
| `woman_travel_outside_home` | Woman can travel outside her home in the same way as a man | True / False |
| `woman_apply_passport` | Woman can apply for a passport in the same way as a man | True / False |
| `woman_travel_abroad` | Woman can travel abroad in the same way as a man | True / False |

#### Workplace

| Field | Description | Values |
|---|---|---|
| `woman_get_job` | Woman can get a job in the same way as a man | True / False |
| `law_prohibits_gender_discrimination` | Law prohibits gender-based discrimination in employment | True / False |
| `law_sexual_harassment` | Law on sexual harassment in employment exists | True / False |
| `penalties_sexual_harassment` | Criminal penalties or civil remedies for sexual harassment in employment | True / False |
| `woman_work_night` | Woman can work night jobs in the same way as a man | True / False |
| `woman_work_dangerous` | Woman can work in jobs deemed dangerous in the same way as a man | True / False |
| `woman_work_industrial` | Woman can work in industrial jobs in the same way as a man | True / False |

#### Pay

| Field | Description | Values |
|---|---|---|
| `law_equal_pay` | Law mandates equal remuneration for work of equal value | True / False |

#### Marriage

| Field | Description | Values |
|---|---|---|
| `no_obey_husband_law` | No law requires a woman to obey her husband | True / False |
| `woman_head_household` | Woman can be head of household in the same way as a man | True / False |
| `law_domestic_violence` | Law on domestic violence exists | True / False |
| `woman_divorce_rights` | Woman has the same rights to divorce as a man | True / False |
| `woman_remarry_rights` | Woman has the same rights to remarry as a man | True / False |

#### Parenthood

| Field | Description | Values |
|---|---|---|
| `paid_maternity_leave_14weeks` | At least 14 weeks of paid maternity leave | True / False |
| `paid_maternity_leave_length` | Length of paid maternity leave | 0–455 days |
| `govt_pays_maternity_leave` | Government administers 100% of maternity leave benefits | True / False |
| `paid_paternity_leave` | Paid paternity leave exists | True / False |
| `paid_paternity_leave_length` | Length of paid paternity leave | 0–90 days |
| `paid_parental_leave` | Paid parental leave exists | True / False |
| `parental_leave_shared_days` | Shared parental leave days available | 0–1,460 days |
| `parental_leave_mother_days` | Parental leave days reserved for the mother | 0–478 days |
| `parental_leave_father_days` | Parental leave days reserved for the father | 0–365 days |
| `protect_pregnant_workers` | Prohibition on dismissal of pregnant workers | True / False |

#### Entrepreneurship

| Field | Description | Values |
|---|---|---|
| `law_credit_gender_discrimination` | Law prohibits gender-based discrimination in access to credit | True / False |
| `woman_sign_contract` | Woman can sign a contract in the same way as a man | True / False |
| `woman_register_business` | Woman can register a business in the same way as a man | True / False |
| `woman_open_bank_account` | Woman can open a bank account in the same way as a man | True / False |

#### Assets

| Field | Description | Values |
|---|---|---|
| `equal_property_rights` | Sons and daughters have equal inheritance rights | True / False |
| `equal_inheritance_children` | Female and male surviving spouses have equal inheritance rights | True / False |
| `equal_inheritance_spouses` | Male and female children have equal inheritance rights from their parents | True / False |
| `equal_asset_admin_marriage` | Law grants spouses equal administrative authority over assets during marriage | True / False |
| `value_nonmonetary_contributions` | Law provides for the valuation of nonmonetary contributions | True / False |

#### Pension

| Field | Description | Values |
|---|---|---|
| `equal_pension_age_full` | Retirement age for full pension benefits is the same for men and women | True / False |
| `equal_pension_age_partial` | Retirement age for partial pension benefits is the same for men and women | True / False |
| `equal_retirement_age` | Mandatory retirement age is the same for men and women | True / False |
| `pension_credit_childcare` | Periods of childcare are accounted for in pension benefits | True / False |

---

### Religious Diversity Variables (Pew Research)

From the [Pew Research Center Global Religious Diversity](https://www.pewresearch.org/religion/2014/04/04/global-religious-diversity/) study. These are static (one value per country, replicated across all years).

| Field | Description | Range / Values |
|---|---|---|
| `rdi` | Religious Diversity Index - higher values indicate greater diversity in religious composition | 0–9 (theoretical max: 10; observed max in dataset: 9) |
| `dominant_religion` | The largest religious group in the country | `christian`, `muslim`, `unaffiliated`, `hindu`, `buddhist`, `folk`, `jewish` |

---

## Results: Granger Causality

### Methodology

Granger causality tests were run country-by-country using `statsmodels.tsa.stattools.grangercausalitytests`. Both series are **first-differenced** before testing to address the non-stationarity common to panel indices with on-going trends. Lags of 1–4 years are tested; each country-pair's result is summarized by the minimum p-value across lags. Country-pairs with fewer than 20 usable observations are excluded.

**Note:** Each time series is identified by a country-pair (`ccode_ISO3`) rather than a single country code, because unifications and dissolutions produce multiple series sharing the same `curr_iso3`.

Results are aggregated across countries in two ways: the **% of countries** where the test is significant at p < 0.05 (share of countries showing the pattern), and **Fisher's combined p-value** (pooled evidence across all countries).

Six democracy/civil liberties predictors are tested against nine WBL outcomes (8 sub-indices + overall WBL index), in both directions.

### Forward Direction: Democracy / Civil Liberties → Women's Legal Rights

Democracy and civil liberties variables consistently Granger-cause future changes in women's legal rights. The table below shows, for each WBL outcome, the mean % of countries significant across all 6 predictors and the single predictor with the strongest signal.

| WBL Target | Mean % sig | Max % sig | Strongest predictor |
|---|---|---|---|
| Pension | 29.6% | 34.3% | Liberal Democracy |
| Parenthood | 29.1% | 35.8% | Liberal Democracy |
| Mobility | 25.9% | 28.6% | Freedom of Association |
| WBL Index | 20.1% | 23.5% | Electoral Democracy |
| Pay | 20.0% | 30.3% | Electoral Democracy |
| Assets | 19.2% | 23.9% | Rule of Law |
| Workplace | 17.3% | 20.3% | Polity2 |
| Entrepreneurship | 16.7% | 21.2% | Rule of Law |
| Marriage | 15.2% | 18.0% | Polity2 |

The strongest forward signals are for **Pension** and **Parenthood** (liberal democracy as the best predictor), followed by **Mobility** (freedom of association). **Marriage** is the least Granger-caused by democracy indicators, possibly reflecting stronger influence of social and religious norms in that domain.

### Reverse Direction: Women's Legal Rights → Democracy / Civil Liberties

The same tests were run in reverse - testing whether past changes in WBL sub-indices predict future changes in democracy or civil liberties.

| WBL Predictor | Mean % sig | Max % sig | Strongest democracy target |
|---|---|---|---|
| Parenthood | 17.1% | 19.8% | Polity2 |
| Mobility | 17.0% | 21.7% | Polity2 |
| Assets | 17.0% | 21.9% | Liberal Democracy |
| Pension | 15.7% | 17.8% | Freedom of Expression |
| Pay | 15.7% | 19.3% | Electoral Democracy |
| Entrepreneurship | 15.1% | 19.5% | Freedom of Association |
| WBL Index | 13.8% | 16.1% | Liberal Democracy |
| Marriage | 11.5% | 15.2% | Freedom of Expression |
| Workplace | 9.8% | 13.2% | Polity2 |

The reverse signals are **consistently weaker** than the forward direction. Across all WBL sub-indices, the mean % of countries significant in the reverse direction ranges from 9.8% to 17.1%, compared to 15.2%–29.6% in the forward direction. This asymmetry supports the interpretation that democracy and civil liberties changes tend to **precede** improvements in women's legal rights, rather than the reverse.

The aggregate WBL index shows a mean of 13.8% reverse significance vs. 20.1% forward - a roughly 1.5× gap. Individual sub-indices follow the same pattern, with **Workplace** being the area of most extreme asymmetry (9.8% reverse vs. 17.3% forward).

---

## Results: Panel Fixed Effects Regression

### Methodology

Panel Fixed Effects (FE) regressions were run for all combinations of 10 predictors × 9 WBL targets × 4 lags (1–4 years), yielding 360 regressions per direction. Each regression includes country fixed effects (absorbing stable country characteristics) and year fixed effects (absorbing global time trends). Both the predictor and target are first-differenced to focus on within-country changes.

The 10 predictors are: Polity2, Electoral Democracy, Liberal Democracy, Freedom of Association, Freedom of Expression, Rule of Law (the 6 core democracy/civil liberties indices) plus Civil Society, Female Legislators, Women Political Empowerment, and Women Civil Society.

### Forward Direction: Democracy / Civil Liberties → Women's Legal Rights

**62.2% of forward regressions are significant at p < 0.05**, with all coefficients among the top 20 being positive. Results at lag 4, averaged across all 10 predictors:

| WBL Target | Mean coef | % Significant | Strongest predictor |
|---|---|---|---|
| Workplace | 0.237 | 100% | Female Legislators |
| Pay | 0.205 | 90% | Female Legislators |
| Entrepreneurship | 0.181 | 100% | Female Legislators |
| WBL Index | 0.130 | 100% | Women Political Empower |
| Assets | 0.131 | 50% | Female Legislators |
| Marriage | 0.123 | 60% | Female Legislators |
| Parenthood | 0.081 | 40% | Women Political Empower |
| Mobility | 0.062 | 40% | Female Legislators |
| Pension | 0.017 | 10% | - |

**Female Legislators is the single strongest predictor overall**: a 10 percentage point increase in women's share of parliament predicts a 3.8 pp improvement in marriage law rights the following year (coef = 0.380, t = 6.73).

### Reverse Direction: Women's Legal Rights → Democracy / Civil Liberties

**40.3% of reverse regressions are significant**, compared to 62.2% forward - confirming the asymmetry found in the Granger analysis. Key contrasts:

- **Workplace: 100% forward, 10% reverse** - the clearest one-directional result.
- **Pay/Entrepreneurship: 90-100% forward, ~60% reverse** - a genuine virtuous cycle, but with the forward channel dominant.
- **Pension: 10% forward, 0% reverse** - structurally inert in both directions.

### Granger vs Panel FE: Complementary Pictures

The two methods rank WBL targets differently because they capture different phenomena:

| | Granger top targets | FE top targets |
|---|---|---|
| Forward | Parenthood, Mobility, Pension | Workplace, Pay, Entrepreneurship |
| Why | Captures global democratisation waves (temporal co-movement) | Year fixed effects absorb global waves; detects within-country policy response |

Together they give a complete picture: **democracy drives WBL improvements across both long historical waves (Granger) and within individual countries' own political cycles (FE)**.

---

## Results: Difference-in-Differences with Event Study

### Methodology

The DiD event study tests whether WBL outcomes shift specifically around the year a country undergoes a democratic transition, compared to countries that never transitioned. The treatment is defined as the first year where Polity2 crosses from ≤ 0 to > 0 with a jump of at least 3 points, falling between 1976 and 2013 (to allow 5 years of data on both sides). 93 transitions are identified under this definition.

**Important limitation:** this design treats all democratic transitions as equivalent events. A country jumping from −7 to +6 on the Polity2 scale is counted the same as one moving from −1 to +2. The underlying variable is a continuous 21-point scale (−10 to +10), and the binary threshold crossing discards information about transition magnitude and durability.

### Pre-transition pattern: WBL declines into the transition year

The pre-period coefficients for the WBL Index are all statistically significant and follow a consistent downward pattern toward t = −1:

| Event time | Coefficient | p-value |
|---|---|---|
| t = −5 | +0.011 | 0.001 *** |
| t = −4 | +0.009 | 0.001 *** |
| t = −3 | +0.006 | 0.009 *** |
| t = −2 | +0.003 | 0.034 ** |
| t = −1 | 0 (reference) | — |

Countries that went on to democratize had slightly higher WBL scores years before the transition, but that advantage eroded steadily into the transition year. This is consistent with authoritarian regimes tightening restrictions on rights in the years before collapse — a pattern visible across Latin American military dictatorships and Eastern European communist regimes.

This pre-trend also means the parallel trends assumption is violated for most sub-indices, which limits the causal interpretation of the post-period estimates.

### Post-transition effects: Workplace and Pension

The post-period coefficients are near zero and not statistically significant for most sub-indices within the ±5 year window. Two exceptions pass the parallel trends check (no significant pre-period drift):

- **Workplace**: average post-transition coefficient +0.016, directionally positive and consistent with the Panel FE results. Workplace protections — anti-discrimination laws, sexual harassment legislation — are among the first legislative priorities of new democratic governments.
- **Pension**: pre-trends are flat, but the post-transition effect is also flat (avg ≈ 0.000). Pension law appears structurally unresponsive to regime transitions within a 5-year window, consistent with both the Granger and FE findings.

### Why this doesn't contradict the Granger and FE results

The flat post-transition result does not mean democracy has no effect on WBL. The Granger and FE methods capture **continuous gradual democratization** — ongoing changes in civil society participation, female legislative representation, and rule of law over many years. The DiD captures a **discrete threshold event** — the year polity2 first crosses zero.

These are different questions. The evidence from all three methods points to the same conclusion: democracy and WBL improve together, but the mechanism is slow and cumulative, not triggered by a single transition event. WBL improvements build over years of sustained democratic governance rather than jumping at the moment a regime formally crosses a numeric threshold.