import streamlit as st

st.set_page_config(page_title="Monitoring Pengambilan Part", page_icon="🛠️", layout="wide")

html_code = """
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Monitoring Pengambilan Part dari Mesin</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body {
      font-family: 'Inter', sans-serif;
      background-color: #ffffff;
      color: #1f2937;
      margin: 0;
      padding: 2rem 1rem;
      min-height: 100vh;
    }
    header {
      max-width: 1200px;
      margin: 0 auto 2rem auto;
      text-align: center;
    }
    header h1 {
      font-size: 2.5rem;
      font-weight: 800;
      color: #111827;
      margin-bottom: 0.25rem;
    }
    header p {
      font-size: 1.125rem;
      color: #6b7280;
    }
    .stats {
      max-width: 1200px;
      margin: 0 auto 3rem auto;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1.5rem;
    }
    .stat-card {
      background: #f3f4f6;
      border-radius: 12px;
      padding: 1.5rem;
      box-shadow: 0 1px 3px rgb(0 0 0 / 0.1);
      text-align: center;
      transition: box-shadow 0.3s ease;
      cursor: default;
    }
    .stat-card:hover {
      box-shadow: 0 8px 20px rgb(0 0 0 / 0.15);
    }
    .stat-number {
      font-size: 2.75rem;
      font-weight: 900;
      color: #111827;
      margin-bottom: 0.25rem;
      font-feature-settings: "tnum";
      font-variant-numeric: tabular-nums;
    }
    .stat-label {
      font-size: 0.875rem;
      font-weight: 600;
      color: #6b7280;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    section {
      max-width: 1200px;
      margin: 0 auto 3rem auto;
      background: #ffffff;
      border-radius: 12px;
      box-shadow: 0 1px 6px rgb(0 0 0 / 0.1);
      padding: 2rem;
    }
    section h2 {
      font-size: 1.75rem;
      font-weight: 700;
      color: #111827;
      margin-bottom: 1rem;
      border-bottom: 2px solid #e5e7eb;
      padding-bottom: 0.5rem;
    }
    details summary {
      font-weight: 600;
      font-size: 1rem;
      color: #374151;
      cursor: pointer;
      margin-bottom: 1rem;
      outline: none;
      list-style: none;
    }
    details[open] summary::after {
      content: "▲";
      float: right;
      font-size: 0.75rem;
      color: #6b7280;
    }
    details summary::after {
      content: "▼";
      float: right;
      font-size: 0.75rem;
      color: #6b7280;
    }
    .filters {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 1.5rem;
    }
    select {
      flex: 1 1 180px;
      padding: 0.5rem 0.75rem;
      border: 1px solid #d1d5db;
      border-radius: 8px;
      font-size: 1rem;
      color: #374151;
      background-color: #f9fafb;
      transition: border-color 0.2s ease;
    }
    select:focus {
      outline: none;
      border-color: #2563eb;
      box-shadow: 0 0 0 3px rgb(37 99 235 / 0.3);
      background-color: white;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.95rem;
      color: #374151;
    }
    thead tr {
      background-color: #f9fafb;
      border-bottom: 2px solid #e5e7eb;
    }
    th, td {
      padding: 0.75rem 1rem;
      text-align: left;
      border-bottom: 1px solid #e5e7eb;
      vertical-align: middle;
    }
    tbody tr:hover {
      background-color: #f3f4f6;
    }
    @media (max-width: 640px) {
      .filters {
        flex-direction: column;
      }
      select {
        flex: 1 1 100%;
      }
    }
  </style>
</head>
<body>
  <header>
    <h1>Monitoring Pengambilan Part dari Mesin</h1>
    <p>Sistem tracking pengambilan part mesin</p>
  </header>

  <section class="stats" aria-label="Statistik Pengambilan Part">
    <div class="stat-card" role="region" aria-labelledby="total-mesin-label">
      <div class="stat-number" id="total-mesin">1</div>
      <div class="stat-label" id="total-mesin-label">Total Mesin</div>
    </div>
    <div class="stat-card" role="region" aria-labelledby="total-part-label">
      <div class="stat-number" id="total-part">3</div>
      <div class="stat-label" id="total-part-label">Total Part Dicopot</div>
    </div>
    <div class="stat-card" role="region" aria-labelledby="part-monitor-label">
      <div class="stat-number" id="part-monitor">2</div>
      <div class="stat-label" id="part-monitor-label">Part Monitor (&lt; 1 bulan)</div>
    </div>
    <div class="stat-card" role="region" aria-labelledby="part-perhatian-label">
      <div class="stat-number" id="part-perhatian">1</div>
      <div class="stat-label" id="part-perhatian-label">Part Perhatian (&ge; 1 bulan)</div>
    </div>
  </section>

  <section aria-labelledby="data-mesin-title">
    <h2 id="data-mesin-title">Data Mesin</h2>
    <details open>
      <summary>Filter Mesin</summary>
      <div class="filters">
        <select id="filter-mesin-nama" aria-label="Filter Nama Mesin">
          <option value="">Semua Nama Mesin</option>
          <option value="Picoplus">Picoplus</option>
        </select>
        <select id="filter-mesin-sn" aria-label="Filter Serial Number Mesin">
          <option value="">Semua Serial Number</option>
          <option value="PC424M017">PC424M017</option>
        </select>
      </div>
    </details>
    <div style="overflow-x:auto;">
      <table id="mesinTable" role="table" aria-label="Tabel Data Mesin">
        <thead>
          <tr>
            <th>Nama Mesin</th>
            <th>Serial Number</th>
            <th>Tanggal Input</th>
            <th>Jumlah Part</th>
            <th>Aksi</th>
            <th>Note</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Picoplus</td>
            <td>PC424M017</td>
            <td>31 Juli 2025</td>
            <td>3</td>
            <td>Belum dilengkapi</td>
            <td>Mesin Stock</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section aria-labelledby="data-part-title">
    <h2 id="data-part-title">Data Part Dicopot</h2>
    <details open>
      <summary>Filter Part</summary>
      <div class="filters">
        <select id="filter-part-number" aria-label="Filter Part Number">
          <option value="">Semua Part Number</option>
          <option value="-">-</option>
        </select>
        <select id="filter-part-nama" aria-label="Filter Nama Part">
          <option value="">Semua Nama Part</option>
          <option value="DYE ROD Picoplus">DYE ROD Picoplus</option>
          <option value="Simmer Board">Simmer Board</option>
          <option value="Temperature Sensor">Temperature Sensor</option>
        </select>
        <select id="filter-part-mesin" aria-label="Filter Mesin">
          <option value="">Semua Mesin</option>
          <option value="Picoplus">Picoplus</option>
        </select>
        <select id="filter-part-sn" aria-label="Filter Serial Number">
          <option value="">Semua SN</option>
          <option value="PC424M017">PC424M017</option>
        </select>
      </div>
    </details>
    <div style="overflow-x:auto;">
      <table id="partTable" role="table" aria-label="Tabel Data Part Dicopot">
        <thead>
          <tr>
            <th>Part Number</th>
            <th>Nama Part</th>
            <th>Mesin</th>
            <th>SN</th>
            <th>Tanggal Dicopot</th>
            <th>Aging (hari)</th>
            <th>Tujuan</th>
            <th>Aksi</th>
            <th>Note</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>-</td>
            <td>DYE ROD Picoplus</td>
            <td>Picoplus</td>
            <td>PC424M017</td>
            <td>31 Juli 2025</td>
            <td>35 hari</td>
            <td>Untuk Tosca Clinic Menteng</td>
            <td>Menunggu part pengganti</td>
            <td>Dikirim 1 Agustus 2025</td>
          </tr>
          <tr>
            <td>-</td>
            <td>Simmer Board</td>
            <td>Picoplus</td>
            <td>PC424M017</td>
            <td>6 Agustus 2025</td>
            <td>29 hari</td>
            <td>Untuk Tosca Clinic Menteng</td>
            <td>Menunggu part pengganti</td>
            <td>Dikirim 6 Agustus 2025</td>
          </tr>
          <tr>
            <td>-</td>
            <td>Temperature Sensor</td>
            <td>Picoplus</td>
            <td>PC424M017</td>
            <td>2 September 2025</td>
            <td>2 hari</td>
            <td>Untuk Votre Menteng</td>
            <td>Menunggu part pengganti</td>
            <td>Dikirim 2 September 2025, dicopot oleh rizki di logos</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <script>
    function filterTable(tableId, filters) {
      const table = document.getElementById(tableId);
      const trs = table.getElementsByTagName('tr');
      for (let i = 1; i < trs.length; i++) {
        let show = true;
        const tds = trs[i].getElementsByTagName('td');
        filters.forEach((filter, index) => {
          if (filter.value && !tds[index].innerText.toLowerCase().includes(filter.value.toLowerCase())) {
            show = false;
          }
        });
        trs[i].style.display = show ? '' : 'none';
      }
    }

    // Mesin filters
    const mesinFilters = [
      document.getElementById('filter-mesin-nama'),
      document.getElementById('filter-mesin-sn')
    ];
    mesinFilters.forEach(filter => {
      filter.addEventListener('change', () => {
        filterTable('mesinTable', mesinFilters);
      });
    });

    // Part filters
    const partFilters = [
      document.getElementById('filter-part-number'),
      document.getElementById('filter-part-nama'),
      document.getElementById('filter-part-mesin'),
      document.getElementById('filter-part-sn')
    ];
    partFilters.forEach(filter => {
      filter.addEventListener('change', () => {
        filterTable('partTable', partFilters);
      });
    });
  </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=2200, scrolling=True)
