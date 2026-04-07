import pandas as pd


xl = pd.ExcelFile('jc.xlsx')

df_2020 = pd.read_excel(xl, sheet_name='2020')
df_2021 = pd.read_excel(xl, sheet_name='2021')
df_2022 = pd.read_excel(xl, sheet_name='2022')
df_2023 = pd.read_excel(xl, sheet_name='2023')
df_2024 = pd.read_excel(xl, sheet_name='2024')
df_2025 = pd.read_excel(xl, sheet_name='2025')
df_2020A = pd.read_excel(xl, sheet_name='2020A')
df_2021A= pd.read_excel(xl, sheet_name='2021A')
df_2022A = pd.read_excel(xl, sheet_name='2022A')
df_2023A = pd.read_excel(xl, sheet_name='2023A')
df_2024A = pd.read_excel(xl, sheet_name='2024A')
df_2025A = pd.read_excel(xl, sheet_name='2025A')

df_2024A = df_2024A.rename(columns={"Closing Rank": "Closing Rank 2024"})
df_2023A = df_2023A.rename(columns={"Closing Rank": "Closing Rank 2023"})
df_2022A = df_2022A.rename(columns={"Closing Rank": "Closing Rank 2022"})
df_2021A = df_2021A.rename(columns={"Closing Rank": "Closing Rank 2021"})
df_2020A = df_2020A.rename(columns={"Closing Rank": "Closing Rank 2020"})

df_2024 = df_2024.rename(columns={"Closing Rank": "Closing Rank 2024"})
df_2023 = df_2023.rename(columns={"Closing Rank": "Closing Rank 2023"})
df_2022 = df_2022.rename(columns={"Closing Rank": "Closing Rank 2022"})
df_2021 = df_2021.rename(columns={"Closing Rank": "Closing Rank 2021"})
df_2020 = df_2020.rename(columns={"Closing Rank": "Closing Rank 2020"})

dfA=df_2025A.merge(df_2024A, on=['Institute', 'Academic Program Name', 'Quota', 'Seat Type', 'Gender'], how='left')\
    .merge(df_2023A, on=['Institute', 'Academic Program Name', 'Quota', 'Seat Type', 'Gender'], how='left')\
    .merge(df_2022A, on=['Institute', 'Academic Program Name', 'Quota', 'Seat Type', 'Gender'], how='left')\
    .merge(df_2021A, on=['Institute', 'Academic Program Name', 'Quota', 'Seat Type', 'Gender'], how='left')\
    .merge(df_2020A, on=['Institute', 'Academic Program Name', 'Quota', 'Seat Type', 'Gender'], how='left')

dfM=df_2025.merge(df_2024, on=['Institute', 'Academic Program Name', 'Quota', 'Seat Type', 'Gender'], how='left')\
    .merge(df_2023, on=['Institute', 'Academic Program Name', 'Quota', 'Seat Type', 'Gender'], how='left')\
    .merge(df_2022, on=['Institute', 'Academic Program Name', 'Quota', 'Seat Type', 'Gender'], how='left')\
    .merge(df_2021, on=['Institute', 'Academic Program Name', 'Quota', 'Seat Type', 'Gender'], how='left')\
    .merge(df_2020, on=['Institute', 'Academic Program Name', 'Quota', 'Seat Type', 'Gender'], how='left')

rank_cols = [col for col in dfA.columns if "Closing Rank" in col]

dfA = dfA[
    ~dfA[rank_cols]
    .astype(str)
    .apply(lambda x: x.str.strip().str.endswith('P'))
    .any(axis=1)
]

rank_colss = [col for col in dfM.columns if "Closing Rank" in col]

dfM = dfM[
    ~dfM[rank_colss]
    .astype(str)
    .apply(lambda x: x.str.strip().str.endswith('P'))
    .any(axis=1)
]

state = {

    # ---------------- IITs ----------------
    "Bombay": "Maharashtra",
    "Delhi": "Delhi",
    "Madras": "Tamil Nadu",
    "Kanpur": "Uttar Pradesh",
    "Kharagpur": "West Bengal",
    "Roorkee": "Uttarakhand",
    "Guwahati": "Assam",
    "Hyderabad": "Telangana",
    "Indore": "Madhya Pradesh",
    "Mandi": "Himachal Pradesh",
    "Patna": "Bihar",
    "Ropar": "Punjab",
    "Bhubaneswar": "Odisha",
    "Gandhinagar": "Gujarat",
    "Jodhpur": "Rajasthan",
    "Varanasi": "Uttar Pradesh",
    "Tirupati": "Andhra Pradesh",
    "Palakkad": "Kerala",
    "Bhilai": "Chhattisgarh",
    "Goa": "Goa",
    "Jammu": "Jammu & Kashmir",
    "Dharwad": "Karnataka",
    "Dhanbad": "Jharkhand",

    # ---------------- NITs ----------------
    "Trichy": "Tamil Nadu",
    "Surathkal": "Karnataka",
    "Warangal": "Telangana",
    "Calicut": "Kerala",
    "Durgapur": "West Bengal",
    "Rourkela": "Odisha",
    "Silchar": "Assam",
    "Hamirpur": "Himachal Pradesh",
    "Jalandhar": "Punjab",
    "Kurukshetra": "Haryana",
    "Nagpur": "Maharashtra",
    "Patna_NIT": "Bihar",
    "Raipur": "Chhattisgarh",
    "Srinagar": "Jammu & Kashmir",
    "Agartala": "Tripura",
    "Arunachal": "Arunachal Pradesh",
    "Meghalaya": "Meghalaya",
    "Manipur": "Manipur",
    "Mizoram": "Mizoram",
    "Nagaland": "Nagaland",
    "Sikkim": "Sikkim",
    "Puducherry": "Puducherry",
    "Goa_NIT": "Goa",
    "Delhi_NIT": "Delhi",
    "Uttarakhand": "Uttarakhand",
    "Andhra": "Andhra Pradesh",
    "Jamshedpur": "Jharkhand",
    "Jaipur": "Rajasthan",
    #----------IIIT-----------------
    "Allahabad": "Uttar Pradesh",
    "Gwalior": "Madhya Pradesh",
    "Jabalpur": "Madhya Pradesh",
    "Kancheepuram": "Tamil Nadu",
    "Kurnool": "Andhra Pradesh",
    "Lucknow": "Uttar Pradesh",
    "Pune": "Maharashtra",
    "Vadodara": "Gujarat",
    "Nagpur_IIIT": "Maharashtra",
    "Sri City": "Andhra Pradesh",
    "Una": "Himachal Pradesh",
    "Kota": "Rajasthan",
    "Ranchi": "Jharkhand",
    "Bhagalpur": "Bihar",
    "Surat": "Gujarat",
    "Bhopal": "Madhya Pradesh",
    "Agartala_IIIT": "Tripura",
    "Kalyani": "West Bengal",
    "Dharwad_IIIT": "Karnataka",
    "Raichur": "Karnataka",
    "Kottayam": "Kerala",
    "Manipur_IIIT": "Manipur",
    "Nagaland_IIIT": "Nagaland",
    "Tiruchirappalli": "Tamil Nadu",
    "Sonepat": "Haryana",
    "Shibpur": "West Bengal"
}
def get_state(institute_name):
    for key in state:
        if key.lower() in institute_name.lower():
            return state[key]
    return "Unknown"
dfA["State"] = dfA["Institute"].apply(get_state)
dfM["State"] = dfM["Institute"].apply(get_state)

dfA.to_csv("ADV1ws.csv")
dfM.to_csv("Mainws.csv")

