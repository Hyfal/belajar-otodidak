from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/inventaris_db'
db = SQLAlchemy(app)

class Barang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    jumlah = db.Column(db.Integer, nullable=False)

@app.route('/barang', methods=['POST'])
def tambah_barang():
    data = request.get_json()
    barang_baru = Barang(nama=data['nama'], jumlah=data['jumlah'])
    db.session.add(barang_baru)
    db.session.commit()
    return jsonify({'message': 'Barang berhasil ditambahkan'}), 201

if __name__ == '__main__':
    app.run(debug=True)
