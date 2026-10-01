# Product Requirements Document (PRD)
**Dr. Muhammad Hassan Tariq — Patient Acquisition Website**
**Version:** 1.0
**Date:** 2026-09-30
**Prepared for:** Antigravity (AI build agent)

## 1. Project Overview
Build a professional, fast, mobile-responsive website for Dr. Muhammad Hassan Tariq, a doctor based in Rahim Yar Khan, Punjab, Pakistan, specializing in Male Infertility & Childlessness / Male Reproductive Health and Pediatrics.
**Important:** This is NOT a clinic management system. There is no patient portal, no login, no online booking calendar. It is a conversion-focused platform — its single business goal is to bring patients to the doctor via WhatsApp. Every call-to-action on the site must lead to WhatsApp.

## 2. Goals
- Present the doctor as a trusted, board-certified specialist.
- List all services clearly in professional English.
- Funnel every visitor toward one action: contacting via WhatsApp for an appointment.
- Allow non-technical staff to edit services, qualifications, and clinic info via Django admin.

## 3. Tech Stack
- **Language:** Python 3.10+
- **Framework:** Django (latest stable)
- **Database:** SQLite (Django default — no extra configuration)
- **Frontend:** Plain HTML + CSS + minimal JavaScript (keep it fast, no heavy framework)
- **Environment:** Virtual environment (venv), dependencies pinned in requirements.txt
- **Deployment target:** PythonAnywhere or VPS with gunicorn (prepare wsgi.py, static collection, DEBUG=False checklist)

**Constraints:**
- Do NOT add a custom user auth system, REST API, or any JavaScript framework.
- Keep third-party packages to a minimum (Django only, unless strictly needed).

## 4. Target Users
Patients (or their families) in Rahim Yar Khan and surrounding areas seeking male fertility, hormonal, diabetes, or children's health care.
Mostly mobile users, Urdu-speaking, low-to-medium digital literacy → the site must be simple, with one obvious action (WhatsApp button).

## 5. Site Structure (Pages)
### 5.1 Home (/)
- **Top bar (dark blue):** phone 0339-8770001 · location Rahim Yar Khan · timings Mon–Sat · 9AM – 6PM
- **Navbar (white):** Logo Dr. MHT + tagline Reproductive Health & Pediatrics. Links: Home, About, Services, Men's Health, Pediatrics, Diabetes, Contact. Blue Book Appointment button.
- **Hero (two-column):**
  - **Left:** badge Board-Certified · Male Reproductive Health & Pediatrics; H1 Dr. Muhammad Hassan Tariq; subheading (blue) Male Infertility and Childlessness; paragraph in professional English describing compassionate, evidence-based care for male fertility, hormonal health, diabetes, and paediatric well-being; blue Book Appointment → button; three trust badges with icons: Confidential & Compassionate, Evidence-Based Treatments, Family-Centred Care.
  - **Right:** doctor portrait photo in a rounded card with light-blue decorative background shapes.
- **Services section (light blue background #EAF3FB):** heading Our Services, subheading Specialized care tailored to your health journey. Three white cards:
  - Male Infertility Evaluation — semen analysis, hormonal profiling, personalized fertility assessment.
  - Pediatric Health & Care (Amraaz-e-Atfaal) — paediatric consultations, growth monitoring, vaccinations, child health guidance.
  - Diabetes & Hormonal Health — diabetes management, hormonal imbalance diagnosis, endocrine support.
  - Each card: blue circular icon, English description, Learn more → link.
- **Two-column section:** Clinic Timings card (Mon–Sat 9:00 AM – 6:00 PM, Sunday Closed, walk-ins welcome subject to availability, Location: Rahim Yar Khan, Punjab, Pakistan) + Why Choose Us? (Over 8+ years of experience in male reproductive health; Combined expertise in paediatrics & fertility care; Private, respectful, and patient-centred approach).
- **Footer (dark blue):** © 2026 Dr. Muhammad Hassan Tariq · Rahim Yar Khan · 0339-8770001 · All rights reserved
- **Floating WhatsApp button** (bottom-right, green) with tooltip Chat with us on WhatsApp.

### 5.2 Service Detail (/services/<slug>/)
Full English description of the selected service, symptoms/conditions treated, and a prominent WhatsApp CTA (Book Appointment on WhatsApp).

### 5.3 About (/about/)
Doctor introduction + full qualifications list:
- MBBS (FMH), Lahore
- Masters in Male Infertility, UK
- Fellow, Academy for Men's Health, Singapore
- Certified, South Asian Society for Sexual Medicine (SASSM)
- American Diabetes Association Certified, USA

### 5.4 Contact (/contact/)
Phone number, WhatsApp button, city, clinic timings. No contact form needed (WhatsApp is the contact method).

## 6. Content — Services Seed Data
### 6.1 Male Reproductive Health
Varicocele · Hydrocele · Azoospermia · Low Sperm Count · Hormonal Deficiency · Premature Ejaculation · Delayed Puberty · Male Weakness · Obesity-related fertility issues

### 6.2 Pediatrics (Amraaz-e-Atfaal / Bachon ki Bimariyan)
Fever · Cold, Flu & Cough · Allergies · Asthma · Nutritional Deficiency · Delayed Growth & Development

### 6.3 Diabetes
Diabetes Management · Reduced Sexual Desire due to Diabetes · ADA-certified diabetes care · Hormonal imbalance diagnosis & endocrine support

**Wording rule:** ALL website copy in professional English, medical tone. No Roman Urdu on the site itself.

## 7. Design Requirements
- **Color scheme:** BLUE-WHITE combination.
  - Primary dark blue: `#0B3C6E` (top bar, footer, headings)
  - Primary blue: `#1E7FDB` or similar (buttons, accents)
  - Light blue backgrounds: `#EAF3FB`
  - White cards and navbar, dark navy text `#102A43`
  - WhatsApp green `#25D366` for the floating button only
- **Layout reference:** copy the section order and layout structure of the provided brown-theme reference design, translated into the blue-white palette (top bar → navbar → hero → services → timings/why-choose-us → footer).
- **Typography:** clean sans-serif (system stack or Inter). Large, confident headings.
- **Fully responsive:** must look correct on mobile (single column stacking, tappable buttons, sticky/floating WhatsApp button always visible).
- **Use the provided doctor portrait image.**

## 8. WhatsApp Integration (Critical)
- **WhatsApp number:** 923398770001
- **Prefilled message:** Assalam-o-Alaikum, mujhe Dr. Muhammad Hassan Tariq se appointment chahiye
- **Link format:** `https://wa.me/923398770001?text=<URL-encoded message>`
- Every Book Appointment button, the floating button, and all CTAs must open this link in a new tab.
- Implement via a Django context processor so the link is defined once and reused in all templates.

## 9. Data Models
- `Service` — title, slug, icon_name, short_description, full_description, category (choices: male_health, pediatrics, diabetes), order
- `Qualification` — degree_title, institution, country, order
- `ClinicInfo` (singleton) — phone_number (default 0339-8770001), whatsapp_number (default 923398770001), city (default Rahim Yar Khan), timings_weekdays, timings_sunday, address
- Provide a management command `seed_content` that populates all qualifications, services (§6), and clinic info.

## 10. Admin Requirements
- Register Service, Qualification, ClinicInfo in Django admin with sensible list_display, list_filter (category), and ordering.
- Staff must be able to edit all site content without touching code.

## 11. Non-Functional Requirements
- Page load fast on 3G mobile connections (minimal CSS/JS, optimized images).
- SEO: unique `<title>` and meta description per page, Open Graph tags, sitemap.
- DEBUG=False deployment checklist, collectstatic configured.
- `.gitignore` must exclude `venv/`, `db.sqlite3`, `__pycache__/`.

## 12. Build Phases
| Phase | Deliverable |
|---|---|
| 0 | Fresh environment: venv, Django installed, requirements.txt, version verified |
| 1 | Django project doctor_site + app website, dev server runs |
| 2 | Models, migrations, seed_content with all data from §6 and §5.3 |
| 3 | Views, URLs, context processor (WhatsApp link), templates wired |
| 4 | Blue-white templates per §5 and §7, responsive, doctor portrait integrated |
| 5 | Admin registration, SEO, sitemap, deploy checklist, final link verification |

## 13. Acceptance Criteria
- [ ] `python manage.py runserver` works from a fresh venv using only `requirements.txt`
- [ ] All 5+ qualifications, 15+ services, and clinic info visible on the site from seed data
- [ ] Every CTA on every page opens the correct `wa.me` link with the prefilled message
- [ ] Layout matches the reference design structure in blue-white; fully responsive on mobile
- [ ] All copy in professional English; phone 0339-8770001 and city Rahim Yar Khan correct everywhere
- [ ] Admin panel allows editing services, qualifications, and clinic info
- [ ] No broken links, no missing images, no console errors
