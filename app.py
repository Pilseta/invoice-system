from flask import Flask, render_template, jsonify, request
import os
import json

app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Rēķinu Sistēma</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background: #f8f9fa; padding: 20px; }
            .hero { 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 60px 20px;
                border-radius: 20px;
                margin-bottom: 40px;
            }
            .feature-card {
                border: none;
                border-radius: 15px;
                padding: 30px;
                margin: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                transition: transform 0.3s;
            }
            .feature-card:hover {
                transform: translateY(-5px);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="hero text-center">
                <h1 class="display-4">🏢 RĒĶINU SISTĒMA</h1>
                <p class="lead">Profesionāla rēķinu, avansa rēķinu un pavadzīmju veidošanas platforma</p>
                <a href="/create" class="btn btn-light btn-lg">SĀKT DARBU</a>
            </div>
            
            <div class="row">
                <div class="col-md-4">
                    <div class="feature-card text-center">
                        <h2>📝</h2>
                        <h4>Jauns Rēķins</h4>
                        <p>Izveidojiet rēķinus, avansa rēķinus un pavadzīmes</p>
                        <a href="/create" class="btn btn-primary">Izveidot</a>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card text-center">
                        <h2>👥</h2>
                        <h4>Klienti</h4>
                        <p>Pārvaldiet klientu datubāzi un vēsturi</p>
                        <a href="/clients" class="btn btn-success">Pārvaldīt</a>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card text-center">
                        <h2>📊</h2>
                        <h4>Statistika</h4>
                        <p>Skatiet atskaites un analīzi</p>
                        <a href="/stats" class="btn btn-info">Apskatīt</a>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/create')
def create():
    return '''
    <div class="container mt-4">
        <h1>🧾 Jauns Rēķins</h1>
        <div class="card p-4">
            <p>Rēķinu veidošanas forma drīzumā būs pieejama...</p>
            <a href="/" class="btn btn-secondary">← Atpakaļ</a>
        </div>
    </div>
    '''

@app.route('/clients')
def clients():
    return '''
    <div class="container mt-4">
        <h1>👥 Klienti</h1>
        <div class="card p-4">
            <p>Klientu pārvaldība drīzumā būs pieejama...</p>
            <a href="/" class="btn btn-secondary">← Atpakaļ</a>
        </div>
    </div>
    '''

@app.route('/stats')
def stats():
    return '''
    <div class="container mt-4">
        <h1>📊 Statistika</h1>
        <div class="card p-4">
            <p>Statistika drīzumā būs pieejama...</p>
            <a href="/" class="btn btn-secondary">← Atpakaļ</a>
        </div>
    </div>
    '''

if __name__ == '__main__':
    print("=" * 50)
    print("RĒĶINU SISTĒMA")
    print("Atveriet: http://localhost:5000")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5000, debug=True)
