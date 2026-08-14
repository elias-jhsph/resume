# Elias Weston-Farber

## Research Engineer — Scientific AI & Clinical Trial Data Infrastructure

**Location:** Baltimore, MD
**Phone:** 609-442-9837
**Email:** [elias@eliastechlabs.com](mailto:elias@eliastechlabs.com)

**GitHub:** [github.com/eliaswestonfarber](https://github.com/eliaswestonfarber)
**ORCID:** [0000-0002-8452-9432](https://orcid.org/0000-0002-8452-9432)
**Passion:** [Baltimore Comedy Place](https://baltcomedyplace.com/blog/how-i-built-this.html)
**Portfolio:** [eliastechlabs.com](https://eliastechlabs.com)

Research engineer building AI systems for scientific evidence synthesis and clinical trial data infrastructure. Created ScienceAI, an open-source agentic harness that coordinates frontier language models for systematic literature analysis with provenance tracking. 9 peer-reviewed publications including NEJM and JAMA. BSPH AI Research Day Staff Award, 2026.

---

## Awards

**BSPH AI Research Day Staff Award** — Johns Hopkins Bloomberg School of Public Health, March 2026
Awarded for podium presentation and poster session on ScienceAI alongside Jeff Leek's keynote. Selected from submitted abstracts across BSPH. Abstract co-authors: Renan Castillo, Katherine Frey.

---

## Selected Projects

**ScienceAI** — Open-Source Agentic Harness for Scientific Literature Analysis *(2024–present)*
- Designed and built a multi-agent orchestration system for systematic review and meta-analysis tasks: PI orchestrator delegates to Analyst Agents that perform structured data extraction with reflection/validation
- Supports GPT, Claude, and Gemini as interchangeable backends with unified provider abstraction
- Built field-level provenance tracking: every extracted data point links to source quotes, page locations, and derivation explanations
- Validated by reproducing Scolaro et al. (2014) meta-analysis: three frontier models independently recovered the primary finding (OR 2.15–2.37 vs. published 2.32) from 19 source papers
- Published on PyPI (`pip install scienceai-llm`), GPL-3.0, 18 releases, full CI/CD; archived on Zenodo (DOI: [10.5281/zenodo.21938772](https://doi.org/10.5281/zenodo.21938772))

**Baltimore Comedy Place** — Fully autonomous, AI-powered data pipeline that scrapes, cleans, and aggregates event listings from disparate sources to create Baltimore's first comprehensive comedy show guide

**EliasTechLabs** — Consulting business website using AWS Lambda, CloudFront, S3, featuring an OpenAI-powered website assistant

**RSmartsheet** — R package interfacing with Smartsheet API, used by health authorities for project management

**SearchIt** — Systematic web search application used by NGOs for public data gathering and analysis

---

## Work Experience

### Senior Cloud Engineer & Data Manager
**METRC, Johns Hopkins Bloomberg School of Public Health**
*2023 – Present*

- Manage cloud infrastructure and data pipelines powering multi-site randomized controlled trials across 70+ Level I trauma centers nationwide
- Engineered an automated DSMB reporting system for nine studies, replacing a manual approach that required five full-time analysts with one that now requires only a single analyst
- Decreased cloud costs by 20% by migrating parts of the backend to Compute Engine while simultaneously improving system responsiveness through HTMX and WebSockets
- Implemented a real-time Firebase database to ensure data synchronization across distributed environments

### Senior Research Application Developer & Data Manager
**Johns Hopkins Bloomberg School of Public Health**
*2020 – 2023*

- Led and managed a team of six analysts and developers, successfully setting up seven studies on an analytic platform built on GCP, automating weekly reporting
- Designed and implemented a system for real-time study data issue tracking and notifications, replacing a manual static file-based system and facilitating rapid response measures that supported a major publication
- Developed tailored visualization and reporting solutions for research teams, integrating Selenium, Scrapy, and Plotly

### Research Application Developer
**Johns Hopkins Bloomberg School of Public Health**
*2019 – 2020*

- Developed a robust administrative data storage solution for managing records across 30+ METRC studies, leveraging custom Smartsheet & Google Sheets APIs and a cross-platform Electron application
- Wrote multiple R packages and designed a Python+R Docker environment to standardize the computational environment for METRC study analysis

### Backend Developer & Data Scientist
**Civicly Involved, Chicago**
*2018 – 2019*

- Led team designing API-based data integration and management solutions including geospatial analysis on Google Cloud

---

## Publications

*Role on METRC publications: Lead data engineer at the coordinating center, managing the clinical trial data pipelines, quality systems, and reporting infrastructure underlying each study. In consortium trials, named authorship reflects site PIs and study leads; coordinating center staff who build and maintain the shared data infrastructure are listed as collaborators.*

1. O'Toole RV, O'Hara NN, ..., **Weston-Farber E**, ..., Castillo RC; METRC. "Intrawound Tobramycin Plus Vancomycin to Prevent Surgical Site Infection in Tibial Fractures: The TOBRA Randomized Clinical Trial." **JAMA**, 2026.
2. Levy JF, ..., Castillo RC, O'Hara NN; METRC (incl. **Weston-Farber E**). "The Cost-Effectiveness of Enoxaparin Compared with Aspirin for Thromboprophylaxis." **J Bone Joint Surg Am**, 2026.
3. Levy JF, ..., O'Hara NN; METRC (incl. **Weston-Farber E**). "Cost Savings of Switching to Aspirin for Thromboprophylaxis in Orthopaedic Trauma Patients." **J Am Acad Orthop Surg**, 2026.
4. O'Hara NN, Frey KP, ..., O'Toole RV; METRC (incl. **Weston-Farber E**). "Effect of Aspirin Versus Low-Molecular-Weight Heparin Thromboprophylaxis on Medication Satisfaction." **J Bone Joint Surg Am**, 2024.
5. O'Hara NN, O'Toole RV, ..., Stein DM; METRC (incl. **Weston-Farber E**). "Risk-Stratified Thromboprophylaxis Effects of Aspirin Versus Low-Molecular-Weight Heparin." **J Trauma Acute Care Surg**, 2024.
6. O'Toole RV, Stein DM, ..., Castillo RC; METRC (incl. **Weston-Farber EM**). "Aspirin or Low-Molecular-Weight Heparin for Thromboprophylaxis after a Fracture." **N Engl J Med**, 2023.
7. Staguhn ED, **Weston-Farber E**, Castillo RC. "The Impact of Statewide School Closures on COVID-19 Infection Rates." **Am J Infect Control**, 2021.
8. Castillo RC, Staguhn ED, **Weston-Farber E**. "The Effect of State-Level Stay-at-Home Orders on COVID-19 Infection Rates." **Am J Infect Control**, 2020.
9. Tarpada SP, O'Hara NN, ..., Marvel D; METRC (incl. **Weston-Farber E**). "Effect of Aspirin Versus Low-Molecular-Weight Heparin for Thromboprophylaxis in High-Risk and Fracture Location Subpopulations." **J Orthop Trauma**, 2026. *(Podium presentation, OTA 2024; Bovill Award)*

**In Press / Under Review**

10. "A Prospective Randomized Trial to Assess Early versus Delayed Weight Bearing Following Operatively Treated Ankle Fractures in the United States." METRC. *(Bovill Award, OTA 2025)*
11. "The Effect of Hemorrhage Magnitude on the Immunologic Response in Polytraumatized Patients with Destabilizing Orthopaedic Injuries." METRC.
12. "Active Bleeding on Admission CT is Correlated with Blood Transfusion Needs in the Setting of Multi-System Trauma." METRC.
13. "Early Cumulative Hemorrhagic 'Shock Volume' is Associated with Organ Dysfunction in Polytrauma Patients." METRC.

---

## Education

**University of Maryland Baltimore County**, Baltimore — *2018*
*Bachelor of Science in Environmental Science & Geography*
*Bachelor of Arts in Political Science*

---

## Technical Skills

- **Languages:** Python, R, JavaScript, SQL
- **AI/ML:** Multi-agent LLM orchestration, provider API integration (OpenAI, Anthropic, Google), structured data extraction, prompt engineering, evaluation design
- **Frameworks:** Flask, Node.js, PyTorch, Pandas, Tidyverse, Shiny, Electron, HTMX
- **Infrastructure:** Docker, AWS, GCP, GitHub Actions, Firebase, WebSockets
- **Data & Analysis:** Tableau, ArcGIS, QGIS, Plotly, ggplot2
