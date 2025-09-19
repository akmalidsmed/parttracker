import streamlit as st

# ----------------- Konfigurasi Halaman -----------------
st.set_page_config(
    page_title="Monitoring Pengambilan Part",
    page_icon="🛠️",
    layout="wide"
)

# ----------------- Setup Session Auth -----------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ----------------- Login Page -----------------
if not st.session_state.authenticated:
    st.title("🔑 Login Dashboard")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if password == "idsMED11!":   # ✅ hanya password
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ Password salah")

# ----------------- Main Page -----------------
else:
    st.sidebar.markdown("## 🔓 Status: Terautentikasi")
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()

    # ----------------- HTML Dashboard -----------------
    html_code = """
    <!DOCTYPE html>
    <html lang="id">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>Monitoring Pengambilan Part dari Mesin</title>
      <script src="https://cdn.tailwindcss.com"></script>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"/>
      <style>
        body { background-color: #f4f7fa; font-family: Arial, sans-serif; }
        .card { background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        .header { background: #1E3A8A; color: white; padding: 15px; border-radius: 12px; margin-bottom: 20px; }
        .btn { padding: 8px 12px; border-radius: 8px; }
        .btn-green { background: #10B981; color: white; }
        .btn-blue { background: #3B82F6; color: white; }
        .btn-red { background: #EF4444; color: white; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 10px; text-align: center; }
        th { background: #1E3A8A; color: white; }
      </style>
    </head>
    <body>
      <div class="header">
        <h1 class="text-2xl font-bold"><i class="fa-solid fa-screwdriver-wrench"></i> Monitoring Pengambilan Part</h1>
        <p>Sistem Pemantauan Otomatis Part dari Mesin</p>
      </div>

      <div class="grid grid-cols-3 gap-6">
        <div class="card text-center">
          <h2 class="text-xl font-semibold">Total Part</h2>
          <p class="text-3xl font-bold text-blue-600">152</p>
        </div>
        <div class="card text-center">
          <h2 class="text-xl font-semibold">Part Diambil</h2>
          <p class="text-3xl font-bold text-green-600">87</p>
        </div>
        <div class="card text-center">
          <h2 class="text-xl font-semibold">Sisa Part</h2>
          <p class="text-3xl font-bold text-red-600">65</p>
        </div>
      </div>

      <div class="card mt-6">
        <h2 class="text-xl font-bold mb-3">📋 Riwayat Pengambilan</h2>
        <table>
          <thead>
            <tr>
              <th>Tanggal</th>
              <th>Nama Part</th>
              <th>Qty</th>
              <th>Pengambil</th>
              <th>Aksi</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>2025-09-18</td>
              <td>Filter Mesin</td>
              <td>3</td>
              <td>Budi</td>
              <td>
                <button class="btn btn-blue"><i class="fa-solid fa-eye"></i> Detail</button>
                <button class="btn btn-red"><i class="fa-solid fa-trash"></i> Hapus</button>
              </td>
            </tr>
            <tr>
              <td>2025-09-17</td>
              <td>Selang Hidrolik</td>
              <td>2</td>
              <td>Siti</td>
              <td>
                <button class="btn btn-blue"><i class="fa-solid fa-eye"></i> Detail</button>
                <button class="btn btn-red"><i class="fa-solid fa-trash"></i> Hapus</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </body>
    </html>
    """

    st.components.v1.html(html_code, height=1200, scrolling=True)
