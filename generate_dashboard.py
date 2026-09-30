"""
generate_dashboard.py
=============================================================================
SIASATI Kemenhub 2026 - Production Dashboard Generator
=============================================================================
Script ini menggabungkan data analitik mobilitas multimoda (data/mobility_data_bundle.json)
dengan template frontend interaktif (templates/dashboard_template.html)
untuk menghasilkan aplikasi web standalone production (index.html).

Fitur Dashboard yang dihasilkan:
- Filter Rentang Tanggal Interaktif (Date Picker: Start & End Date)
- Quick Presets (All Time, 7 Hari Terakhir, 30 Hari Terakhir, Peak Lebaran, dll)
- Multi-Slicer Moda Transportasi (Bus, ASDP, Kereta Api, Laut, Udara)
- Slicer Arah Arus (Total, Datang, Berangkat) & Slicer 40 Provinsi
- Peta Interaktif Spasial GIS (Leaflet) dengan 1.200+ Node Simpul Transportasi
- Grafik Tren Harian Reaktif & Analisis Operasional Puncak Lebaran (Chart.js)
=============================================================================
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "mobility_data_bundle.json")
TEMPLATE_PATH = os.path.join(BASE_DIR, "templates", "dashboard_template.html")
OUTPUT_HTML = os.path.join(BASE_DIR, "index.html")

def build_dashboard():
    print("=" * 70)
    print("SIASATI KEMENHUB 2026 - GENERATING PRODUCTION DASHBOARD")
    print("=" * 70)

    # 1. Validasi keberadaan file
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"File data bundle tidak ditemukan: {DATA_PATH}")
    if not os.path.exists(TEMPLATE_PATH):
        raise FileNotFoundError(f"File template tidak ditemukan: {TEMPLATE_PATH}")

    # 2. Baca data bundle
    print(f"[1/4] Membaca data bundle dari: {DATA_PATH}")
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data_bundle = json.load(f)
    print(f"      [OK] Berhasil memuat data: {len(data_bundle.get('daily_timeline', []))} hari observasi")
    print(f"      [OK] Node spasial: {len(data_bundle.get('spatial_nodes', []))} simpul transportasi")

    # 3. Baca template HTML
    print(f"[2/4] Membaca template UI dari: {TEMPLATE_PATH}")
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    # 4. Injeksi data bundle JSON ke dalam template
    print("[3/4] Melakukan injeksi data ke dalam template web...")
    json_data_str = json.dumps(data_bundle, ensure_ascii=False)
    output_content = template.replace("__DATA_PLACEHOLDER__", json_data_str)

    # 5. Tulis output HTML
    print(f"[4/4] Menyimpan dashboard interaktif ke: {OUTPUT_HTML}")
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(output_content)

    size_kb = os.path.getsize(OUTPUT_HTML) / 1024
    print("-" * 70)
    print(f"[OK] SUKSES! File {OUTPUT_HTML} berhasil digenerate.")
    print(f"[OK] Ukuran file: {size_kb:.1f} KB (Siap di-hosting di GitHub Pages)")
    print("=" * 70)

if __name__ == "__main__":
    build_dashboard()
