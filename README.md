````markdown
# 🕒 Watch Sell — Online Soat Do‘koni

**Watch Sell** — bu Django asosida ishlab chiqilgan soat savdosi uchun mo‘ljallangan onlayn do‘kon loyihasi.  
Loyihada foydalanuvchini ro‘yxatdan o‘tkazish, email orqali tasdiqlash, mahsulotlarni ko‘rish va admin panelga yuborish funksiyalari mavjud.

---

## 🌐 Live Demo

🖥 Ishlayotgan sayt:  
🔗 https://watchsellservice.pythonanywhere.com/

---

## 🛠 Texnologiyalar

- **Python 3**
- **Django 4**
- **HTML, CSS, Bootstrap**
- **JavaScript (asosiy)**
- **Django Email Backend (SMTP)**
- **SQLite (default)**
- **PythonAnywhere** (Deploy uchun)
- **Multi-language (uz/ru/en)**

---

## 🧠 Shaxsiy tajriba

> Bu loyiha davomida eng ko‘p e'tiborimni foydalanuvchi bilan ishlash jarayonlariga qaratdim.  
> Xususan:
> 
> ✅ **Ro‘yxatdan o‘tish va login sahifalarini** sozlash  
> ✅ **Parolni unutgan holatda tiklash tizimini** yaratish  
> ✅ **Emailga tasdiqlash kodi yuborish va real gmailni tekshirish**
> 
> Bu orqali men quyidagilarni chuqur o‘rgandim:
> - Django'da email yuborish
> - Foydalanuvchi ma’lumotlarini forma orqali qabul qilish va tekshirish
> - Multi-language frontend (Xush kelibsiz xabari 3 tilda)
> - Real email bo‘lmagan holatda ro‘yxatdan o‘tishni bloklash

---

## 🌍 Tilni tanlash funksiyasi

Saytga kirganingizda foydalanuvchiga avtomatik ravishda 3 tilda (O‘zbek, Rus, Ingliz) **"Xush kelibsiz"** xabari chiqariladi:

- 🇺🇿 Uzbek: *Xush kelibsiz!*  
- 🇷🇺 Русский: *Добро пожаловать!*  
- 🇬🇧 English: *Welcome!*

> Bu foydalanuvchilarning tilini aniqlab, mos interfeysni ko‘rsatadi. Django i18n funksiyasi asosida.

---

## 📧 Real Gmail tekshiruvi

- Ro‘yxatdan o‘tish vaqtida foydalanuvchi **gmail manzilini kiritishi shart**
- Django email backend orqali **real Gmail manziliga** tasdiqlovchi 6 xonali kod yuboriladi
- Gmail mavjud bo‘lmasa yoki noto‘g‘ri kiritilsa — ro‘yxatdan o‘tish ruxsat etilmaydi

---

## 📁 Loyihadagi asosiy kataloglar

| Katalog        | Tavsifi |
|----------------|---------|
| `watch_sell/`  | Django asosiy konfiguratsiya fayllari (`settings.py`, `urls.py`, `wsgi.py`) |
| `home_app/`    | Bosh sahifa uchun logika va sahifalar |
| `account/`     | Ro‘yxatdan o‘tish, login, logout, email verification, parolni tiklash |
| `product_app/` | Mahsulotlar bilan ishlash (ko‘rish, qo‘shish) |
| `contact_app/` | Foydalanuvchi fikrlari, bog‘lanish shakli |
| `templates/`   | HTML fayllar |
| `static/`      | CSS, JS, rasm va boshqa statik fayllar |

---

## 🚀 Ishga tushirish

```bash
git clone https://github.com/Abdurahmon17/watch_sell.git
cd watch_sell
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
````

🔗 Saytga kiring: `http://127.0.0.1:8000/`

---

## ✉️ Parolni unutgan foydalanuvchi

1. "Forgot password" tugmasini bosadi
2. Emailga 6 xonali tasdiqlash kodi yuboriladi
3. Foydalanuvchi shu kodni kiritadi
4. Agar kod to‘g‘ri bo‘lsa — yangi parol kiritish sahifasiga o‘tadi
5. Kod noto‘g‘ri bo‘lsa — xato xabari chiqadi

---

## 📌 Kelajakdagi imkoniyatlar

* Mahsulotlarni filtrlash va qidirish
* REST API orqali mobil versiya
* Savatcha (shopping cart) funksiyasi
* To‘lov tizimi integratsiyasi (Click/Payme)

---

## 🤝 Xissa qo‘shish

1. Fork qiling
2. O‘zgartirishlar kiriting
3. Pull Request yuboring

---

## 👨‍💻 Muallif

**Abdurahmon Abdumavlonov**
📧 Email: [abdumavlonovabdurahmon75@gmail.com](mailto:abdumavlonovabdurahmon75@gmail.com)
🔗 GitHub: [Abdurahmon17](https://github.com/Abdurahmon17)

---

## 📄 Litsenziya

Ushbu loyiha hozircha litsenziyasiz. Agar kerak bo‘lsa MIT litsenziya qo‘shilishi mumkin.

---

✅ Bu loyiha orqali foydalanuvchi autentifikatsiyasi, email-verifikatsiya, parol tiklash, va ko‘p tilli interfeysni chuqur o‘rgandim.

```

---

✅ Endi bu `README.md` faylni:
- GitHub loyihangga yukla
- Yoki xohlasang `.md` fayl holida yuklab beray

---

Keyingisi: `kindergarden_org` loyihangga ham `README.md` yozamizmi? Yoki bu faylni yuklab olaymi?
```
