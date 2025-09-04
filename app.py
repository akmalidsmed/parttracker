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
    /* Fullscreen & reset */
    html, body {
      height: 100%;
      margin: 0;
      padding: 0;
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(135deg, #ff6ec4 0%, #7873f5 100%);
      color: #fff;
      overflow-y: auto;
    }
    body {
      display: flex;
      flex-direction: column;
      min-height: 100vh;
      padding: 2rem 3rem;
    }
    header {
      text-align: center;
      margin-bottom: 3rem;
      text-shadow: 0 2px 6px rgba(0,0,0,0.3);
    }
    header h1 {
      font-size: 3rem;
      font-weight: 900;
      margin-bottom: 0.25rem;
      letter-spacing: 0.05em;
    }
    header p {
      font-size: 1.25rem;
      font-weight: 500;
      opacity: 0.85;
    }
    .stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 2rem;
      max-width: 1200px;
      margin: 0 auto 4rem auto;
      width: 100%;
    }
    .stat-card {
      border-radius: 20px;
      padding: 2rem 1.5rem;
      font-weight: 700;
      font-size: 2.5rem;
      text-align: center;
      box-shadow: 0 8px 20px rgb(0 0 0 / 0.25);
      cursor: default;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      user-select: none;
    }
    .stat-label {
      font-size: 1rem;
      font-weight: 600;
      margin-top: 0.5rem;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      opacity: 0.9;
    }
    .stat-blue { background: #3b82f6; box-shadow: 0 8px 20px #2563ebcc; }
    .stat-green { background: #10b981; box-shadow: 0 8px 20px #059669cc; }
    .stat-yellow { background: #fbbf24; box-shadow: 0 8px 20px #d97706cc; color: #1f2937; }
    .stat-red { background: #ef4444; box-shadow: 0 8px 20px #b91c1ccc; }
    .stat-card:hover {
      transform: translateY(-10px);
      box-shadow: 0 15px 35px rgb(0 0 0 / 0.4);
    }

    section {
      max-width: 1200px;
      margin: 0 auto 4rem auto;
      background: rgba(255 255 255 / 0.15);
      border-radius: 20px;
      padding: 2rem 2.5rem;
      box-shadow: 0 8px 30px rgb(0 0 0 / 0.2);
      backdrop-filter: blur(12px);
      color: #fff;
    }
    section h2 {
      font-size: 2rem;
      font-weight: 800;
      margin-bottom: 1.5rem;
      text-shadow: 0 1px 3px rgba(0,0,0,0.4);
    }
    details summary {
      font-weight: 700;
      font-size: 1.125rem;
      cursor: pointer;
      margin-bottom: 1rem;
      list-style: none;
      user-select: none;
      text-shadow: 0 1px 2px rgba(0,0,0,0.3);
    }
    details[open] summary::after {
      content: "▲";
      float: right;
      font-size: 0.9rem;
      opacity: 0.7;
    }
    details summary::after {
      content: "▼";
      float: right;
      font-size: 0.9rem;
      opacity: 0.7;
    }
    .filters {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 2rem;
    }
    select {
      flex: 1 1 180px;
      padding: 0.6rem 1rem;
      border-radius: 12px;
      border: none;
      font-size: 1rem;
      font-weight: 600;
      color: #1f2937;
      background: #fef3c7;
      box-shadow: 0 2px 8px rgb(0 0 0 / 0.15);
      transition: box-shadow 0.3s ease;
      cursor: pointer;
      user-select: none;
    }
    select:focus {
      outline: none;
      box-shadow: 0 0 0 4px #fbbf24aa;
      background: #fde68a;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 1rem;
      color: #1f2937;
      background: #fef3c7;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 6px 20px rgb(0 0 0 / 0.15);
    }
    thead tr {
      background: #f59e0b;
      color: #1f2937;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    th, td {
      padding: 1rem 1.25rem;
      border-bottom: 1px solid #fcd34d;
      vertical-align: middle;
    }
    tbody tr:hover {
      background: #fde68a;
      cursor: default;
    }
    @media (max-width: 768px) {
      body {
        padding: 1.5rem 1rem;
      }
      header h1 {
        font-size: 2rem;
      }
      section {
        padding: 1.5rem 1.5rem;
      }
      .stat-card {
        font-size: 2rem;
        padding: 1.5rem 1rem;
      }
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
    <div class="stat-card stat-blue" role="region" aria-labelledby="total-mesin-label">
      <div class="stat-number" id="total-mesin">1</div>
      <div class="stat-label" id="total-mesin-label">Total Mesin</div>
    </div>
    <div class="stat-card stat-green" role="region" aria-labelledby="total-part-label">
      <div class="stat-number" id="total-part">3</div>
      <div class="stat-label" id="total-part-label">Total Part Dicopot</div>
    </div>
    <div class="stat-card stat-yellow" role="region" aria-labelledby="part-monitor-label">
      <div class="stat-number" id="part-monitor">2</div>
      <div class="stat-label" id="part-monitor-label">Part Monitor (&lt; 1 bulan)</div>
    </div>
    <div class="stat-card stat-red" role="region" aria-labelledby="part-perhatian-label">
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

st.components.v1.html(html_code, height=1000, scrolling=True)
