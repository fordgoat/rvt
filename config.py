import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID", "29486311"))
api_hash = os.getenv("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
bot_token = os.getenv("BOT_TOKEN", "6943283709:AAGK3LU4n_8gk40KnvRBKHfBgKMpJ1foP8w")
# =========================================================== #

db_url = os.getenv("DB_URL", "mongodb+srv://kikoy:kikoy6969@cluster0.vooxu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db_name = os.getenv("DB_NAME", "test") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.getenv("CHANNEL_1", "-1001197188587"))
channel_2 = int(os.getenv("CHANNEL_2", "-1001689707975")) #untuk group comentar user
channel_log = int(os.getenv("CHANNEL_LOG", "-1002109996381"))
# =========================================================== #

id_admin = int(os.getenv("ID_ADMIN", "1707380693"))
# =========================================================== #

batas_kirim = int(os.getenv("BATAS_KIRIM", "5"))
# =========================================================== #

biaya_kirim = int(os.getenv("BIAYA_KIRIM", "20"))
# =========================================================== #

hastag = os.getenv("HASTAG", "#s #a #FwbBoy #FwbGirl #FwbAsk #FwbStory").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.getenv("PIC_BOY", "https://telegra.ph/file/c67bd36023648dc777bd9.jpg")
pic_girl = os.getenv("PIC_GIRL", "https://telegra.ph/file/cb885bcbf5081dbd45f27.jpg")
# =========================================================== #

pesan_join = os.getenv("PESAN_JOIN", "Tidak Dapat Diakses Harap Join Terlebih Dahulu")
start_msg = os.getenv("START_MSG", "Hai {mention} 🌱\n\n<b>SM Menfess Bot</b> adalah Bot Auto Post, Semua Pesan Yang Kamu Kirim Akan Masuk Ke Channel @smmenfess Secara Anonymous. Untuk Bantuan Ketik /help")

gagalkirim_msg = os.getenv("GAGAL_KIRIM", """
{mention}, Pesan Mu Gagal Terkirim Silahkan Gunakan Hashtag Berikut:

#Boy / #Girl (Untuk Mencari Pasangan, Teman , Partner FWB)
#Ask (Untuk Bertanya)
#Story (Untuk Berbagi Cerita)
#Spill (Untuk Spill Masalah)
#Find (Untuk Mencari Pasangan, Teman, Partner FWB)
""")
