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
      <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
      />
      <style>
        body { font-family: Arial, sans-serif; background-color: #f9fafb; }
        .header { background-color: #1e3a8a; color: white; padding: 20px; text-align: center; }
        .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); margin: 10px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px; }
      </style>
    </head>
    <body>
      <div class="header">
        <h1 class="text-3xl font-bold">📊 Monitoring Pengambilan Part dari Mesin</h1>
        <p>Dashboard pemantauan real-time</p>
      </div>

      <div class="grid">
        <div class="card">
          <h2 class="text-xl font-semibold mb-2"><i class="fas fa-cogs"></i> Total Part</h2>
          <p class="text-2xl font-bold text-blue-700">128</p>
        </div>

        <div class="card">
          <h2 class="text-xl font-semibold mb-2"><i class="fas fa-check-circle"></i> Sudah Diambil</h2>
          <p class="text-2xl font-bold text-green-600">85</p>
        </div>

        <div class="card">
          <h2 class="text-xl font-semibold mb-2"><i class="fas fa-box"></i> Belum Diambil</h2>
          <p class="text-2xl font-bold text-red-600">43</p>
        </div>
      </div>

      <div class="card" style="margin: 20px;">
        <h2 class="text-xl font-semibold mb-2"><i class="fas fa-table"></i> Detail Pengambilan</h2>
        <table class="min-w-full border border-gray-300">
          <thead>
            <tr class="bg-gray-100">
              <th class="border px-4 py-2">No</th>
              <th class="border px-4 py-2">Nama Part</th>
              <th class="border px-4 py-2">Status</th>
              <th class="border px-4 py-2">Tanggal</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="border px-4 py-2">1</td>
              <td class="border px-4 py-2">Sensor Lutronic A1</td>
              <td class="border px-4 py-2 text-green-600">✅ Diambil</td>
              <td class="border px-4 py-2">2025-09-15</td>
            </tr>
            <tr>
              <td class="border px-4 py-2">2</td>
              <td class="border px-4 py-2">Module Laser B2</td>
              <td class="border px-4 py-2 text-red-600">❌ Belum</td>
              <td class="border px-4 py-2">-</td>
            </tr>
          </tbody>
        </table>
      </div>
    </body>
    </html>
    """

    # Render HTML ke Streamlit
    st.components.v1.html(html_code, height=2200, scrolling=True)
