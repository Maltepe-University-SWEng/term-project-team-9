[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/oZBp5p5Q)

# 🧠 Large Language Model ve Fıkra Üretimi 

Bu proje, Maltepe Üniversitesi Yazılım Mühendisliği öğrencileri tarafından Software Project Management dersi kapsamında geliştirilmiştir.  
Amacımız, doğal dil işleme (NLP) alanındaki bilgi birikimimizi kullanarak Türk kültürüne özgü mizahi metinler (fıkra) üretebilen bir yapay zeka uygulaması geliştirmekti.

Projenin merkezinde, iki farklı yaklaşım yer almaktadır:

- 🧪 **Sıfırdan Eğitilen Küçük Ölçekli LLM (Transformer tabanlı)**  
- 🔧 **Mevcut GPT-2 modelinin Türkçe fıkra veri setiyle fine-tune edilmesi**

Her iki model de fıkra üretme amacıyla test edilmiştir. Bu sayede hem kendi eğittiğimiz küçük bir modelin sınırlarını gözlemleme hem de hazır büyük bir dil modelini adapte ederek performans farklarını analiz etme fırsatımız oldu.

---

## 🚀 Uygulama Özeti

Proje, kullanıcı dostu bir **Streamlit** arayüzü üzerinden çalışır. Kullanıcı "Fıkra Üret" butonuna bastığında, arka plandaki modelle oluşturulmuş anlamlı ve mizahi bir fıkra sunulur.  
Model Türkçe dilinde eğitildiği için metinler tutarlı ve kültürel olarak yerel değerlere uygundur.

---

## 🔧 Kullanılan Teknolojiler

- Python 3.10+
- PyTorch
- Hugging Face Transformers
- Streamlit
- Google Colab (model eğitimi için)
- Kaggle (model eğitimi için)
- GitHub (sürüm kontrolü ve iş birliği)

---



