import pandas as pd
import matplotlib.pyplot as plt

# ---------- Load Classified Data ----------
file_path = "../output/Classified_Complaints.xlsx"
df = pd.read_excel(file_path)

# ---------- Department-wise Count ----------
dept_counts = df["Department"].value_counts()

print("Department-wise Complaint Count:")
print(dept_counts)

# ---------- Bar Chart ----------
plt.figure()
dept_counts.plot(kind="bar")
plt.title("Number of Complaints per Department")
plt.xlabel("Department")
plt.ylabel("Number of Complaints")
plt.tight_layout()
plt.savefig("../output/department_analysis.png")
plt.show()

# ---------- Pie Chart ----------
plt.figure()
dept_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Complaint Distribution by Department")
plt.ylabel("")  # Hide y-label
plt.tight_layout()
plt.show()
