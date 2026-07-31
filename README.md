# va-waco-vsc-enrollment-optimization

##### **Management Analyst:** Daniel Rodriguez III

##### **Date:** July 31, 2026
---

## Project Overview
This repository houses the end-to-end analytical framework designed for the **Waco VA Regional Office Veterans Service Center (VSC)**. The project addresses a critical 38% surge in healthcare enrollment requests that resulted in average turnaround times escalating to 9.49 days, significantly breaching the federally mandated 5-day Service Level Agreement (SLA).

## Core Objectives
- **Identify Root Causes:** Isolate whether delays stem from IT infrastructure (Technical Latency) or personnel constraints (Operational Bottlenecks).
- **Data-Driven Diagnostic:** Utilize SQL ELT pipelines and statistical modeling (ANOVA) to validate findings.
- **Strategic Restoration:** Provide the Assistant Veterans Service Center Manager (AVSCM) with a targeted action plan to restore 95% SLA compliance.
- **Executive Oversight:** Deploy a Looker Studio Performance Console for real-time monitoring.

## Repository Structure
- `data_generation/`: Python scripts for high-fidelity synthetic data production.
- `data_warehouse/`: BigQuery DDL and ELT SQL scripts.
- `statistical_analysis/`: ANOVA and Tukey HSD testing notebooks.
- `documentation/`: Executive briefs, dashboard specifications, and project charters.

## Key Findings
- **Technical Latency:** Accounts for 44.86% of delays due to system handoff lag.
- **Operational Bottlenecks:** Priority Group Upgrades average 13.91 days due to manual verification requirements.
- **Current SLA Compliance:** 19.7%.
