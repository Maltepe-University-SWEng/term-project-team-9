
# 🧠 Large Language Model ve Fıkra Üretimi – *FıkraBot*

Bu proje, Maltepe Üniversitesi Yazılım Mühendisliği öğrencileri tarafından **Software Project Management** dersi kapsamında geliştirilmiştir.  
Amacımız, doğal dil işleme (NLP) alanındaki bilgi birikimimizi kullanarak **Türk kültürüne özgü mizahi metinler (fıkra)** üretebilen bir yapay zeka uygulaması geliştirmekti.

Projenin merkezinde iki farklı yaklaşım yer almaktadır:

- 🧪 **Sıfırdan Eğitilen Küçük Ölçekli LLM (Transformer tabanlı)**  
- 🔧 **Türkçe GPT-2 modelinin Nasreddin Hoca fıkra veri setiyle fine-tune edilmesi**

Her iki model de fıkra üretme amacıyla test edilmiştir. Bu sayede hem kendi eğittiğimiz küçük bir modelin sınırlarını gözlemleme hem de hazır büyük bir dil modelini adapte ederek performans farklarını analiz etme fırsatımız oldu.

---

## 🚀 Uygulama Özeti

Proje iki farklı kullanıcı arayüzü içerir:

### 1. **Custom Model – Web Arayüzü (Node.js & EJS)**
- Python'da geliştirilen özel bir Transformer modeline bağlanan modern ve sohbet benzeri bir kullanıcı arayüzü sunar.
- Kullanıcılar giriş yaptıktan sonra prompt yazarak fıkra üretebilir.

### 2. **Fine-tuned Model – Streamlit Arayüzü**
- Nasreddin Hoca fıkralarıyla eğitilmiş GPT-2 modeli ile Streamlit üzerinde gerçek zamanlı fıkra üretimi yapılır.
- “Fıkra Üret” butonuna basıldığında model mizahi ve kültürel olarak yerel bir metin üretir.

---

## 🏗️ Mimari

### 🔬 Backend (Python + PyTorch)

- **Custom Transformer Decoder Modeli**
  - Embedding katmanı (vocab: 10.000)
  - Positional Encoding
  - 2 Katmanlı Transformer Decoder (4 attention head)
  - Linear çıkış katmanı
  - Tokenizer: SentencePiece (özel eğitildi)
  - Eğitim & inference PyTorch ile yapılmıştır.

- **Fine-tuned Model**
  - Hugging Face üzerinden ytu-ce-cosmos/turkish-gpt2 modeli
  - Nasreddin Hoca fıkralarıyla fine-tune edilmiştir.
  - inference Streamlit üzerinden yapılır.

### 🌐 Frontend (Kullanıcı Arayüzü)

#### 1. **Custom Model UI**
- Node.js + Express.js ile geliştirildi
- EJS template motoru ile sayfalar oluşturuldu
- Kullanıcı giriş sistemi (JWT, bcryptjs)
- MongoDB ile kullanıcı yönetimi

#### 2. **Fine-tuned Model UI**
- Streamlit ile hızlı prototipleme
- Tek butonla mizahi içerik üretimi

---

## 📦 Kullanılan Teknolojiler

| Backend              | Frontend                | Model Eğitim Ortamı    |
|----------------------|--------------------------|--------------------------|
| Python 3.10+         | Node.js (v18+)           | Kaggle / Google Colab   |
| PyTorch              | Express.js               | PyTorch + Transformers  |
| Flask (API server)   | EJS (Template engine)    | SentencePiece tokenizer |
| Hugging Face         | MongoDB (veritabanı)     | model_v11.pth (custom)  |
| Streamlit            | bcryptjs, axios, JWT     | turkish-gpt2 (fine-tuned)|

---

## ⚙️ Kurulum Talimatları

### Ortam Kurulumu

#### 1. Reposityory’yi klonlayın:
```bash
git clone <repo-url>
cd PythonProject
```

#### 2. Python ortamı kurun:
```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
```

#### 3. Frontend ortamı:
```bash
cd frontend
npm install
```

---

## ▶️ Uygulamayı Başlatma

### Backend:
```bash
./run_api.sh
```

### Frontend:
```bash
./run_frontend.sh
```

veya birleşik şekilde:

```bash
node run.js
```

- Frontend: [http://localhost:3001](http://localhost:3001)  
- Backend API: [http://localhost:5001](http://localhost:5001)

---

## 📁 Proje Yapısı

```
FikraBot/
├── api/                      # Flask API backend
├── frontend/                 # Node.js tabanlı arayüz
│   ├── views/               # EJS dosyaları
│   └── app.js               # Express başlangıç dosyası
├── model.ipynb               # Custom model eğitimi
├── app.py                    # Streamlit arayüzü (fine-tuned model)
├── model_v11.pth             # Eğitilmiş model dosyası
├── run.js                    # Her iki servisi başlatan dosya
└── requirements.txt          # Python bağımlılıkları
```

---

## 📚 Model Eğitimi

- **Custom Model**: SentencePiece tokenizer ile tokenlaştırılan genel Türkçe fıkralar ile sıfırdan eğitildi.
- **Fine-tuned Model**: Hugging Face üzerinden alınan GPT-2 modeli, Nasreddin Hoca fıkralarıyla fine-tune edildi.
- Eğitim süreçleri sırasında loss takibi, validation split ve erken durdurma gibi yöntemler kullanıldı.

---

## 👨‍💻 Katkıda Bulunanlar

- Esma Şen (Scrum Master)
- Alp Salcıoğlu
- Melahat Eda Acar
- Berke Ensel
- İbrahim Kartal
- Eren Yıldırım

---

## 📄 Lisans

Bu projede kullanılan içerikler yalnızca eğitim amaçlıdır. Gerekli durumlarda açık kaynak lisansı eklenecektir.
