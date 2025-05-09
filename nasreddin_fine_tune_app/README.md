# 🧠 Nasreddin Hoca Fıkra Üretici

Bu proje, fine-tune edilmiş bir GPT-2 modeli ile Türkçe Nasreddin Hoca fıkraları üretmektedir.  
Kullanıcı dostu bir Streamlit arayüzü ile her tıklamada farklı fıkra üretir.

---

## 📌 Kullanılan Teknolojiler

- Python
- PyTorch
- Hugging Face Transformers
- Streamlit

---

## ⚙️ Kurulum Adımları

### 1. Gerekli kütüphaneleri yükleyin:

- pip install -r requirements.txt

### 2. Model dosyasını indirin ve doğru klasöre yerleştirin

- 📁 [Modeli indir (.bin)](https://drive.google.com/uc?id=1fFkaM2hy4RnbrSehGjXXfqmE-nqwK9-F&export=download)


# Klasör yapısı şu şekilde olmalıdır:
nasreddin_fine_tune_app/
├── app.py
├── requirements.txt
├── model/
├── nasreddin_model/
│   └── pytorch_model.bin
...

### 3. Uygulamayı terminalde komutu çalıştırarak app.py dosyasında başlatın

- streamlit run app.py
