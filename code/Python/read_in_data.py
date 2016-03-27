
# Read in Data
m = pd.read_csv("data/POV_data.csv",index_col=0)
# Create Smoothed Matrix
m_smoothed = m.copy()
m_smoothed["AFFC"] = (m["AFFC"] + m["ADWD"]) * (m["AFFC"].sum() / m[["AFFC","ADWD"]].sum().sum())
m_smoothed["ADWD"] = (m["AFFC"] + m["ADWD"]) * (m["ADWD"].sum() / m[["AFFC","ADWD"]].sum().sum())           
# Created Matrix where books 4,5 are combined
m_combined = m.ix[:,:4].copy()
m_combined = m_combined.join(pd.DataFrame((m["AFFC"] +m["ADWD"])))
m_combined.columns = [_ for _ in m_combined.columns if _!= 0] + ["Book4_5"]
# Create Matrices for Validation
m_val1 = m.ix[:9,:2].copy()
m_val2 = m.ix[:12,:3].copy()