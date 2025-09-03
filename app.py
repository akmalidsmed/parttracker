import streamlit as st

st.set_page_config(page_title="Monitoring Part - Streamlit", page_icon="📊", layout="wide")

# Load HTML langsung sebagai string
html_code = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IDSMED - Mediva Buyback Tracker</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; }
        header { background: #2563eb; color: white; padding: 20px; text-align: center; font-size: 1.5rem; font-weight: bold; }
        .container { padding: 20px; }
        .card { background: white; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
        .card h2 { font-size: 1.2rem; margin-bottom: 10px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        table, th, td { border: 1px solid #ddd; }
        th, td { padding: 10px; text-align: left; }
        th { background: #f3f4f6; }
        .status-ok { color: green; font-weight: bold; }
        .status-warning { color: orange; font-weight: bold; }
        .status-danger { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <header>
        <i class="fa-solid fa-microchip"></i> IDSMED - Mediva Buyback Tracker
    </header>
    <div class="container">
        <div class="card">
            <h2><i class="fa-solid fa-database"></i> Ringkasan Data</h2>
            <p>Total Mesin: <b>25</b></p>
            <p>Total Part Terpasang: <b>130</b></p>
            <p>Status Mesin Aktif: <span class="status-ok">20</span></p>
            <p>Status Mesin Pending: <span class="status-warning">3</span></p>
            <p>Status Mesin Rusak: <span class="status-danger">2</span></p>
        </div>
        <div class="card">
            <h2><i class="fa-solid fa-screwdriver-wrench"></i> Monitoring Mesin</h2>
            <table>
                <tr>
                    <th>No</th>
                    <th>Nama Mesin</th>
                    <th>Status</th>
                    <th>Jumlah Part</th>
                </tr>
                <tr>
                    <td>1</td>
                    <td>Laser Cynosure</td>
                    <td class="status-ok">Aktif</td>
                    <td>15</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Laser Lutronic</td>
                    <td class="status-warning">Pending</td>
                    <td>10</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Laser Candela</td>
                    <td class="status-danger">Rusak</td>
                    <td>8</td>
                </tr>
            </table>
        </div>
    </div>
</body>
</html>
"""

st.components.v1.html(html_code, height=800, scrolling=True)
