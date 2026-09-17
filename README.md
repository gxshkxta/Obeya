# Obeya · EMY

Локално табло за управление на задачи, решения и идеи за проекта EMY.

## 1. Инсталация

В PowerShell:

```powershell
cd C:\KINETRIX\Obeya
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Отворете `.env` и задайте:

- `SECRET_KEY`: дълга случайна стойност.
- `GOOGLE_CLIENT_ID` и `GOOGLE_CLIENT_SECRET`: от Google Cloud OAuth 2.0 Client.
- `ALLOWED_EMAILS`: до 3 позволени имейла, разделени със запетая.
- `USER_ROLES`: роли във формат `Role:email`, разделени със запетая.

В Google Cloud Console добавете този authorized redirect URI:

```text
http://localhost:5000/auth/google/callback
```

Ако влизате от друг компютър в локалната мрежа, добавете и URI с адреса на хоста, например:

```text
http://192.168.1.25:5000/auth/google/callback
```

## 2. Стартиране

```powershell
cd C:\KINETRIX\Obeya
.\.venv\Scripts\Activate.ps1
python app.py
```

Отворете `http://localhost:5000` на хоста. За останалите членове на екипа използвайте `http://<IP-на-компютъра>:5000`.

Приложението слуша на `0.0.0.0`, за да е достъпно в LAN. При нужда разрешете входящ TCP порт 5000 във Windows Firewall само за Private network:

```powershell
New-NetFirewallRule -DisplayName "Obeya Flask 5000" -Direction Inbound -Protocol TCP -LocalPort 5000 -Action Allow -Profile Private
```

Не отваряйте порта към Public network и не публикувайте приложението директно в интернет без HTTPS reverse proxy.

## 3. Функционалност

- Google OAuth вход с allowlist и роли за до трима потребители.
- Master Tasks Board с направления, отговорници, филтри, срокове и четири статуса.
- Decision log и Ideas Parking.
- SQLite базата `obeya.db` се създава автоматично при първо стартиране.

За production-like локална употреба задайте `FLASK_DEBUG=0` и сменете `SECRET_KEY`.
