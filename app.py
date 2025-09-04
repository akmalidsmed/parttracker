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
      background-color: #f9fafb;
      color: #111827;
      margin: 0;
      padding: 20px;
      min-height: 100vh;
    }
    h1, h2 {
      font-weight: 700;
    }
    .card {
      background: white;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgb(0 0 0 / 0.05);
      padding: 1.5rem;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .card:hover {
      transform: translateY(-6px);
      box-shadow: 0 10px 25px rgb(0 0 0 / 0.1);
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
    }
    thead {
      background-color: #e5e7eb;
    }
    th, td {
      padding: 0.75rem 1rem;
      text-align: left;
      border-bottom: 1px solid #d1d5db;
    }
    tbody tr:hover {
      background-color: #f3f4f6;
    }
    details summary {
      cursor: pointer;
      font-weight: 600;
      margin-bottom: 0.75rem;
      outline: none;
    }
    select {
      padding: 0.4rem 0.75rem;
      border: 1px solid #d1d5db;
      border-radius: 6px;
      margin-right: 0.75rem;
      font-size: 0.9rem;
      color: #374151;
      background-color: white;
      transition: border-color 0.2s ease;
    }
    select:focus {
      outline: none;
      border-color: #3b82f6;
      box-shadow: 0 0 0 3px rgb(59 130 246 / 0.3);
    }
    .filters {
      margin-bottom: 1rem;
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
    }
    @media (max-width: 640px) {
      .filters {
        flex-direction: column;
      }
      select {
        margin-right: 0;
        width: 100%;
      }
    }
  </style>
</head>
<body>
  <header class="mb-8 text-center">
    <h1 class="text-4xl text-gray-900 mb-2">Monitoring Pengambilan Part dari Mesin</h1>
    <p class="text-gray-600 text-lg">Sistem tracking pengambilan part mesin</p>
  </header>

  <!-- Stats Cards -->
  <section class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6 mb-10">
    <div class="card bg-blue-50 text-blue-700">
      <div class="text-3xl font-extrabold mb-1" id="stat-mesin">1</div>
      <div class="uppercase tracking-wide text-sm font-semibold">Total Mesin</div>
    </div>
    <div class="card bg-green-50 text-green-700">
      <div class="text-3xl font-extrabold mb-1" id="stat-part">3</div>
      <div class="uppercase tracking-wide text-sm font-semibold">Total Part Dicopot</div>
    </div>
    <div class="card bg-yellow-50 text-yellow-700">
      <div class="text-3xl font-extrabold mb-1" id="stat-monitor">2</div>
      <div class="uppercase tracking-wide text-sm font-semibold">Part Monitor (&lt; 1 bulan)</div>
    </div>
    <div class="card bg-red-50 text-red-700">
      <div class="text-3xl font-extrabold mb-1" id="stat-warning">1</div>
      <div class="uppercase tracking-wide text-sm font-semibold">Part Perhatian (&ge; 1 bulan)</div>
    </div>
  </section>

  <!-- Data Mesin -->
  <section class="card mb-10">
    <h2 class="text-2xl mb-4">Data Mesin</h2>
    <details class="mb-4" open>
      <summary>Filter Mesin</summary>
      <div class="filters mt-3">
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
    <div class="overflow-x-auto">
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

  <!-- Data Part Dicopot -->
  <section class="card">
    <h2 class="text-2xl mb-4">Data Part Dicopot</h2>
    <details class="mb-4" open>
      <summary>Filter Part</summary>
      <div class="filters mt-3">
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
    <div class="overflow-x-auto">
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
