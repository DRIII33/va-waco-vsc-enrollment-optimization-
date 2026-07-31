# Executive Summary: Waco VSC Enrollment Optimization

---
#### **Management Analyst:** Daniel Rodriguez III

#### **Date:** July 31, 2026

---

### **Project Overview**

This initiative establishes a data-driven diagnostic framework for the Waco VA Regional Office (RO 349) to address critical failures in the Veterans Health Administration (VHA) healthcare enrollment pipeline. By leveraging BigQuery ELT processes and statistical inference, we provide the leadership team with actionable intelligence to restore federal SLA compliance.

### **The Business Challenge (The Reason for Hire)**

The Waco VSC has experienced a **38% surge** in dual VBA-VHA healthcare enrollment requests over the past 18 months due to legislative expansions. Consequently, the office's average time to complete an enrollment determination escalated from **4.2 days to 9.49 days**, violating VHA's strict 5-day internal service level agreement (SLA). Prior to this analysis, the AVSCM could not definitively identify whether delays stemmed from Technical Latency (system handoffs) or Operational Bottlenecks (manual verification surges).

### **Core Diagnostic Findings**

  * **Total Sample Size:** 5,000 unique veteran records (Jan 2025 – June 2026).
  * **SLA Compliance Rate:** Currently at **19.7%**, meaning 4 out of 5 veterans face delayed healthcare access.
  * **Primary Technical Driver:** **44.86% of delays** are attributed to a unique server synchronization lag at the Waco node, adding **~5.1 days of latency** before human intervention is possible.
  * **Primary Operational Driver:** Priority Group Upgrades are the most significant human bottleneck, averaging **13.91 days** due to complex manual verification requirements.

### **Strategic Recommendations**

  1. **API Modernization:** Shift from batch-mode transfers to real-time API integrations to eliminate the 5.1-day server-side delay.
  2. Rapid Response Unit:** Realign 25% of staff into a specialized triage team for Priority Group Upgrades, utilizing standardized validation templates to reduce manual processing time by an estimated 55%.
