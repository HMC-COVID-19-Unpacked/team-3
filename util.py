import pandas as pd

DATA_DIR = 'overall_data/'

covid = pd.read_csv(DATA_DIR + 'covid_compiled.csv', dtype={'fips': str})
obesity = pd.read_csv(DATA_DIR + 'obesity_compiled.csv', dtype={'fips': str})

# print(covid.dtypes)
# print(obesity.dtypes)
# print(obesity['fips'])

covid['obesity_freq'] = 0.0

for x in range(covid.shape[0]):
    if covid['fips'][x] in list(obesity['fips']):
        # print(obesity.loc[obesity['fips'] == covid['fips'][x], 'freq'])
        covid['obesity_freq'][x] = obesity.loc[obesity['fips'] == covid['fips'][x], 'freq'].iloc[0]
covid = covid.drop(columns=['Unnamed: 0'])

covid.to_csv('overall_data/covid_obesity.csv')