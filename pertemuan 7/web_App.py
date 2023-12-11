from flask import Flask, render_template, request, jsonify

app_flask = Flask(__name__)

class ChickenOrder:
    def __init__(self):
        self.jenis_potong_mapping = {"D": "Dada", "P": "Paha", "S": "Sayap"}
        self.harga_mapping = {"D": 2500, "P": 2000, "S": 1500}

        self.banyak_jenis = 0
        self.jenis_potong = []
        self.harga = []
        self.jumlah = []

    def add_order(self, jenis, banyak):
        self.banyak_jenis += 1

        if jenis in self.jenis_potong_mapping:
            self.jenis_potong.append(self.jenis_potong_mapping[jenis])
            self.harga.append(self.harga_mapping[jenis])
            self.jumlah.append(banyak * self.harga_mapping[jenis])
        else:
            self.jenis_potong.append("kode salah")
            self.harga.append(0)
            self.jumlah.append(banyak * 0)

    def get_order_data(self, index):
        return {
            "jenis_potong": self.jenis_potong[index],
            "harga": self.harga[index],
            "jumlah": self.jumlah[index]
        }

chicken_order = ChickenOrder()

@app_flask.route('/')
def index():
    return render_template('index.html')

@app_flask.route('/place_order', methods=['POST'])
def place_order():
    order_data = request.json
    jenis_potong = order_data['jenis_potong']
    banyak_potong = order_data['banyak_potong']

    chicken_order.add_order(jenis_potong, banyak_potong)

    billing_message = get_billing_message(chicken_order.banyak_jenis - 1)

    return jsonify({"billing_message": billing_message})

def get_billing_message(index):
    order_data = chicken_order.get_order_data(index)
    total_harga = order_data["harga"] * order_data["jumlah"]

    bonus = ""
    if total_harga > 100000:
        bonus = "Selamat! Anda mendapatkan Shampo sebagai bonus."

    billing_message = f"Detail Pesanan:\nJenis Potong: {order_data['jenis_potong']}\nHarga: {order_data['harga']}\nJumlah: {order_data['jumlah']}\n{bonus}"

    return billing_message

if __name__ == '__main__':
    app_flask.run(debug=True)