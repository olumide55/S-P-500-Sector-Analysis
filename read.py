import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sp500_companies.csv')
df_clean= df.dropna(subset = ['Ebitda', 'Revenuegrowth'])
sector_summary = df_clean.groupby('Sector')[['Marketcap', 'Ebitda', 'Revenuegrowth']].mean()
pd.options.display.float_format = '{:,.2f}'.format
print(sector_summary)

fig, axes = plt.subplots(1, 3, figsize=(22, 6))

sns.barplot(x=sector_summary['Marketcap'], y=sector_summary.index, order=sector_summary['Marketcap'].sort_values().index, ax=axes[0], color='steelblue')
axes[0].set_title('Average Market Cap by Sector')
axes[0].set_xlabel('Market Cap (USD)')
axes[0].set_ylabel('')

sns.barplot(x=sector_summary['Ebitda'], y=sector_summary.index, order=sector_summary['Ebitda'].sort_values().index, ax=axes[1], color='darkorange')
axes[1].set_title('Average EBITDA by Sector')
axes[1].set_xlabel('EBITDA (USD)')
axes[1].set_ylabel('')

sns.barplot(x=sector_summary['Revenuegrowth'], y=sector_summary.index, order=sector_summary['Revenuegrowth'].sort_values().index, ax=axes[2], color='seagreen')
axes[2].set_title('Average Revenue Growth by Sector')
axes[2].set_xlabel('Revenue Growth')
axes[2].set_ylabel('')

plt.tight_layout()
plt.savefig('sector_charts.png', dpi=150, bbox_inches='tight')
plt.show()

