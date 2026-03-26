# A Causal Analysis of the Relationship between Democracies, Civil Liberties, and Women's Rights under the Law

This project does a historical analysis of the variation in the level of democracy, political freedom, and civil liberties in a country and how these impact on the women's equality defined by the legal framework of such states.

___

## Sources


---

## Main Dataset: Polity5, V-Dem, WBL, RDI

File: `processed-datasets/merged/democracy_wbl_rdi.csv`

**8,561 rows × 101 columns** — 174 countries, years 1971–2018.

Merges three sources:
- **Polity5** — regime type and authority characteristics
- **V-Dem** (Varieties of Democracy) — fine-grained democracy indices, including gender-specific measures
- **World Bank Women, Business and the Law (WBL)** — legal rights indicators for women
- **Pew Research Center Religious Diversity Index** — religious composition and dominant religion per country

---

### Identifiers

| Field | Description | Range / Values |
|---|---|---|
| `ts_id` | Unique time-series ID in format `{ccode}_{ISO3}` | string |
| `orig_ccode` | Original Polity5 numeric country code | 2–950 |
| `orig_country` | Country name as it appears in the original Polity5 dataset (may differ for historical entities) | string |
| `country` | Canonical country name | string |
| `curr_iso3` | Current ISO 3166-1 alpha-3 country code (used as the merge key) | 174 unique codes |
| `curr_country` | Current country name matching `curr_iso3` | string |
| `year` | Year of observation | 1971–2018 |

---

### Polity5 Variables (`p_` prefix)

Democracy/autocracy scores from the [Polity5 project](https://www.systemicpeace.org/polityproject.html).

> **Special codes:** Several Polity5 fields use the values −88 (transition/interregnum period — no coherent authority), −77 (interruption — foreign interruption of governance), and −66 (periods of interregnum) as missing-data indicators rather than numeric scores. These should be treated as NaN in analysis. `p_regtrans` uses 99 for interregnum and −77/−66 for interruption/interregnum codes.

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

Indices marked **0–1** follow the standard V-Dem scale. Indices marked **z-score** are latent variable estimates on an interval scale centered near 0 — higher values indicate better conditions for women, lower values indicate worse.

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
| `wbl_index` | Overall WBL index — average of the 8 sub-indices below | 17.5–100 |
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
| `rdi` | Religious Diversity Index — higher values indicate greater diversity in religious composition | 0–9 (theoretical max: 10; observed max in dataset: 9) |
| `dominant_religion` | The largest religious group in the country | `christian`, `muslim`, `unaffiliated`, `hindu`, `buddhist`, `folk`, `jewish` |
