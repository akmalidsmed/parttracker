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
  <style>
    :root {
      --primary: #3b82f6;
      --secondary: #10b981;
      --accent: #f59e0b;
      --warning: #ef4444;
      --light: #f3f4f6;
      --dark: #1f2937;
    }

    body {
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      min-height: 100vh;
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

    .status-badge {
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
    }

    .status-new {
      background: #10b981;
      color: white;
    }
    .status-monitor {
      background: #f59e0b;
      color: white;
    }
    .status-warning {
      background: #ef4444;
      color: white;
    }

    .fade-in {
      animation: fadeIn 0.5s ease-in;
    }

    @keyframes fadeIn {
      from {
        opacity: 0;
        transform: translateY(20px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    /* Login admin kecil di kanan atas */
    #admin-login {
      position: fixed;
      top: 12px;
      right: 12px;
      background: rgba(255 255 255 / 0.15);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(255 255 255 / 0.2);
      border-radius: 12px;
      padding: 8px 12px;
      display: flex;
      align-items: center;
      gap: 8px;
      z-index: 1000;
      color: white;
      font-size: 14px;
      width: 180px;
    }

    #admin-login input[type="password"] {
      flex: 1;
      padding: 4px 8px;
      border-radius: 6px;
      border: none;
      outline: none;
      font-size: 14px;
      background: rgba(255 255 255 / 0.9);
      color: #111;
    }

    #admin-login button {
      background: var(--primary);
      color: white;
      border: none;
      border-radius: 6px;
      padding: 5px 10px;
      cursor: pointer;
      font-weight: 600;
      font-size: 14px;
      transition: background-color 0.3s ease;
    }

    #admin-login button:hover {
      background: #2563eb;
    }
  </style>
</head>
<body>
  <!-- Admin Login kecil kanan atas -->
  <div id="admin-login" title="Login Admin">
    <input
      type="password"
      id="admin-password"
      placeholder="PIN Admin"
      autocomplete="off"
      aria-label="PIN Admin"
    />
    <button id="login-btn" title="Login Admin">
      <i class="fas fa-lock-open"></i>
    </button>
  </div>

  <div class="max-w-7xl mx-auto">
    <!-- Header -->
    <div class="glass-effect p-6 mb-6 text-center">
      <h1 class="text-3xl font-bold text-white mb-2">
        Monitoring Pengambilan Part dari Mesin
      </h1>
      <p class="text-white/80">Sistem tracking pengambilan part mesin</p>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
      <div
        class="card-hover bg-gradient-to-br from-blue-500 to-blue-600 p-6 rounded-xl text-white"
      >
        <div class="text-2xl font-bold mb-2" id="stat-mesin">0</div>
        <div class="text-sm">Total Mesin</div>
      </div>

      <div
        class="card-hover bg-gradient-to-br from-green-500 to-green-600 p-6 rounded-xl text-white"
      >
        <div class="text-2xl font-bold mb-2" id="stat-part">0</div>
        <div class="text-sm">Total Part Dicopot</div>
      </div>

      <div
        class="card-hover bg-gradient-to-br from-yellow-500 to-yellow-600 p-6 rounded-xl text-white"
      >
        <div class="text-2xl font-bold mb-2" id="stat-monitor">0</div>
        <div class="text-sm">Part Monitor</div>
      </div>

      <div
        class="card-hover bg-gradient-to-br from-red-500 to-red-600 p-6 rounded-xl text-white"
      >
        <div class="text-2xl font-bold mb-2" id="stat-warning">0</div>
        <div class="text-sm">Part Perhatian</div>
      </div>
    </div>

    <!-- Data Mesin -->
    <div class="glass-effect p-6 mb-8">
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-2xl font-bold text-white">Data Mesin</h2>
        <button
          id="add-mesin-btn"
          class="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg transition-colors hidden"
        >
          <i class="fas fa-plus mr-2"></i>Tambah Mesin
        </button>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-white">
          <thead class="bg-white/10">
            <tr>
              <th class="px-4 py-3 text-left">Nama Mesin</th>
              <th class="px-4 py-3 text-left">Serial Number</th>
              <th class="px-4 py-3 text-left">Tanggal Input</th>
              <th class="px-4 py-3 text-left">Jumlah Part</th>
              <th class="px-4 py-3 text-left">Aksi</th>
            </tr>
          </thead>
          <tbody id="mesin-table-body">
            <tr>
              <td colspan="5" class="px-4 py-8 text-center text-white/60">
                <i class="fas fa-cogs text-3xl mb-2"></i>
                <p>Belum ada data mesin</p>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Data Part Dicopot -->
    <div class="glass-effect p-6 mb-8">
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-2xl font-bold text-white">Data Part Dicopot</h2>
        <button
          id="add-part-btn"
          class="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg transition-colors hidden"
        >
          <i class="fas fa-plus mr-2"></i>Tambah Part
        </button>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
        <select
          id="filter-mesin"
          class="px-4 py-2 rounded-lg bg-white/90 border-none focus:ring-2 focus:ring-blue-400 outline-none"
        >
          <option value="">Semua Mesin</option>
        </select>
        <select
          id="filter-sn"
          class="px-4 py-2 rounded-lg bg-white/90 border-none focus:ring-2 focus:ring-blue-400 outline-none"
        >
          <option value="">Semua SN Mesin</option>
        </select>
        <input
          type="date"
          id="filter-date-from"
          class="px-4 py-2 rounded-lg bg-white/90 border-none focus:ring-2 focus:ring-blue-400 outline-none"
        />
        <input
          type="date"
          id="filter-date-to"
          class="px-4 py-2 rounded-lg bg-white/90 border-none focus:ring-2 focus:ring-blue-400 outline-none"
        />
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-white">
          <thead class="bg-white/10">
            <tr>
              <th class="px-4 py-3 text-left">Part Number</th>
              <th class="px-4 py-3 text-left">Nama Part</th>
              <th class="px-4 py-3 text-left">Mesin</th>
              <th class="px-4 py-3 text-left">SN</th>
              <th class="px-4 py-3 text-left">Tanggal Dicopot</th>
              <th class="px-4 py-3 text-left">Tujuan</th>
              <th class="px-4 py-3 text-left">Aksi</th>
              <th class="px-4 py-3 text-left">Note</th>
            </tr>
          </thead>
          <tbody id="part-table-body">
            <tr>
              <td colspan="8" class="px-4 py-8 text-center text-white/60">
                <i class="fas fa-microchip text-3xl mb-2"></i>
                <p>Belum ada data part</p>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <script>
    // Data arrays
    let mesinData = JSON.parse(localStorage.getItem("mesinData")) || [];
    let partData = JSON.parse(localStorage.getItem("partData")) || [];
    let userRole = "viewer";
    const adminPassword = "0101";

    // DOM elements
    const addMesinBtn = document.getElementById("add-mesin-btn");
    const addPartBtn = document.getElementById("add-part-btn");
    const loginBtn = document.getElementById("login-btn");
    const adminPasswordInput = document.getElementById("admin-password");

    // Stats elements
    const statMesin = document.getElementById("stat-mesin");
    const statPart = document.getElementById("stat-part");
    const statMonitor = document.getElementById("stat-monitor");
    const statWarning = document.getElementById("stat-warning");

    // Table bodies
    const mesinTableBody = document.getElementById("mesin-table-body");
    const partTableBody = document.getElementById("part-table-body");
    const filterMesinSelect = document.getElementById("filter-mesin");
    const filterSnSelect = document.getElementById("filter-sn");

    // Initialize page
    function init() {
      updateStats();
      renderMesinTable();
      renderPartTable();
      populateFilterMesin();
      populateFilterSn();
      updateUIForRole();
    }

    // Update stats
    function updateStats() {
      statMesin.textContent = mesinData.length;
      statPart.textContent = partData.length;

      // Count monitor and warning parts
      const now = new Date();
      let monitorCount = 0;
      let warningCount = 0;
      partData.forEach((part) => {
        const diffDays = Math.floor(
          (now - new Date(part.tanggalPencopotan)) / (1000 * 60 * 60 * 24)
        );
        if (diffDays > 30) warningCount++;
        else if (diffDays > 7) monitorCount++;
      });
      statMonitor.textContent = monitorCount;
      statWarning.textContent = warningCount;
    }

    // Render mesin table dengan dropdown status part
    function renderMesinTable() {
      mesinTableBody.innerHTML = "";
      if (mesinData.length === 0) {
        mesinTableBody.innerHTML = `
          <tr>
            <td colspan="5" class="px-4 py-8 text-center text-white/60">
              <i class="fas fa-cogs text-3xl mb-2"></i>
              <p>Belum ada data mesin</p>
            </td>
          </tr>
        `;
        return;
      }
      mesinData.forEach((mesin, index) => {
        // Hitung jumlah part dicopot untuk mesin ini
        const partsForMesin = partData.filter((p) => p.mesinId === mesin.id);
        const partCount = partsForMesin.length;

        // Ambil status part mesin jika sudah disimpan, default "Part belum dilengkapi"
        const statusKey = `mesinStatus_${mesin.id}`;
        const savedStatus = localStorage.getItem(statusKey) || "belum";

        const tr = document.createElement("tr");
        tr.className = "border-b border-white/10 hover:bg-white/5";

        tr.innerHTML = `
          <td class="px-4 py-3">${mesin.nama}</td>
          <td class="px-4 py-3">${mesin.sn}</td>
          <td class="px-4 py-3">${new Date(mesin.tanggalInput).toLocaleDateString("id-ID")}</td>
          <td class="px-4 py-3">${partCount}</td>
          <td class="px-4 py-3">
            <select onchange="updateMesinStatus('${mesin.id}', this.value)" class="bg-gray-800 text-white rounded px-2 py-1 w-full">
              <option value="belum" ${savedStatus === "belum" ? "selected" : ""}>Part belum dilengkapi</option>
              <option value="sebagian" ${savedStatus === "sebagian" ? "selected" : ""}>Part dilengkapi sebagian</option>
              <option value="sepenuhnya" ${savedStatus === "sepenuhnya" ? "selected" : ""}>Part dilengkapi sepenuhnya</option>
            </select>
          </td>
        `;
        mesinTableBody.appendChild(tr);
      });
    }

    // Fungsi simpan status part mesin ke localStorage
    function updateMesinStatus(mesinId, status) {
      localStorage.setItem(`mesinStatus_${mesinId}`, status);
    }

    // Render part table dengan kolom baru dan filter
    function renderPartTable() {
      partTableBody.innerHTML = "";
      const filterMesin = filterMesinSelect.value;
      const filterSn = filterSnSelect.value;
      const filterDateFrom = document.getElementById("filter-date-from").value;
      const filterDateTo = document.getElementById("filter-date-to").value;

      let filteredParts = partData;

      if (filterMesin) {
        filteredParts = filteredParts.filter((p) => p.mesinId === filterMesin);
      }

      if (filterSn) {
        filteredParts = filteredParts.filter((p) => {
          const mesin = mesinData.find((m) => m.id === p.mesinId);
          return mesin && mesin.sn === filterSn;
        });
      }

      if (filterDateFrom) {
        filteredParts = filteredParts.filter(
          (p) => new Date(p.tanggalPencopotan) >= new Date(filterDateFrom)
        );
      }

      if (filterDateTo) {
        filteredParts = filteredParts.filter(
          (p) => new Date(p.tanggalPencopotan) <= new Date(filterDateTo)
        );
      }

      if (filteredParts.length === 0) {
        partTableBody.innerHTML = `
          <tr>
            <td colspan="8" class="px-4 py-8 text-center text-white/60">
              <i class="fas fa-microchip text-3xl mb-2"></i>
              <p>Belum ada data part</p>
            </td>
          </tr>
        `;
        return;
      }

      filteredParts.forEach((part, index) => {
        const mesin = mesinData.find((m) => m.id === part.mesinId);
        const tujuan = part.tujuan || "-";
        const note = part.note || "";
        const sn = mesin ? mesin.sn : "-";

        const tr = document.createElement("tr");
        tr.className = "border-b border-white/10 hover:bg-white/5";
        tr.innerHTML = `
          <td class="px-4 py-3">${part.partNumber || "-"}</td>
          <td class="px-4 py-3">${part.nama}</td>
          <td class="px-4 py-3">${mesin ? mesin.nama : "Unknown"}</td>
          <td class="px-4 py-3">${sn}</td>
          <td class="px-4 py-3">${new Date(part.tanggalPencopotan).toLocaleDateString("id-ID")}</td>
          <td class="px-4 py-3">${tujuan}</td>
          <td class="px-4 py-3">
            <button onclick="alert('Lihat detail part belum diimplementasikan')" class="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded mr-2">
              <i class="fas fa-eye"></i
"""

st.components.v1.html(html_code, height=1000, scrolling=True)
