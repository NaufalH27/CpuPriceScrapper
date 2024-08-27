from bs4 import BeautifulSoup
import os
from . import string_helper



def get_city_list_by_first_letter(text):
    try:
        city_dict = get_city_dictionary_by_initial()
        clean_text = string_helper.remove_substring(text, "Kab. ").strip()
        first_letter = clean_text[0]
        return city_dict[first_letter]
    except:
        return None



#this is the final result after running the generate_city_dictionary() script, just use this for performance
def get_city_dictionary_by_initial():
    return {
    'A': ['Kab. Aceh Barat', 'Kab. Aceh Barat Daya', 'Kab. Aceh Besar', 'Kab. Aceh Jaya', 'Kab. Aceh Selatan', 'Kab. Aceh Singkil', 'Kab. Aceh Tamiang', 'Kab. Aceh Tengah', 'Kab. Aceh Tenggara', 'Kab. Aceh Timur', 'Kab. Aceh Utara', 'Kab. Agam', 'Kab. Alor', 'Kab. Asahan', 'Kab. Asmat', 'Kab. Kotabaru', 'Kab. Kotawaringin Barat', 'Kab. Kotawaringin Timur', 'Ambon'], 
    'B': ['Bali', 'Banten', 'Bengkulu', 'Bandung', 'Kab. Badung', 'Kab. Balangan', 'Kab. Bandung', 'Kab. Bandung Barat', 'Kab. Banggai', 'Kab. Banggai Kepulauan', 'Kab. Banggai Laut', 'Kab. Bangka', 'Kab. Bangka Barat', 'Kab. Bangkalan', 'Kab. Bangka Selatan', 'Kab. Bangka Tengah', 'Kab. Bangli', 'Kab. Banjar', 'Kab. Banjarnegara', 'Kab. Bantaeng', 'Kab. Bantul', 'Kab. Banyuasin', 'Kab. Banyumas', 'Kab. Banyuwangi', 'Kab. Barito Kuala', 'Kab. Barito Selatan', 'Kab. Barito Timur', 'Kab. Barito Utara', 'Kab. Barru', 'Kab. Batang', 'Kab. Batanghari', 'Kab. Batu Bara', 'Kab. Baturaja', 'Kab. Bekasi', 'Kab. Belitung', 'Kab. Belitung Timur', 'Kab. Belu', 'Kab. Bener Meriah', 'Kab. Bengkalis', 'Kab. Bengkayang', 'Kab. Bengkulu Selatan', 'Kab. Bengkulu Tengah', 'Kab. Bengkulu Utara', 'Kab. Berau', 'Kab. Biak Numfor', 'Kab. Bima', 'Kab. Bintan', 'Kab. Bireuen', 'Kab. Blitar', 'Kab. Blora', 'Kab. Boalemo', 'Kab. Bogor', 'Kab. Bojonegoro', 'Kab. Bolaang Mongondow', 'Kab. Bolaang Mongondow Selatan', 'Kab. Bolaang Mongondow Timur', 'Kab. Bolaang Mongondow Utara', 'Kab. Bombana', 'Kab. Bondowoso', 'Kab. Bone', 'Kab. Bone Bolango', 'Kab. Boven Digoel', 'Kab. Boyolali', 'Kab. Brebes', 'Kab. Buleleng', 'Kab. Bulukumba', 'Kab. Bulungan', 'Kab. Bulungan', 'Kab. Bungo', 'Kab. Buol', 'Kab. Buru', 'Kab. Buru Selatan', 'Kab. Buru Selatan', 'Kab. Buton', 'Kab. Buton Selatan', 'Kab. Buton Tengah', 'Kab. Buton Utara', 'Balikpapan', 'Banjar', 'Banjarbaru', 'Batam', 'Batu', 'Bau Bau', 'Bekasi', 'Bima', 'Binjai', 'Bitung', 'Blitar', 'Bogor', 'Bontang', 'Bukittinggi', 'Banda Aceh', 'Bandar Lampung', 'Banjarmasin', 'Bengkulu'], 
    'C': ['Kab. Ciamis', 'Kab. Cianjur', 'Kab. Cilacap', 'Kab. Cirebon', 'Cilegon', 'Cimahi', 'Cirebon'],
    'D': ['D.I. Aceh', 'D.I. Yogyakarta', 'Kab. Dairi', 'Kab. Deiyai', 'Kab. Deli Serdang', 'Kab. Demak', 'Kab. Dharmasraya', 'Kab. Dogiyai', 'Kab. Dompu', 'Kab. Donggala', 'Denpasar Utara', 'Depok', 'Dumai', 'Denpasar'], 
    'E': ['Kab. Empat Lawang', 'Kab. Ende', 'Kab. Enrekang'], 
    'F': ['Kab. Fak Fak', 'Kab. Flores Timur'],
    'G': ['Gorontalo', 'Kab. Garut', 'Kab. Gayo Lues', 'Kab. Gianyar', 'Kab. Gorontalo', 'Kab. Gorontalo Utara', 'Kab. Gowa', 'Kab. Gresik', 'Kab. Grobogan', 'Kab. Gunungkidul', 'Kab. Gunung Mas', 'Gunungsitoli', 'Gorontalo'], 
    'H': ['Kab. Halmahera Barat', 'Kab. Halmahera Selatan', 'Kab. Halmahera Tengah', 'Kab. Halmahera Timur', 'Kab. Halmahera Utara', 'Kab. Hulu Sungai Selatan', 'Kab. Hulu Sungai Tengah', 'Kab. Hulu Sungai Utara', 'Kab. Humbang Hasundutan'], 
    'I': ['Kab. Indragiri Hilir', 'Kab. Indragiri Hulu', 'Kab. Indramayu', 'Kab. Intan Jaya'], 
    'J': ['Jambi', 'Jawa Barat', 'Jawa Tengah', 'Jawa Timur', 'Kab. Jayapura', 'Kab. Jayawijaya', 'Kab. Jember', 'Kab. Jembrana', 'Kab. Jeneponto', 'Kab. Jepara', 'Kab. Jombang', 'Jakarta Barat', 'Jakarta Pusat', 'Jakarta Selatan', 'Jakarta Timur', 'Jakarta Utara', 'Jambi', 'Jayapura'], 
    'K': ['Kalimantan Barat', 'Kalimantan Selatan', 'Kalimantan Tengah', 'Kalimantan Timur', 'Kalimantan Utara', 'Kepulauan Bangka Belitung', 'Kepulauan Riau', 'Kab. Kaimana', 'Kab. Kampar', 'Kab. Kapuas', 'Kab. Kapuas Hulu', 'Kab. Karanganyar', 'Kab. Karangasem', 'Kab. Karawang', 'Kab. Karimun', 'Kab. Karo', 'Kab. Katingan', 'Kab. Kaur', 'Kab. Kayong Utara', 'Kab. Kebumen', 'Kab. Kediri', 'Kab. Keerom', 'Kab. Kendal', 'Kab. Kepahiang', 'Kab. Kep. Siau Tagulandang Biaro', 'Kab. Kepulauan Anambas', 'Kab. Kepulauan Aru', 'Kab. Kepulauan Mentawai', 'Kab. Kepulauan Mentawai', 'Kab. Kepulauan Meranti', 'Kab. Kepulauan Sangihe', 'Kab. Kepulauan Selayar', 'Kab. Kepulauan Sula', 'Kab. Kepulauan Talaud', 'Kab. Kepulauan Yapen', 'Kab. Kerinci', 'Kab. Ketapang', 'Kab. Klaten', 'Kab. Klungkung', 'Kab. Kolaka', 'Kab. Kolaka Timur', 'Kab. Kolaka Utara', 'Kab. Konawe', 'Kab. Konawe Kepulauan', 'Kab. Konawe Kepulauan', 'Kab. Konawe Selatan', 'Kab. Konawe Utara', 'Kab. Kuantan Singingi', 'Kab. Kubu Raya', 'Kab. Kudus', 'Kab. Kulon Progo', 'Kab. Kuningan', 'Kab. Kupang', 'Kab. Kutai Barat', 'Kab. Kutai Kartanegara', 'Kab. Kutai Timur', 'Kepulauan Seribu', 'Kediri', 'Kendari', 'Kupang'], 
    'L': ['Lampung', 'Kab. Labuhanbatu', 'Kab. Labuhanbatu Selatan', 'Kab. Labuhanbatu Utara', 'Kab. Lahat', 'Kab. Lamandau', 'Kab. Lamongan', 'Kab. Lampung Barat', 'Kab. Lampung Selatan', 'Kab. Lampung Tengah', 'Kab. Lampung Timur', 'Kab. Lampung Utara', 'Kab. Landak', 'Kab. Langkat', 'Kab. Lanny Jaya', 'Kab. Lebak', 'Kab. Lebong', 'Kab. Lembata', 'Kab. Lima Puluh Kota', 'Kab. Lingga', 'Kab. Lombok Barat', 'Kab. Lombok Tengah', 'Kab. Lombok Timur', 'Kab. Lombok Utara', 'Kab. Lumajang', 'Kab. Luwu', 'Kab. Luwu Timur', 'Kab. Luwu Utara', 'Langsa', 'Lhokseumawe', 'Lubuk Linggau'], 
    'M': ['Maluku', 'Maluku Utara', 'Medan', 'Kab. Madiun', 'Kab. Magelang', 'Kab. Magetan', 'Kab. Mahakam Ulu', 'Kab. Majalengka', 'Kab. Majene', 'Kab. Malaka', 'Kab. Malang', 'Kab. Malinau', 'Kab. Malinau', 'Kab. Maluku Barat Daya', 'Kab. Maluku Barat Daya', 'Kab. Maluku Tengah', 'Kab. Maluku Tenggara', 'Kab Maluku Tenggara Barat', 'Kab Maluku Tenggara Barat', 'Kab. Mamasa', 'Kab. Mamberamo Raya', 'Kab. Mamberamo Tengah', 'Kab. Mamuju', 'Kab. Mamuju Tengah', 'Kab. Mamuju Utara', 'Kab. Mandailing Natal', 'Kab. Manggarai', 'Kab. Manggarai Barat', 'Kab. Manggarai Timur', 'Kab. Manokwari', 'Kab. Manokwari Selatan', 'Kab. Mappi', 'Kab. Maros', 'Kab. Maybrat', 'Kab. Melawi', 'Kab. Mempawah', 'Kab. Merangin', 'Kab. Merauke', 'Kab. Mesuji', 'Kab. Mimika', 'Kab. Minahasa', 'Kab. Minahasa Selatan', 'Kab. Minahasa Tenggara', 'Kab. Minahasa Utara', 'Kab. Mojokerto', 'Kab. Morowali', 'Kab. Morowali Utara', 'Kab. Muara Enim', 'Kab. Muaro Jambi', 'Kab. Muko Muko', 'Kab. Muna', 'Kab. Muna Barat', 'Kab. Murung Raya', 'Kab. Musi Banyuasin', 'Kab. Musi Rawas', 'Kab. Musi Rawas Utara', 'Madiun', 'Magelang', 'Malang', 'Metro', 'Mojokerto', 'Makassar', 'Manado', 'Mataram'], 
    'N': ['Nusa Tenggara Barat', 'Nusa Tenggara Timur', 'Kab. Nabire', 'Kab. Nagan Raya', 'Kab. Nagekeo', 'Kab. Natuna', 'Kab. Nduga', 'Kab. Ngada', 'Kab. Nganjuk', 'Kab. Ngawi', 'Kab. Nias', 'Kab. Nias Barat', 'Kab. Nias Selatan', 'Kab. Nias Utara', 'Kab. Nunukan', 'Kab. Nunukan'], 
    'O': ['Kab. Ogan Ilir', 'Kab. Ogan Komering Ilir', 'Kab. Ogan Komering Ulu', 'Kab. Ogan Komering Ulu Selatan', 'Kab. Ogan Komering Ulu Timur', 'Kotamobagu'], 
    'P': ['Papua', 'Papua Barat', 'Kab. Pacitan', 'Kab. Padang Lawas', 'Kab. Padang Lawas Utara', 'Kab. Padang Pariaman', 'Kab. Padang Pariaman', 'Kab. Pahuwato', 'Kab. Pakpak Bharat', 'Kab. Pamekasan', 'Kab. Pandeglang', 'Kab. Pangandaran', 'Kab. Pangkajene Kepulauan', 'Kab. Paniai', 'Kab. Parigi Moutong', 'Kab. Pasaman', 'Kab. Pasaman Barat', 'Kab. Paser', 'Kab. Pati', 'Kab. Pegunungan Arfak', 'Kab Pegunungan Bintang', 'Kab. Pekalongan', 'Kab. Pelalawan', 'Kab. Pemalang', 'Kab. Penajam Paser Utara', 'Kab. Penukal Abab Lematang Ilir', 'Kab. Pesawaran', 'Kab. Pesisir Barat', 'Kab. Pesisir Selatan', 'Kab. Pesisir Selatan', 'Kab. Pidie', 'Kab. Pidie Jaya', 'Kab. Pinrang', 'Kab. Polewali Mandar', 'Kab. Ponorogo', 'Kab. Pontianak', 'Kab. Poso', 'Kab. Pringsewu', 'Kab. Probolinggo', 'Kab. Pulang Pisau', 'Kab. Pulau Morotai', 'Kab. Pulau Taliabu', 'Kab. Puncak', 'Kab. Puncak Jaya', 'Kab. Purbalingga', 'Kab. Purwakarta', 'Kab. Purworejo', 'Padang Panjang', 'Padangsidimpuan', 'Pagar Alam', 'Palopo', 'Pare Pare', 'Pariaman', 'Pariaman', 'Pasuruan', 'Payakumbuh', 'Pekalongan', 'Pematang Siantar', 'Prabumulih', 'Probolinggo', 'Padang', 'Palangkaraya', 'Palembang', 'Palu', 'Pangkal Pinang', 'Pekanbaru', 'Pontianak'], 
    'R': ['Riau', 'Kab. Raja Ampat', 'Kab. Rejang Lebong', 'Kab. Rembang', 'Kab. Rokan Hilir', 'Kab. Rokan Hulu', 'Kab. Rote Ndao'], 
    'S': ['Sulawesi Barat', 'Sulawesi Selatan', 'Sulawesi Tengah', 'Sulawesi Tenggara', 'Sulawesi Utara', 'Sumatera Barat', 'Sumatera Selatan', 'Sumatera Utara', 'Kab. Sabu Raijua', 'Kab. Sambas', 'Kab. Samosir', 'Kab. Sampang', 'Kab. Sanggau', 'Kab. Sarmi', 'Kab. Sarolangun', 'Kab. Sekadau', 'Kab. Selayar', 'Kab. Seluma', 'Kab. Semarang', 'Kab. Seram Bagian Barat', 'Kab. Seram Bagian Timur', 'Kab. Serang', 'Kab. Serdang Bedagai', 'Kab. Seruyan', 'Kab. Siak', 'Kab. Sidenreng Rappang', 'Kab. Sigi', 'Kab. Sijunjung', 'Kab. Sikka', 'Kab. Simalungun', 'Kab. Simeulue', 'Kab. Sinjai', 'Kab. Sintang', 'Kab. Situbondo', 'Kab. Sleman', 'Kab. Solok', 'Kab. Solok Selatan', 'Kab. Soppeng', 'Kab. Sorong', 'Kab. Sorong Selatan', 'Kab. Sragen', 'Kab. Subang', 'Kab. Sukabumi', 'Kab. Sukamara', 'Kab. Sukoharjo', 'Kab. Sumba Barat', 'Kab. Sumba Barat Daya', 'Kab. Sumba Tengah', 'Kab. Sumba Timur', 'Kab. Sumbawa', 'Kab. Sumbawa Barat', 'Kab. Sumedang', 'Kab. Sumenep', 'Kab. Supiori', 'Sabang', 'Salatiga', 'Sawahlunto', 'Sibolga', 'Singkawang', 'Solok', 'Sorong', 'Subulussalam', 'Sukabumi', 'Sungai Penuh', 'Surakarta', 'Sungai Penuh', 'Samarinda', 'Semarang', 'Serang'], 
    'T': ['Kab. Tabalong', 'Kab. Tabanan', 'Kab. Takalar', 'Kab. Tambrauw', 'Kab. Tanah Bumbu', 'Kab. Tanah Datar', 'Kab. Tanah Laut', 'Kab. Tana Tidung', 'Kab. Tana Tidung', 'Kab. Tana Toraja', 'Kab. Tangerang', 'Kab. Tanggamus', 'Kab. Tanjung Jabung Barat', 'Kab. Tanjung Jabung Timur', 'Kab. Tapanuli Selatan', 'Kab. Tapanuli Tengah', 'Kab. Tapanuli Utara', 'Kab. Tapin', 'Kab. Tasikmalaya', 'Kab. Tebo', 'Kab. Tegal', 'Kab. Teluk Bintuni', 'Kab. Teluk Wondama', 'Kab. Temanggung', 'Kab. Timor Tengah Selatan', 'Kab. Timor Tengah Utara', 'Kab. Toba Samosir', 'Kab. Tojo Una Una', 'Kab. Tolikara', 'Kab. Toli Toli', 'Kab. Toraja Utara', 'Kab. Trenggalek', 'Kab. Tuban', 'Kab. Tulang Bawang', 'Kab. Tulang Bawang Barat', 'Kab. Tulungagung', 'Tangerang', 'Tangerang Selatan', 'Tanjung Balai', 'Tarakan', 'Tarakan', 'Tasikmalaya', 'Tebing Tinggi', 'Tegal', 'Ternate', 'Tidore', 'Tidore Kepulauan', 'Tomohon', 'Tual', 'Tual', 'Tanjung Pinang'], 
    'W': ['Kab. Wajo', 'Kab. Wakatobi', 'Kab. Waropen', 'Kab. Way Kanan', 'Kab. Wonogiri', 'Kab. Wonosobo'], 
    'Y': ['Kab. Yahukimo', 'Kab. Yalimo', 'Yogyakarta']
    }






#this is the scrapping script i use, kota.html is just some part of the tokopedia html page,
#the part is taken from tokopedia search filter in "lokasi section"

# this function should not be used in production.
# This function is provided for demonstration purposes only.
def generate_city_dictionary():
    city_dict = {} 

    curr_dir = os.getcwd()
    file_path = os.path.join(curr_dir,'kota.html')
    html = ""
    with open(file_path, 'r') as file:
        html = file.read()

    soup = BeautifulSoup(html, features="html.parser")
    all_parent_div = soup.find_all('div', {'class': 'css-aibqdm'})
    for parent_div in all_parent_div:
        city_first_letter = parent_div.find('b').get_text(strip=True)
        city_dict[city_first_letter] = []
        all_city_name = parent_div.find_all('span', {'class':"css-iaqlny"})
        for city_name in all_city_name:
            city_dict[city_first_letter].append(city_name.get_text(strip=True))
    return city_dict
    