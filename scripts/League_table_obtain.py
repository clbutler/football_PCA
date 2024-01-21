#!/usr/bin/env python
# coding: utf-8


import pandas as pd


prem = pd.read_html('https://www.skysports.com/premier-league-table')


table_prem = prem[0]


table_prem.to_csv(snakemake.output[0])


national_league = pd.read_html('https://www.skysports.com/national-league-table')

table_national_league = national_league[0]


table_national_league.to_csv(snakemake.output[1])

