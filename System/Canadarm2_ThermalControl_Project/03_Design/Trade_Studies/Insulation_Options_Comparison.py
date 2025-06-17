import os
from openpyxl import Workbook

# Get the folder where this script is located
current_folder = os.path.dirname(os.path.abspath(__file__))

# Set the full path for the Excel file
file_path = os.path.join(current_folder, "Insulation_Options_Comparison.xlsx")

# Create the workbook and add data
wb = Workbook()
ws = wb.active
ws.title = "Insulation_Options_Comparison"

# Header
ws.append(["Material", "Thermal Conductivity (W/m·K)", "Mass (g/m²)", "Radiation Resistance", "Cost", "Recommendation"])

# Data
data = [
    ["MLI (5 layers)", "Very Low", "Low", "High", "Medium", "✔ Recommended"],
    ["Kapton Film", "Low", "Very Low", "Medium", "High", "Backup Only"],
    ["Aerogel Blanket", "Very Low", "Moderate", "Low", "High", "❌ Not Suitable"]
]

for row in data:
    ws.append(row)

# Save the file in the same folder
wb.save(file_path)

print(f"File saved to: {file_path}")
