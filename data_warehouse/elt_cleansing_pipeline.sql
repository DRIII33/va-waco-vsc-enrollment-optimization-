CREATE OR REPLACE TABLE `driiiportfolio.waco_vsc_operations.analytics_vsc_performance_reporting` AS
WITH cleaned_records AS (
    SELECT
        TRIM(Record_ID) AS record_id,
        COALESCE(TRIM(VBA_RO_Assigned), 'Unknown/Unassigned') AS regional_office,
        CASE
            WHEN Enrollment_Type IS NULL OR TRIM(Enrollment_Type) = '' THEN 'PENDING CLASSIFICATION'
            ELSE UPPER(TRIM(Enrollment_Type))
        END AS enrollment_classification,
        -- Direct cast since the audit confirmed columns are already TIMESTAMP types
        CAST(VBA_Receipt_Timestamp AS TIMESTAMP) AS ts_vba_receipt,
        CAST(VBA_VHA_Transfer_Timestamp AS TIMESTAMP) AS ts_vha_transferred,
        CAST(VHA_Triage_Timestamp AS TIMESTAMP) AS ts_vha_triaged,
        CAST(VHA_Final_Determination_Timestamp AS TIMESTAMP) AS ts_vha_finalized
    FROM
        `driiiportfolio.waco_vsc_operations.raw_veteran_enrollments`
    WHERE
        Record_ID IS NOT NULL
),
interval_calculations AS (
    SELECT
        *,
        TIMESTAMP_DIFF(ts_vha_transferred, ts_vba_receipt, SECOND) / 86400.0 AS days_vba_to_vha_handoff,
        TIMESTAMP_DIFF(ts_vha_triaged, ts_vha_transferred, SECOND) / 86400.0 AS days_vha_internal_triage,
        TIMESTAMP_DIFF(ts_vha_finalized, ts_vba_receipt, SECOND) / 86400.0 AS total_turnaround_days
    FROM
        cleaned_records
)
SELECT
    *,
    CASE
        WHEN total_turnaround_days <= 5.0 THEN 1
        ELSE 0
    END AS is_sla_compliant,
    CASE
        WHEN (days_vba_to_vha_handoff > 5.0) THEN 'SYSTEM HANDOFF DELAY(Tech)'
        WHEN (days_vha_internal_triage > 3.0) THEN 'INTERNAL TRIAGE BOTTLENECK(Staff)'
        ELSE 'ROUTINE PROCESSING'
    END AS primary_delay_attribution
FROM
    interval_calculations;
