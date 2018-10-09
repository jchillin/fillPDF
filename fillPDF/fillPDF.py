import csv
from fdfgen import forge_fdf
import os
import sys

sys.path.insert(0, os.getcwd())
filename_prefix = "NVC"
csv_file = "~/Documents/fillPDF/ReleaseForm.csv"
pdf_file1 = "~/Documents/fillPDF/Medical_Release_for_Adults.pdf"
pdf_file2 = "~/Documents/fillPDF/Release_and_Indemnification_Agreement_for_Domestic_Travel_for_Adults.pdf"
pdf_file3 = "~/Documents/fillPDF/UT-Dallas-Responsibilities-of-Participants-Updated1.1.pdf"
tmp_file = "tmp.fdf"
output_folder = './output/'

def process_csv(file):
    headers = []
    data =  []
    csv_data = csv.reader(open(file))
    for i, row in enumerate(csv_data):
      if i == 0:
        headers = row
        continue;
      field = []
      for i in range(len(headers)):
        field.append((headers[i], row[i]))
      data.append(field)
    return data

def form_fill(fields):
  fdf = forge_fdf("",fields,[],[],[])
  fdf_file = open(tmp_file,"w")
  fdf_file.write(fdf)
  fdf_file.close()
  output_file = '{0}{1} {2}.pdf'.format(output_folder, filename_prefix, fields[1][1])
  cmd = 'pdftk "{0}" fill_form "{1}" output "{2}" dont_ask'.format(pdf_file, tmp_file, output_file)
  os.system(cmd)
  os.remove(tmp_file)

data = process_csv(csv_file)
print('Generating Forms:')
print('-----------------------')
for i in data:
  if i[0][1] == 'Yes':
    continue
  print('{0} {1} created...'.format(filename_prefix, i[1][1]))
  form_fill(i)
