# 🚀 SIASATI Multimoda 2026 - Dashboard Analitik & GIS Interaktif

> **Sistem Informasi Angkutan dan Sarana Transportasi Indonesia (SIASATI)**  
> Pusat Data dan Teknologi Informasi (PUSDATIN) - Kementerian Perhubungan Republik Indonesia

🌐 **Live Demo Website:** [https://noviandadwitr23.github.io/siasati-kemenhub-2026/](https://noviandadwitr23.github.io/siasati-kemenhub-2026/)

---

## 📌 Ringkasan Proyek
Aplikasi analitik & visualisasi data komprehensif untuk memantau mobilitas pergerakan penumpang nasional di 5 moda transportasi utama (Bus AKAP, ASDP/Penyeberangan, Kereta Api, Laut, dan Udara) di seluruh Indonesia.

Dibangun dengan pipeline data Python (ETL & Aggregation) dan frontend interaktif modern (Tailwind CSS, Leaflet GIS, & Chart.js).

---

## 📂 Struktur Repositori & Kode Sumber

```text
siasati-kemenhub-2026/
├── index.html                    # Web App Dashboard Interaktif Utama (Production / GitHub Pages)
├── generate_dashboard.py         # [SYNTAX PYTHON] Menggabungkan data analitik ke template web
├── process_data.py               # [SYNTAX PYTHON] Pipeline ETL: Pembersihan data, deduplikasi & agregasi
├── data/
│   └── mobility_data_bundle.json # Bundle analitik terkompilasi (Timeline harian, spasial, KPI)
├── templates/
│   └── dashboard_template.html   # Template antarmuka web (Tailwind, Leaflet, Slicers, Chart.js)
├── .gitignore                    # Berkas filter git
└── README.md                     # Dokumentasi lengkap proyek
```

---

## 🐍 Sintaks & Pipeline Python

Pipeline pemrosesan dan pembuatan dashboard terdiri dari 2 script Python utama:

### 1. `process_data.py` (ETL & Analisis Agregasi)
Script ini bertugas memproses dataset mentah multimoda (`siasati_multimoda_2026.csv`):
* **Pembersihan Data:**
  * Menghapus duplikat identik (*keep first*).
  * Mengagregasikan (*sum*) duplikat yang memiliki ID prasarana, moda, dan tanggal sama namun metrik berbeda.
  * Menangani koordinat kosong (*empty lat-lon*).
* **Agregasi Metrik:**
  * Timeline harian 272 hari per moda transportasi.
  * Agregasi bulanan & pangsa pasar (*modal share*).
  * Analisis operasional puncak Mudik & Balik Lebaran (H-8 s/d H+15).
  * Analisis rasio beban armada (*load factor proxy*).
  * Pemetaan spasial 1.200+ simpul prasarana dengan koordinat presisi.
* **Output:** Menyimpan hasil kompilasi ke `data/mobility_data_bundle.json`.

```bash
# Menjalankan pembersihan dan kompilasi data
python process_data.py
```

### 2. `generate_dashboard.py` (Web Generator)
Script ini menggabungkan `data/mobility_data_bundle.json` dengan template interaktif `templates/dashboard_template.html` untuk memproduksi `index.html` yang mandiri (*standalone*), tanpa memerlukan backend server saat di-hosting di GitHub Pages.

```bash
# Menghasilkan index.html produksi
python generate_dashboard.py
```

---

## ✨ Fitur Antarmuka Dashboard

1. **🗓️ Date Range Filter & Quick Presets:**
   - Filter tanggal dinamis (`Start Date` s/d `End Date`).
   - Tombol instan preset: *All Time*, *7 Hari Terakhir*, *30 Hari Terakhir*, *Periode Puncak Lebaran*.
2. **🎛️ Multi-Slicer Moda Transportasi:**
   - 🚌 Bus (Terminal Tipe A)
   - ⛴️ ASDP (Pelabuhan Penyeberangan)
   - 🚆 Kereta Api (Stasiun KA Nasional)
   - 🚢 Laut (Pelabuhan Laut Domestik)
   - ✈️ Udara (Bandar Udara Nasional)
3. **🗺️ Peta Spasial Geografis (Leaflet GIS):**
   - Pemetaan 1.200+ simpul transportasi nasional berkoordinat presisi.
   - Popup interaktif metrik volume keberangkatan dan kedatangan penumpang.
4. **📊 Visualisasi Tren & Metrik KPI:**
   - Kartu metrik total keberangkatan, kedatangan, pergerakan total, dan rata-rata harian.
   - Grafik tren volume mobilitas harian (Chart.js) yang reaktif terhadap filter tanggal dan moda.
   - Komparasi simpul terpadat nasional (Top Hubs).

---

## 🛠️ Teknologi yang Digunakan
- **Data Engineering:** Python 3, Pandas, NumPy
- **Frontend Core:** HTML5, Modern Vanilla JavaScript (ES6+)
- **Styling:** [Tailwind CSS](https://tailwindcss.com/)
- **GIS Mapping:** [Leaflet.js](https://leafletjs.com/) & OpenStreetMap Tiles
- **Data Visualization:** [Chart.js](https://www.chartjs.org/)
- **Hosting / Deployment:** GitHub Pages

---

## 👤 Penulis / Author
- **Novianda Dwi** ([@noviandadwitr23](https://github.com/noviandadwitr23))
- Program Magang: PUSDATIN - Kementerian Ketenagakerjaan & Kementerian Perhubungan Republik Indonesia
