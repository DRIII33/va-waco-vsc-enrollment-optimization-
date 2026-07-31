import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. ANOVA for Regional Offices
ro_groups = [group['Total_Processing_Days'].values for name, group in df.groupby('VBA_RO_Assigned')]
f_stat_ro, p_val_ro = stats.f_oneway(*ro_groups)

# 2. Tukey HSD for Regional Offices
tukey_ro = pairwise_tukeyhsd(endog=df['Total_Processing_Days'], groups=df['VBA_RO_Assigned'], alpha=0.05)

# 3. ANOVA for Enrollment Types
type_groups = [group['Total_Processing_Days'].values for name, group in df.groupby('Enrollment_Type')]
f_stat_type, p_val_type = stats.f_oneway(*type_groups)

# 4. Tukey HSD for Enrollment Types
tukey_type = pairwise_tukeyhsd(endog=df['Total_Processing_Days'], groups=df['Enrollment_Type'], alpha=0.05)

print(f"ANOVA (Regional Office): F={f_stat_ro:.2f}, p={p_val_ro:.2e}")
print(f"ANOVA (Enrollment Type): F={f_stat_type:.2f}, p={p_val_type:.2e}")

# 5. Visualization
plt.figure(figsize=(16, 6))

plt.subplot(1, 2, 1)
sns.boxplot(x='VBA_RO_Assigned', y='Total_Processing_Days', data=df, palette='viridis')
plt.title('Processing Days by Regional Office')
plt.xticks(rotation=45)
plt.axhline(5, color='red', linestyle='--', label='5-Day SLA')
plt.legend()

plt.subplot(1, 2, 2)
sns.boxplot(x='Enrollment_Type', y='Total_Processing_Days', data=df, palette='magma')
plt.title('Processing Days by Enrollment Type')
plt.xticks(rotation=45)
plt.axhline(5, color='red', linestyle='--', label='5-Day SLA')
plt.legend()

plt.tight_layout()
plt.show()

print("\n--- Tukey HSD: Regional Office Summary ---")
print(tukey_ro.summary())
print("\n--- Tukey HSD: Enrollment Type Summary ---")
print(tukey_type.summary())
