# 🌙 Quran Ghost Pro - Video Processor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Process-green?style=for-the-badge&logo=ffmpeg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

أداة احترافية مخصصة لدمج خلفيات الفيديو مع نصوص القرآن الكريم (Chroma/Green Screen) بأسلوب الـ **Ghost Effect**، مما يعطي جمالية وهدوء للفيديوهات الدعوية.

## 🚀 المميزات
- **تأثير الـ Ghost:** تقليل شفافية الخلفية وإضافة طبقة سوداء خفيفة لإبراز النص القرآني.
- **المعالجة الذكية:** يقوم البرنامج بمطابقة الفيديوهات وتغيير حجمها (Scale) تلقائياً لتناسب مقاسات الـ Vertical (1080x1920).
- **إزالة الخلفية السوداء:** استخدام فلاتر `colorkey` لإزالة الخلفيات من فيديوهات الكروما.
- **تلقائية بالكامل:** معالجة دفعية (Batch Processing) لجميع الفيديوهات في المجلدات دفعة واحدة.
- **واجهة تفاعلية:** لوحة تحكم بسيطة مع Banner احترافي ومؤشر تحميل (Loading Spinner).

---

## 🛠️ المتطلبات
يجب التأكد من تثبيت الأدوات التالية على جهازك:
1. **Python 3.x**
2. **FFmpeg** (مهم جداً لمعالجة الفيديو)

### تثبيت FFmpeg:
- **Windows:** يمكنك تحميله من [ffmpeg.org](https://ffmpeg.org/download.html).
- **Linux:** `sudo apt install ffmpeg`
- **Mac:** `brew install ffmpeg`

---

## 📁 هيكل المجلدات
بمجرد تشغيل الكود لأول مرة، سيقوم البرنامج بإنشاء المجلدات التالية تلقائياً:

- `quran_backgrounds/`: ضع هنا فيديوهات الخلفية (المناظر الطبيعية، مساجد، إلخ).
- `quran_chroma/`: ضع هنا فيديوهات نصوص القرآن (بخلفية سوداء أو خضراء).
- `quran_output/`: هنا ستجد الفيديوهات النهائية الجاهزة للنشر.

---

## 💻 طريقة الاستخدام

1. قم بتحميل المستودع (Clone) أو نسخ الكود في ملف باسم `quranV1.py`.
2. ضع ملفات الفيديو الخاصة بك في المجلدات المخصصة (`backgrounds` و `chroma`).
3. افتح التيرمينال (Terminal) وشغل الأداة:
   ```bash
   python quranV1.py
   
