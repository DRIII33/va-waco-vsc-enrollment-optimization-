CREATE OR REPLACE TABLE `driiiportfolio.waco_vsc_operations.raw_veteran_enrollments` (
    Record_ID STRING,
    VBA_RO_Assigned STRING,
    Enrollment_Type STRING,
    VBA_Receipt_Timestamp STRING,
    VBA_VHA_Transfer_Timestamp STRING,
    VHA_Triage_Timestamp STRING,
    VHA_Final_Determination_Timestamp STRING
)
PARTITION BY DATE(CAST(VBA_Receipt_Timestamp AS TIMESTAMP));
