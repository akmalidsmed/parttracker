import streamlit as st

st.set_page_config(page_title="Monitoring Pengambilan Part", page_icon="🛠️", layout="wide")

# Initialize session state for authentication
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Password protection
def check_password():
    def password_entered():
        if st.session_state["password"] == "idsMED11!":
            st.session_state.authenticated = True
            del st.session_state["password"]  # Don't store password
        else:
            st.session_state.authenticated = False

    if not st.session_state.authenticated:
        # Login form
        st.markdown("""
        <div style='display: flex; justify-content: center; align-items: center; min-height: 80vh; 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);'>
            <div style='background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px); 
                        border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.2); 
                        padding: 40px; text-align: center; min-width: 400px;'>
                <h1 style='color: white; margin-bottom: 30px; font-size: 2.5rem;'>🛠️</h1>
                <h2 style='color: white; margin-bottom: 30px;'>Monitoring Pengambilan Part</h2>
                <p style='color: rgba(255,255,255,0.8); margin-bottom: 30px;'>Masukkan password untuk mengakses sistem</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Center the password input
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.text_input("Password", type="password", on_change=password_entered, key="password")
            
        if "password" in st.session_state and st.session_state.get("password"):
            if st.session_state["password"] != "idsMED11!":
                st.error("❌ Password salah!")
        
        return False
    
    return True

# Main application
if check_password():
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

        select, input[type="text"] {
          padding: 6px 10px;
          border-radius: 6px;
          border: none;
          margin-right: 10px;
          color: #111;
        }

        .logout-btn {
          position: absolute;
          top: 20px;
          right: 20px;
          background: rgba(255, 255, 255, 0.2);
          color: white;
          border: 1px solid rgba(255, 255, 255, 0.3);
          padding: 8px 16px;
          border-radius: 8px;
          cursor: pointer;
          transition: all 0.3s ease;
        }

        .logout-btn:hover {
          background: rgba(255, 255, 255, 0.3);
        }
      </style>
    </head>
    <body>
      <button class="logout-btn" onclick="logout()">
        <i class="fas fa-sign-out-alt"></i> Logout
      </button>

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
            <select id="filter-mesin-nama">
              <option value="">Semua Nama Mesin</option>
              <option value="Picoplus">Picoplus</option>
            </select>
            <select id="filter-mesin-sn">
              <option value="">Semua Serial Number</option>
              <option value="PC424M017">PC424M017</option>
            </select>
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
            <select id="filter-part-number">
              <option value="">Semua Part Number</option>
              <option value="-">-</option>
            </select>
            <select id="filter-part-nama">
              <option value="">Semua Nama Part</option>
              <option value="DYE ROD Picoplus">DYE ROD Picoplus</option>
              <option value="Simmer Board">Simmer Board</option>
              <option value="Temperature Sensor">Temperature Sensor</option>
            </select>
            <select id="filter-part-mesin">
              <option value="">Semua Mesin</option>
              <option value="Picoplus">Picoplus</option>
            </select>
            <select id="filter-part-sn">
              <option value="">Semua SN</option>
              <option value="PC424M017">PC424M017</option>
            </select>
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
        function filterTable(tableId, filters) {
          const table = document.getElementById(tableId);
          const trs = table.getElementsByTagName('tr');
          for (let i = 1; i < trs.length; i++) {
            let show = true;
            const tds = trs[i].getElementsByTagName('td');
            filters.forEach((filter, index) => {
              if (filter.value && !tds[index].innerText.includes(filter.value)) {
                show = false;
              }
            });
            trs[i].style.display = show ? '' : 'none';
          }
        }

        function logout() {
          if (confirm('Apakah Anda yakin ingin logout?')) {
            // Send message to Streamlit to reset authentication
            window.parent.postMessage({type: 'logout'}, '*');
          }
        }

        // Listen for logout message from Streamlit
        window.addEventListener('message', function(event) {
          if (event.data.type === 'logout') {
            logout();
          }
        });

        document.getElementById('filter-mesin-nama').addEventListener('change', () => {
          filterTable('mesinTable', [
            document.getElementById('filter-mesin-nama'),
            document.getElementById('filter-mesin-sn')
          ]);
        });
        document.getElementById('filter-mesin-sn').addEventListener('change', () => {
          filterTable('mesinTable', [
            document.getElementById('filter-mesin-nama'),
            document.getElementById('filter-mesin-sn')
          ]);
        });

        document.getElementById('filter-part-number').addEventListener('change', () => {
          filterTable('partTable', [
            document.getElementById('filter-part-number'),
            document.getElementById('filter-part-nama'),
            document.getElementById('filter-part-mesin'),
            document.getElementById('filter-part-sn')
          ]);
        });
        document.getElementById('filter-part-nama').addEventListener('change', () => {
          filterTable('partTable', [
            document.getElementById('filter-part-number'),
            document.getElementById('filter-part-nama'),
            document.getElementById('filter-part-mesin'),
            document.getElementById('filter-part-sn')
          ]);
        });
        document.getElementById('filter-part-mesin').addEventListener('change', () => {
          filterTable('partTable', [
            document.getElementById('filter-part-number'),
            document.getElementById('filter-part-nama'),
            document.getElementById('filter-part-mesin'),
            document.getElementById('filter-part-sn')
          ]);
        });
        document.getElementById('filter-part-sn').addEventListener('change', () => {
          filterTable('partTable', [
            document.getElementById('filter-part-number'),
            document.getElementById('filter-part-nama'),
            document.getElementById('filter-part-mesin'),
            document.getElementById('filter-part-sn')
          ]);
        });
      </script>
    </body>
    </html>
    """

    # Add logout functionality in sidebar
    with st.sidebar:
        st.markdown("### 🛠️ Monitoring System")
        st.markdown("---")
        if st.button("🚪 Logout", type="secondary", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()

    st.components.v1.html(html_code, height=2200, scrolling=True)
