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
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
  />
  <script src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
  <link rel="stylesheet" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css"/>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <style>
    :root {
      --primary: #3b82f6;
      --secondary: #10b981;
      --accent: #f59e0b;
      --warning: #ef4444;
      --light: #f3f4f6;
      --dark: #1f2937;
    }

    html, body {
      height: 100%;
      margin: 0;
    }

    body {
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      min-height: 100vh;
      min-width: 100vw;
      display: flex;
      flex-direction: column;
      margin: 0;
      padding: 20px;
      position: relative;
    }

    .glass-effect {
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(10px);
      border-radius: 12px;
      border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .card-hover {
      transition: all 0.3s ease;
      transform: translateY(0);
    }

    .card-hover:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    }

    details {
      margin-bottom: 1rem;
    }

    summary {
      cursor: pointer;
      font-weight: 600;
      color: white;
      margin-bottom: .5rem;
    }

    select {
      padding: 6px 10px;
      border-radius: 6px;
      border: none;
      margin-right: 10px;
      color: #111;
    }
  </style>
</head>
<body>
  <div class="w-full h-full">
    <!-- Header -->
    <div class="glass-effect p-6 mb-6 text-center">
      <h1 class="text-3xl font-bold text-white mb-2">
        Monitoring Pengambilan Part dari Mesin
      </h1>
      <p class="text-white/80">Sistem tracking pengambilan part mesin</p>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
      <div class="card-hover bg-gradient-to-br from-blue-500 to-blue-600 p-6 rounded-xl text-white">
        <div class="text-2xl font-bold mb-2" id="stat-mesin">1</div>
        <div class="text-sm">Total Mesin</div>
      </div>
      <div class="card-hover bg-gradient-to-br from-green-500 to-green-600 p-6 rounded-xl text-white">
        <div class="text-2xl font-bold mb-2" id="stat-part">3</div>
        <div class="text-sm">Total Part Dicopot</div>
      </div>
      <div class="card-hover bg-gradient-to-br from-yellow-500 to-yellow-600 p-6 rounded-xl text-white">
        <div class="text-2xl font-bold mb-2" id="stat-monitor">2</div>
        <div class="text-sm">Part Monitor (< 1 bulan)</div>
      </div>
      <div class="card-hover bg-gradient-to-br from-red-500 to-red-600 p-6 rounded-xl text-white">
        <div class="text-2xl font-bold mb-2" id="stat-warning">1</div>
        <div class="text-sm">Part Perhatian (>= 1 bulan)</div>
      </div>
    </div>

    <!-- Data Mesin -->
    <div class="glass-effect p-6 mb-8">
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-2xl font-bold text-white">Data Mesin</h2>
      </div>
      <details>
        <summary>Filter Mesin</summary>
        <input type="text" id="search-mesin" placeholder="Search...">
      </details>
      <div class="overflow-x-auto">
        <table class="w-full text-white" id="mesinTable">
          <thead class="bg-white/10">
            <tr>
              <th class="px-4 py-3 text-left">Nama Mesin</th>
              <th class="px-4 py-3 text-left">Serial Number</th>
              <th class="px-4 py-3 text-left">Tanggal Input</th>
              <th class="px-4 py-3 text-left">Jumlah Part</th>
              <th class="px-4 py-3 text-left">Aksi</th>
              <th class="px-4 py-3 text-left">Note</th>
            </tr>
          </thead>
          <tbody>
            <tr class="border-b border-white/10 hover:bg-white/5">
              <td class="px-4 py-3">Picoplus</td>
              <td class="px-4 py-3">PC424M017</td>
              <td class="px-4 py-3">31 Juli 2025</td>
              <td class="px-4 py-3">3</td>
              <td class="px-4 py-3">Belum dilengkapi</td>
              <td class="px-4 py-3">Mesin Stock</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Data Part Dicopot -->
    <div class="glass-effect p-6 mb-8">
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-2xl font-bold text-white">Data Part Dicopot</h2>
      </div>
      <details>
        <summary>Filter Part</summary>
        <input type="text" id="search-part" placeholder="Search...">
      </details>
      <div class="overflow-x-auto">
        <table class="w-full text-white" id="partTable">
          <thead class="bg-white/10">
            <tr>
              <th class="px-4 py-3 text-left">Part Number</th>
              <th class="px-4 py-3 text-left">Nama Part</th>
              <th class="px-4 py-3 text-left">Mesin</th>
              <th class="px-4 py-3 text-left">SN</th>
              <th class="px-4 py-3 text-left">Tanggal Dicopot</th>
              <th class="px-4 py-3 text-left">Aging (hari)</th>
              <th class="px-4 py-3 text-left">Tujuan</th>
              <th class="px-4 py-3 text-left">Aksi</th>
              <th class="px-4 py-3 text-left">Note</th>
            </tr>
          </thead>
          <tbody>
            <tr class="border-b border-white/10 hover:bg-white/5">
              <td class="px-4 py-3">-</td>
              <td class="px-4 py-3">DYE ROD Picoplus</td>
              <td class="px-4 py-3">Picoplus</td>
              <td class="px-4 py-3">PC424M017</td>
              <td class="px-4 py-3">31 Juli 2025</td>
              <td class="px-4 py-3">35 hari</td>
              <td class="px-4 py-3">Untuk Tosca Clinic Menteng</td>
              <td class="px-4 py-3">Menunggu part pengganti</td>
              <td class="px-4 py-3">Dikirim 1 Agustus 2025</td>
            </tr>
            <tr class="border-b border-white/10 hover:bg-white/5">
              <td class="px-4 py-3">-</td>
              <td class="px-4 py-3">Simmer Board</td>
              <td class="px-4 py-3">Picoplus</td>
              <td class="px-4 py-3">PC424M017</td>
              <td class="px-4 py-3">6 Agustus 2025</td>
              <td class="px-4 py-3">29 hari</td>
              <td class="px-4 py-3">Untuk Tosca Clinic Menteng</td>
              <td class="px-4 py-3">Menunggu part pengganti</td>
              <td class="px-4 py-3">Dikirim 6 Agustus 2025</td>
            </tr>
            <tr class="border-b border-white/10 hover:bg-white/5">
              <td class="px-4 py-3">-</td>
              <td class="px-4 py-3">Temperature Sensor</td>
              <td class="px-4 py-3">Picoplus</td>
              <td class="px-4 py-3">PC424M017</td>
              <td class="px-4 py-3">2 September 2025</td>
              <td class="px-4 py-3">2 hari</td>
              <td class="px-4 py-3">Untuk Votre Menteng</td>
              <td class="px-4 py-3">Menunggu part pengganti</td>
              <td class="px-4 py-3">Dikirim 2 September 2025, dicopot oleh rizki di logos</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <script>
    $(document).ready(function() {
      $('#mesinTable').DataTable();
      $('#partTable').DataTable();

      $('#search-mesin').on('keyup', function() {
        $('#mesinTable').DataTable().search(this.value).draw();
      });

      $('#search-part').on('keyup', function() {
        $('#partTable').DataTable().search(this.value).draw();
      });
    });
  </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=2200, scrolling=True)
