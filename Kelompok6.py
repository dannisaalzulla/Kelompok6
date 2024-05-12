import streamlit as st

def nama_senyawa(kation, anion):
    # Kamus untuk pasangan kation dan anion
    nama_anion = {
        "Cl": "Klorida",
        "Br": "Bromida",
        "I": "Iodida",
        "O": "Oksida",
        "S": "Sulfida",
        "PO4":"Fosfat",
        "NO3":"Nitrat",
        "NO2":"Nitrit",
        "CH3COO":"Asetat",
        "ClO":"Hipoklorit",
        "ClO2":"Klorit",
        "ClO3":"Klorat",
        "CN":"Sianida",
        "OH":"Hidroksida",
        "SO3":"Sulfit",
        "SO4":"Sulfat",
        "CO3":"Karbonat",
        "SiO3":"Silikat",
        "CrO4":"Kromat",
        "CrO7":"dikromat",
        "BrO":"Hipobromit",
        "BrO3":"Bromat",
        "C2O4":"Oksalat",
        "PO3":"Fosfit",
        "AsO3":"Arrneit",
        "AsO4":"Arsenit",
        "SbO3":"Antimonit",
        "SbO4":"Antimonat",
        "S2O3":"Tia sulfat",
        "MnO4":"Permanganat",
        "F":"Fluorida"}
        # Belom semua
    

    nama_kation = {
        "Na": "Natrium",
        "K": "Kalium",
        "Ca": "Kalsium",
        "Mg": "Magnesium",
        "Fe": "Besi",
        "Ag":"Perak",
        "NH4":"Amonium",
        "H":"Asam",
        "Sr":"Stronsium",
        "Ba":"Barium",
        "Al":"Aluminium",
        "Zn":"Zink",
        "Ni":"Nikel",
        "Sn":"Timah",
        "Pb":"Timbal",
        "Hg":"Raksa",
        "Cu":"Tembaga",
        "Au":"Emas",
        "Pt":"Platina"}
        # Belom semua

    # Cek ada nggak kation dan anion didalam kamus
    if anion in nama_anion and kation in nama_kation:
        nama_senyawa = nama_kation[kation] + " " + nama_anion[anion]
        return nama_senyawa
    else:
        return "Kation atau anion tidak dikenali."

# Buat di strimlit
st.title("Konversi Simbol Kation dan Anion menjadi Nama Senyawa")
kation = st.text_input("Masukkan simbol kation (misalnya Na, K, Ca, Mg,):")
anion = st.text_input("Masukkan simbol anion (misalnya Cl, Br, I, O):")

if st.button("Konversi"):
    if kation.strip() and anion.strip():
        result = nama_senyawa(kation.strip(), anion.strip())
        st.success("Nama senyawa: {}".format(result))
    else:
        st.warning("Masukkan simbol kation dan anion terlebih dahulu.")