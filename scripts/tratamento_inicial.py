from pathlib import Path
import pandas as pd

XLSX_PATH = r"C:\Users\Gabriel\Documents\GitHub\visualizacao_bi_lab4\dados\dataset_fase1_validacao.xlsx"

df1 = pd.read_excel(XLSX_PATH, sheet_name='Mortos')
df2 = pd.read_excel(XLSX_PATH, sheet_name='Ressuscitados')
df3 = pd.read_excel(XLSX_PATH, sheet_name='Estatísticas')

for df in [df1, df2]:
    df['Data de morte'] = pd.to_datetime(df['Data de morte'])
    df['Data de ressurreição'] = pd.to_datetime(df.get('Data de ressurreição'))
    df['Duração de morte (dias)'] = (df['Data de ressurreição'] - df['Data de morte']).dt.days

OUT_DIR = Path(XLSX_PATH).parent
OUTPUT_PATH = OUT_DIR / "dataset_fase1_validacao_tratado.xlsx"

with pd.ExcelWriter(OUTPUT_PATH, engine="openpyxl") as writer:
    df1.to_excel(writer, sheet_name='Mortos', index=False)
    df2.to_excel(writer, sheet_name='Ressuscitados', index=False)
    df3.to_excel(writer, sheet_name='Estatísticas', index=False)