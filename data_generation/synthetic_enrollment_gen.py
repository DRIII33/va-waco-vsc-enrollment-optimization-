import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Configure seed for reproducibility
np.random.seed(42)
num_records = 5000

# Configuration: Waco heavy distribution
ro_options = ["Waco (349)", "Houston (362)", "St. Paul (335)", "Phoenix (344)", "Muskogee (351)"]
ro_weights = [0.55, 0.15, 0.12, 0.10, 0.08]
assigned_ros = np.random.choice(ro_options, size=num_records, p=ro_weights)

enrollment_options = ["New Enrollment", "Priority Group Upgrade", "Combat Veteran Auto-Enroll", "Inter-Facility Transfer"]
enrollment_weights = [0.45, 0.30, 0.15, 0.10]
assigned_types = np.random.choice(enrollment_options, size=num_records, p=enrollment_weights)

# Generate timestamps over 18-month window
start_date = datetime(2025, 1, 1)
end_date = datetime(2026, 6, 30)
delta_days = (end_date - start_date).days
base_dates = [start_date + timedelta(days=np.random.randint(0, delta_days)) for _ in range(num_records)]
base_dates.sort()

# Process durations with engineered bottlenecks
vba_vha_ts, triage_ts, final_ts = [], [], []

for ro, en_type, start in zip(assigned_ros, assigned_types, base_dates):
    d1 = np.random.exponential(scale=1.2) # Base latency
    d2 = np.random.exponential(scale=1.5)
    d3 = np.random.exponential(scale=2.0)

    if ro == "Waco (349)": d1 += np.random.normal(loc=5.1, scale=1.1) # IT Bottleneck
    if en_type == "Priority Group Upgrade": d2 += np.random.normal(loc=6.4, scale=1.8) # Staff Bottleneck

    t1 = start + timedelta(days=max(0.1, d1))
    t2 = t1 + timedelta(days=max(0.1, d2))
    t3 = t2 + timedelta(days=max(0.1, d3))

    vba_vha_ts.append(t1.strftime('%Y-%m-%d %H:%M:%S'))
    triage_ts.append(t2.strftime('%Y-%m-%d %H:%M:%S'))
    final_ts.append(t3.strftime('%Y-%m-%d %H:%M:%S'))

df = pd.DataFrame({
    'Record_ID': [f"VA-VSC-{i:05d}" for i in range(1, num_records+1)],
    'VBA_RO_Assigned': assigned_ros,
    'Enrollment_Type': assigned_types,
    'VBA_Receipt_Timestamp': [d.strftime('%Y-%m-%d %H:%M:%S') for d in base_dates],
    'VBA_VHA_Transfer_Timestamp': vba_vha_ts,
    'VHA_Triage_Timestamp': triage_ts,
    'VHA_Final_Determination_Timestamp': final_ts
})

df.to_csv('generated_vsc_enrollment_data.csv', index=False)
