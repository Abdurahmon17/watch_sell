````markdown
# 🕒 Watch Sell — Online Soat Do‘koni

**Watch Sell** — bu Django asosida ishlab chiqilgan soat savdosi uchun mo‘ljallangan onlayn do‘kon loyihasi.  
Loyihada foydalanuvchini ro‘yxatdan o‘tkazish, email orqali tasdiqlash, mahsulotlarni ko‘rish va admin panelga yuborish funksiyalari mavjud.

---

## 🌐 Demo (Agar mavjud bo‘lsa demo linkini qo‘shing)

---

## 🛠 Texnologiyalar

- **Python 3**
- **Django 4**
- **HTML, CSS, Bootstrap**
- **JavaScript (asosiy)**
- **Django Email Backend (SMTP)**
- **SQLite (default)**

---

## 🧠 Shaxsiy tajriba

> Bu loyiha davomida eng ko‘p e'tiborimni foydalanuvchi bilan ishlash jarayonlariga qaratdim.  
> Xususan:
> 
> ✅ **Ro‘yxatdan o‘tish va login sahifalarini** sozlash  
> ✅ **Parolni unutgan holatda tiklash tizimini** yaratish:  
> - Emailga 6 xonali tasdiqlash kodi yuboriladi  
> - Foydalanuvchi shu kodni kiritadi  
> - Kod mos kelsa, yangi parol kiritish sahifasiga o‘tadi  
> - Aks holda xato xabari qaytariladi  
> 
> Bu orqali **Django'da email yuborish** va **formani to‘ldirib admin panelga saqlash** jarayonlarini chuqur o‘rgandim.

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

### 1. Repozitoriyani klon qiling

```bash
git clone https://github.com/Abdurahmon17/watch_sell.git
cd watch_sell
````

### 2. Virtual muhit yaratish va faollashtirish

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Kerakli kutubxonalarni o‘rnatish

```bash
pip install -r requirements.txt
```

### 4. Migratsiyalarni bajaring

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Superuser yarating

```bash
python manage.py createsuperuser
```

### 6. Serverni ishga tushiring

```bash
python manage.py runserver
```

🔗 Saytga kiring: `http://127.0.0.1:8000/`

---

## ✉️ Email orqali parol tiklash

Foydalanuvchi parolni unutgan bo‘lsa:

1. "Forgot password" tugmasini bosadi
2. Emailga 6 xonali tasdiqlash kodi yuboriladi
3. Foydalanuvchi shu kodni kiritadi
4. Agar kod to‘g‘ri bo‘lsa — yangi parol kiritish sahifasiga o‘tadi
5. Admin panelga ham form ma’lumotlari saqlanadi

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

✅ Bu loyiha orqali foydalanuvchi autentifikatsiyasi va email-verifikatsiya bilan ishlashni chuqur o‘rgandim.

```

---

Agar xohlasang:
- Bu faylni `.md` formatida yuklab beraman
- Keyingi loyiha `kindergarden_org` uchun ham `README` yozib beraman

📌 Endi nima qilamiz? Faylni yuklab beraymi yoki boshqa loyiha uchun yozamizmi?
```
