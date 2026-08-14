# Elias Weston-Farber

## Research Engineer — Scientific AI & Clinical Trial Data Infrastructure

**Location:** Baltimore, MD
**Phone:** 609-442-9837
**Email:** [eliaswestonfarber@gmail.com](mailto:eliaswestonfarber@gmail.com)

**GitHub:** [github.com/eliaswestonfarber](https://github.com/eliaswestonfarber)
**ORCID:** [0000-0002-8452-9432](https://orcid.org/0000-0002-8452-9432)
**Publications:** [PubMed Bibliography](https://www.ncbi.nlm.nih.gov/myncbi/elias.weston-farber.1/bibliography/public/)

Research engineer building AI systems for scientific evidence synthesis and clinical trial data infrastructure. Created ScienceAI, an open-source agentic harness that coordinates frontier language models for systematic literature analysis with provenance tracking. 9 peer-reviewed publications including NEJM and JAMA. BSPH AI Research Day Staff Award, 2026.

---

## Publications & Awards

**9 peer-reviewed publications** (2 authored, 7 as METRC consortium collaborator — lead data engineer at the coordinating center), including **NEJM** and **JAMA** • **4 manuscripts in press / under review** (METRC) • **1 DOI-archived open-source software package** ([10.5281/zenodo.21938772](https://doi.org/10.5281/zenodo.21938772))

**Full publication list:** [PubMed Bibliography](https://www.ncbi.nlm.nih.gov/myncbi/elias.weston-farber.1/bibliography/public/)

**BSPH AI Research Day Staff Award** — Johns Hopkins Bloomberg School of Public Health, March 2026. Awarded for podium presentation and poster session on ScienceAI alongside Jeff Leek's keynote. Selected from submitted abstracts across BSPH. Abstract co-authors: Renan Castillo, Katherine Frey.

---

## Selected Projects

**ScienceAI** — Open-Source Agentic Harness for Scientific Literature Analysis *(2024–present)*
- Designed and built a multi-agent orchestration system for systematic review and meta-analysis tasks: PI orchestrator delegates to Analyst Agents that perform structured data extraction with reflection/validation
- Supports GPT, Claude, and Gemini as interchangeable backends with unified provider abstraction; field-level provenance tracking links every extracted data point to source quotes, page locations, and derivation explanations
- Validated by reproducing Scolaro et al. (2014) meta-analysis: three frontier models independently recovered the primary finding (OR 2.15–2.37 vs. published 2.32) from 19 source papers
- Published on PyPI (`pip install scienceai-llm`), GPL-3.0, 18 releases, full CI/CD, archived on Zenodo

**Baltimore Comedy Place** — Fully autonomous, AI-powered data pipeline that scrapes, cleans, and aggregates event listings from disparate sources to create Baltimore's first comprehensive comedy show guide

**EliasTechLabs** — Serverless personal site built on AWS Lambda, CloudFront, and S3, featuring an LLM-powered website assistant

**RSmartsheet** — R package interfacing with Smartsheet API, used by health authorities for project management

**SearchIt** — Systematic web search application used by NGOs for public data gathering and analysis

---

## Work Experience

### Senior Cloud Engineer & Data Manager
**METRC, Johns Hopkins Bloomberg School of Public Health**
*2023 – Present*

- Manage cloud infrastructure and data pipelines powering multi-site randomized controlled trials across 70+ Level I trauma centers nationwide
- Engineered an automated DSMB reporting system for nine studies, replacing a manual approach that required five full-time analysts with one that now requires only a single analyst
- Decreased cloud costs by 20% by migrating parts of the backend to Compute Engine while simultaneously improving system responsiveness and user engagement through HTMX and WebSockets, enabling real-time feedback
- Implemented a real-time Firebase database to ensure data synchronization across distributed environments

### Senior Research Application Developer & Data Manager
**Johns Hopkins Bloomberg School of Public Health**
*2020 – 2023*

- Led and managed a team of six analysts and developers, successfully setting up seven studies on an analytic platform built on GCP, automating weekly reporting
- Designed and implemented a system for real-time study data issue tracking and notifications, replacing a manual static file-based system and facilitating rapid response measures that supported a major publication
- Developed tailored visualization and reporting solutions for research teams, integrating technologies such as Selenium and Scrapy to extract conflicts of interest data, and Plotly to create interactive reports

### Research Application Developer
**Johns Hopkins Bloomberg School of Public Health**
*2019 – 2020*

- Developed a robust administrative data storage solution for managing records across 30+ METRC studies, leveraging custom Smartsheet & Google Sheets APIs and a cross-platform Electron application
- Wrote multiple R packages and designed a Python+R Docker environment to standardize the computational environment for METRC study analysis

### Backend Developer & Data Scientist
**Civicly Involved, Chicago**
*2018 – 2019*

- Led a team of interns in designing and implementing API-based data integration and management solutions, including geospatial data analysis using Google Cloud technologies

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
