import os
import zipfile
import shutil
import pandas as pd

DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")
EXTRACTED_DIR = os.path.join(os.getcwd(), "extracted")
OUTPUT_DIR = os.path.join(os.getcwd(), "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "di_pipes.xlsx")

os.makedirs(EXTRACTED_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

found_entries = []

def contains_item_8329(excel_path):
    try:
        xl = pd.ExcelFile(excel_path)
        for sheet in xl.sheet_names:
            df = xl.parse(sheet)
            if df.astype(str).apply(lambda x: x.str.contains("8329")).any().any():
                return True
    except Exception as e:
        print(f"❌ Error reading {excel_path}: {e}")
    return False

for zip_file in os.listdir(DOWNLOAD_DIR):
    if not zip_file.endswith(".zip"):
        continue

    zip_path = os.path.join(DOWNLOAD_DIR, zip_file)
    temp_extract_path = os.path.join(DOWNLOAD_DIR, "temp_unzip")

    os.makedirs(temp_extract_path, exist_ok=True)
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_extract_path)
    except Exception as e:
        print(f"❌ Error unzipping {zip_file}: {e}")
        shutil.rmtree(temp_extract_path)
        continue

    found_8329 = False
    for root, _, files in os.walk(temp_extract_path):
        for file in files:
            if file.endswith((".xls", ".xlsx")):
                excel_path = os.path.join(root, file)
                if contains_item_8329(excel_path):
                    found_8329 = True
                    # Copy Excel to extracted/
                    extracted_name = f"{os.path.splitext(zip_file)[0]}__{file}"
                    shutil.copy(excel_path, os.path.join(EXTRACTED_DIR, extracted_name))
                    found_entries.append({
                        "Tender ZIP": zip_file,
                        "BOQ File": file
                    })
                    break

    shutil.rmtree(temp_extract_path)

    if not found_8329:
        os.remove(zip_path)
        print(f"🗑️ Deleted {zip_file} (no 8329)")

    else:
        print(f"✅ Found 8329 in {zip_file}")

if found_entries:
    df = pd.DataFrame(found_entries)
    df.to_excel(OUTPUT_FILE, index=False)
    print(f"\n📄 Saved results to {OUTPUT_FILE}")
else:
    print("\n⚠️ No BOQs with 8329 found.")
